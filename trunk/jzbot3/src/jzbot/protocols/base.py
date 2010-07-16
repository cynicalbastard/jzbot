# This defines stub functions that all protocols must have.
# The eventual idea is that JZBot will check all protocols
# against the functions listed here to make sure that they
# are compatible before using the protocol.

def _todo():
    raise NotSupported("This method still needs to be implemented by " + 
                    " the protocol subclass")


class NotSupported(Exception):
    """
    An exception that can be raised from some protocol methods to indicate
    that the specified method is not supported by the protocol. Methods will
    specify what action the bot will take if this exception is raised when
    calling the method.
    """
    pass


class Protocol(object):
    def __init__(self, server):
        """
        Initializes this protocol instance. Subclasses should call this
        method; it will set the server field to be the specified server.
        """
        self.server = server
    
    def send_action(self, user, message):
        """
        Instructs the protocol to send the specified CTCP action to the
        specified user. If this method raises NotSupported, the bot will call
        send_message with the message altered somewhat.
        """
        _todo()
    
    def send_message(self, user, message):
        """
        Instructs the protocol to send the specified message to the specified
        user.
        """
        _todo()
    
    def send_notice(self, user, message):
        """
        Instructs the protocol to send the specified notice to the specified
        user. If this method raises NotSupported, the bot will call
        send_message with the message altered somewhat.
        """
        _todo()
    
    def send_invite(self, user, channel):
        """
        Instructs the protocol to invite the specified user to the specified
        channel.
        """
        _todo()
    
    def connect(self):
        """
        Instructs the protocol to connect itself to the server and log in.
        This method does not need to return immediately; it can delay while,
        for example, the server processes account information and logs the
        user in. Once this method returns, the protocol should be in a state
        that other methods such as send_message can be invoked successfully.
        """
        _todo()
    
    def join_channel(self, channel):
        """
        Instructs the protocol to join a particular channel. This method
        should return immediately, and then when the channel actually gets
        joined, server.on_self_join_channel should be called. 
        """
        _todo()
    
    def get_max_length(self):
        """
        Returns the maximum length that a message can be for this protocol to
        send it successfully. Messages will be truncated or split up by the
        bot in order to ensure that a message longer than this is never sent
        to the protocol.
        """
        _todo()
    
    
    























