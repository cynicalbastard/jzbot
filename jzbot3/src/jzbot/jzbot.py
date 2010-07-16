
from threading import Thread, RLock as Lock
from jzbot.utils.coreutils import Flag, reapply
from jzbot.utils.fileutils import File
from jzbot.utils.threadutils import as_new_thread
import datastore
import jzbot.welcome as welcome_module
import os
import os.path
import shutil
import imp as importutils
import sys
import jzbot.datastore as datastore

server_map = {}
base_folder = File(__file__).parent.parent.parent

class Server(object):
    """
    A server.
    """
    def __init__(self):
        pass


class CommandSpooler(Thread):
    """
    A class to spool commands for a server
    """
    def __init__(self):
        Thread.__init__(self)


connection_cycle_needed = Flag(True)


@as_new_thread
def start_connection_cycle_thread():
    pass


def do_single_connection_cycle():
    connection_cycle_needed.clear()
    # Finish this up


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





























