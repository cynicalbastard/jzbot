
class UserNotTracked(Exception):
    """
    Raised when an operation on a User object is attempted but the user is not
    currently being tracked.
    """

class TransientConflict(Exception):
    """
    Raised when a transient conflict occurs while initially trying to register
    a user with a server.
    """
