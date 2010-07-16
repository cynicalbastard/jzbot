
import inspect


def redocument(old_function, new_function):
    """
    Copies old_function's docstring to new_function. Then, if the docstring
    does not start with "->", prepends "-> old_function(...)\n\n", where
    old_function is the name of the old function and ... is the parameter list
    to the function, to the docstring and sets the new docstring on the new
    function. The idea is that decorators that completely replace a function
    can use this to copy the old function's method signature into the docstring
    so that users can see what the function is supposed to do.
    
    This also copies old_function's __name__ to new_function.
    """
    new_function.__name__ = old_function.__name__
    new_function.__doc__ = old_function.__doc__
    if not new_function.__doc__.startswith("->"):
        new_function.__doc__ = (old_function.__name__ +
            inspect.formatargspec(*inspect.getargspec(old_function))
                                + "\n" + new_function.__doc__)


class Flag(object):
    """
    An object that can either be set or clear. Its boolean value is whether it
    is set or clear. It is callable; calling it sets it, as does calling its
    set method. Calling its clear method clears it.
    """
    def __init__(self, initial=False):
        """
        Creates a new flag. If initial is specified, it specifies whether the
        flag should start out set.
        """
        self.is_set = initial
    
    def set(self):
        self.is_set = True
    
    __call__ = set
    
    def clear(self):
        self.is_set = False
    
    def __nonzero__(self):
        return self.is_set


def reapply(function, repetitions, argument):
    """
    Calls the function specified with the specified argument the number of
    times specified by repetitions. The second invocation, instead of being
    passed the specified argument, will be passed the return value of the
    first invocation. After invoking the function the specified number of
    times, the final return value is returned.
    
    For example, reapply(os.path.dirname, 2, "/home/amboyd/example.py")
    returns "/home".
    """



















