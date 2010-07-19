
from threading import Thread, RLock as Lock
from jzbot.utils.coreutils import Flag, reapply, redocument
from jzbot.utils.fileutils import File
from jzbot.utils.threadutils import as_new_thread
from jzbot.errors import UserNotTracked
import datastore
import jzbot.welcome as welcome_module
import os
import os.path
import shutil
import imp as importutils
import sys
import jzbot.datastore as datastore
from weakref import WeakValueDictionary
import errors
import time
import traceback


jzbot_is_running = Flag(True)

server_map = {}
base_folder = File(__file__).parent.parent.parent

def when_user_tracked(function):
    """
    A decorator that can be used to decorate methods on the User class. It
    checks to see if the user object the method is being invoked on is tracked
    before allowing the method to be called. If the user is not currently being
    tracked, errors.UserNotTracked is raised. Otherwise, the function
    invocation is allowed to continue.
    """
    def new_function(user, *args, **kwargs):
        if user.tracked != User.TRACKED:
            raise errors.UserNotTracked()
        return function(*args, **kwargs)
    redocument(function, new_function)
    return new_function


class User(object):
    """
    An IRC user on a particular server.
    
    Instances of this class represent a particular user for a particular
    connection. When the server disconnects, all corresponding user objects
    are dropped from tracking and will no longer function. This is in case
    another user on the server takes over a user's transient name while we're
    disconnected; we might otherwise think both users were really the same
    user, and that could result in some security issues. 
    """
    
    TRACKED = 0
    TRANSIENT_CONFLICT = 1
    DISCONNECTED = 2

    def __init__(self, server, local, transient_name, persistent_name=None, 
                 display_name=None, group_name=None, register=True):
        """
        Initializes this user. The user is created under the specified server.
        local is True if this represents the server's local user or False if
        this is just a user on the server. This will also register the user
        into the server's user map and the server's local_user field if local
        is True, as long as register is true. If register is false,
        registration is skipped and can later be performed by calling the
        register method. This is useful if the transient name isn't yet known.
        """
        self.server = server
        self.transient_name = transient_name
        self.persistent_name = persistent_name
        self.display_name = display_name
        self.group_name = group_name
        self.tracking = User.TRACKED
        self.local = local
        if register:
            self.register()
    
    def register(self):
        """
        Registers this user with the server. This involves adding the user to
        the server's user map and setting the user into the server's local_user
        field if this is marked as the local user.
        """
        with self.server.lock:
            # We need to make sure there's FIXME: finish this 
            if self.transient_name in self.server.user_map:
                other_user = self.server.user_map[self.transient_name]
                if other_user.local and not self.local:
                    raise errors.TransientConflict()
    
    @when_user_tracked
    def send_message(self, message):
        pass
    
    def set_transient_name(self, name):
        """
        Sets this user's transient name. If this user is being tracked, this
        will also update the mapping in the server's user dictionary.
        """
        with self.server.lock:
            if self.tracking != User.TRACKED:
                raise UserNotTracked("User object not tracked")
            if self.transient_name not in self.server.user_map:
                raise UserNotTracked("User object not in server's user map")
            if self.server.user_map[self.transient_name] is not self:
                raise UserNotTracked("User object being tracked is not self")
            self.server.user_map
    

class Channel(object):
    pass


