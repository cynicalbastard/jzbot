
import threading
import thread

import jzbot.utils.coreutils as coreutils


class SynchronizedInstance(object):
    """
    A class that can synchronize calls to methods on any object. Instances of
    this class allow any methods defined on the wrapped class to be called on
    this class, and the lock specified when constructing this class will be
    used to synchronize invocation of methods.
    """
    def __init__(self, target, lock=None):
        """
        Creates a new SynchronizedInstance object. Method invocations will
        delegate to the specified target. The specified lock, which should
        support the context manager protocol, will be used to synchronize
        method invocations. If no lock object is provided, a new one will be
        created.
        """
        self.synchronized_target = target
        self.synchronized_cache = {}
        self.synchronized_lock = lock or threading.RLock()
    
    def __getattr__(self, name):
        value = getattr(self.synchronized_target, name)
        if name in self.synchronized_cache:
            return self.synchronized_cache[name]
        def new_function(*args, **kwargs):
            with self.synchronized_lock:
                return value(*args, **kwargs)
        new_function.__name__ = value.__name__
        new_function.__doc__ = value.__doc__
        self.synchronized_cache[name] = new_function
        return new_function


def as_new_thread(function):
    """
    A function decorator that causes the decorated function to start in a new
    thread when invoked. When the function is called, it appears to return
    immediately. Behind the scenes, the function is invoked in a newly-
    created thread with the specified arguments. The function's return value
    is ignored by the thread.
    """
    def new_function(*args, **kwargs):
        thread.start_new_thread(function, args, kwargs)
    coreutils.redocument(function, new_function)
    return new_function
    



































