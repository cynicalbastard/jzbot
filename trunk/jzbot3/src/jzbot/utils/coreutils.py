
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


class DynamicList(object):
    """
    A list-like object that only allows retrieval of elements. If you ask it
    for an element that doesn't yet exist, it will invoke the specified
    function repeatedly to generate items to add to the dynamic list until the
    dynamic list is large enough that the specified item can be retrieved.
    """
    def __init__(self, function):
        self.function = function
        self.items = []
    
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.get_or_add_item(item)
        return self.items[item]
    
    def get_or_add_item(self, item):
        while len(self.items) <= item:
            self.items.append(self.function())
        return self.items[item]
    
    def __iter__(self):
        return self.items.__iter__()


class IgnoreExceptions(object):
    """
    A context manager that ignores either all exceptions thrown from within it
    or exceptions from a specific list.
    """
    def __init__(self, *exceptions):
        """
        Creates a new context manager. If exceptions is present, it should be
        a list of exception classes, and only exceptions that are instances of
        classes in the list (or instances of subclasses in the list) will be
        caught and ignored.
        """
        # I can't remember if the args are passed as a tuple or as a list. If
        # they're passed as a tuple, we can remove the tuple constructor to
        # save on processing time.
        self.exceptions = tuple(exceptions) if len(exceptions) > 0 else None
    
    def __enter__(self):
        pass
    
    def __exit__(self, exception_type, value, traceback):
        if exception_type is None:
            return False
        if self.exceptions is None:
            return True
        return issubclass(exception_type, self.exceptions)

