class Server(object):
    """
    A server.
    """
    def __init__(self, db_object):
        self.user_map = WeakValueDictionary()
        self.channel_map = {}
        self.lock = Lock()
        self.update_from_database_object(db_object)
        self.needs_reconnect = Flag()
    
    def update_from_database_object(self, db_object):
        """
        Instructs this server to update itself from the specified database
        object, which should be the result of a query against the database.
        This updates the server's name, the server's protocol class, the
        server's activated state, and the server's config properties.
        """
        self.name = db_object["name"]
        self.active = db_object["active"]
        self.protocol_name = db_object["protocol"]
        self.config_properties = dict(db_object["config"])
    
    def get_user(self, transient_name):
        pass
    
    def init_user_info(self, transient_name, persistent_name=None,
                       display_name=None, group_name=None):
        """
        Called by the protocol constructor to set the initial information for
        the user. Once the constructor returns, at least the transient name
        must have been set by calling this method.
        """
        pass
    
    def disconnect(self, message=None):
        """
        Disconnects this server. This basically just forwards over to the
        corresponding protocol. It does not clear any of the server maps; use
        clear_session_data for that.
        """
        self.protocol.disconnect()
    
    def clear_session_data(self):
        """
        Clears the information for the last session from this server object.
        This involves clearing the channel map and the user map. This
        synchronizes on the server lock. 
        """
        with self.lock:
            self.user_map.clear()
            self.channel_map.clear()
            self.local_user = None
    
    def on_action(self, transient_name, message, persistent_name=None, 
                  display_name=None, group_name=None):
        """
        Called by a protocol when an action is received.
        """
        pass
    
    def on_message(self, transient_name, message, persistent_name=None,
                   display_name=None, group_name=None):
        """
        Called by a protocol when a message is received.
        """
        pass
    
    def on_connect(self, transient_name=None, persistent_name=None,
                   display_name=None, group_name=None):
        """
        Called when the server successfully connects. The user information
        provided to this method is the information for the user that the
        protocol has connected as. None of it is required.
        """
        pass
    
    def on_disconnect(self):
        """
        Called when the protocol disconnects from the server for some reason.
        """
        pass
    


class CommandSpooler(Thread):
    """
    A class to spool commands for a server
    """
    def __init__(self):
        Thread.__init__(self)


connection_cycle_needed = Flag(True)
connection_cycle_interval = 120 # 2 minutes


@as_new_thread
def start_connection_cycle_thread():
    while jzbot_is_running:
        for i in xrange(connection_cycle_interval / 2):
            time.sleep(2)
            if not jzbot_is_running:
                return
            if connection_cycle_needed:
                break
        try:
            do_single_connection_cycle()
        except:
            print "Exception in connection cycle thread:"
            traceback.print_exc()


def do_single_connection_cycle():
    # First we clear the flag indicating that we need to perform a
    # connection cycle.
    connection_cycle_needed.clear()
    # First we get the list of servers from the database
    db_server_list = list(datastore.db.servers.find({}))
    db_server_map = {}
    # Now we make sure we have a server object for each server we selected from
    # the database
    for db_server in db_server_list:
        if  db_server["name"] not in server_map:
            # We don't have a server object, so we'll create one.
            server = Server(db_server)
            server_map[server.name] = server
        db_server_map[db_server["name"]] = db_server
    # Now we iterate over all the servers and get everything connected up
    for name, server in server_map.items():
        if name in db_server_map:
            db_server = db_server_map[name]
        else:
            db_server = None
        # Check to see if the server is connected but it shouldn't be
        should_disconnect = (db_server is None or (not db_server["active"])
                             or server.needs_reconnect())
        if should_disconnect:
            # The server needs disconnecting, so we'll do exactly that.
            server.disconnect()
        # Now we check to see if the server is disconnected, and if it is, we
        # clear out its session data.
        if not server.is_connected():
            server.clear_session_data()


def load_configuration_module():
    configuration_path = base_folder / "storage" / "config.py"
    if not configuration_path.exists:
        (base_folder / "files" / 
         "default-config.py").copy_to(configuration_path)
    global configuration_module
    with open(configuration_path.path) as file:
        configuration_module = importutils.load_module("jzbot_config", file,
                configuration_path.path, (".py", "r", importutils.PY_SOURCE))
    if hasattr(configuration_module, "exit") and configuration_module.exit:
        print welcome_module.no_config_message
        sys.exit() 


def start():
    global db
    print welcome_module.message
    print "Initializing..."
    # Do we really have anything that needs to be run here?
    print "Loading configuration..."
    load_configuration_module()
    print "Connecting to MongoDB..."
    datastore.init(configuration_module.database_name)
    print "Starting connection cycle thread..."
    start_connection_cycle_thread()
    print "JZBot has successfully started up. Server connections will"
    print "be established momentarily."





























