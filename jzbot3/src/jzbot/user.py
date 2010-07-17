
import jzbot

"""
Indicates that a user object is currently being tracked.
"""
TRACKED = 0

"""
Indicates that a user object is not being tracked because a transient conflict
occurred. This is usually a problem with the protocol or the server.
"""
TRANSIENT_CONFLICT = 1

"""
Indicates that a user object is not being tracked because the server it
corresponds to has since disconnected.
"""
DISCONNECTED = 2


class User(object):
    def __init__(self, transient_name, persistent_name=None, 
                 display_name=None, group_name=None):
        self.transient_name = transient_name
        self.persistent_name = persistent_name
        self.display_name = display_name
        self.group_name = group_name
        self.tracking = TRACKED


class Channel(object):
    pass

























