
import os
import os.path
import shutil


class File(object):
    """
    An object representing a file. It makes the interface offered by os,
    os.path, and shutil more object-oriented.
    """
    def __init__(self, path):
        """
        Creates a new file object from the specified path. The path will be
        normalized before being stored.
        """
        self.path = os.path.abspath(path)
    
    @property
    def parent(self):
        """
        A property containing a File object representing the folder that
        contains this file or folder.
        """
        return File(os.path.dirname(self.path))
    
    def copy_to(self, dest):
        """
        Copies this file to the specified file. The specified file must be
        a full file path, not the path of a directory to copy this file to.
        This method does not work on folders. dest can be either a path or
        another File object. If the specified file already exists, it will be
        replaced by this one.
        """
        if isinstance(dest, str):
            dest = File(dest)
        shutil.copyfile(self.path, dest.path)
    
    def __div__(self, other):
        if not isinstance(other, str):
            raise Exception("Argument to file __div__ has to be a str")
        return File(os.path.join(self.path, other))
    
    @property
    def exists(self):
        """
        A property that indicates whether the file referenced by this File
        object actually exists.
        """
        return os.path.exists(self.path)
    
    def list(self):
        """
        Returns a newly-created list containing one File object for each
        folder within the folder represented by this File object. I don't
        exactly know what will happen if you call this on a file that doesn't
        exist or that isn't a folder, so don't try it.
        """
        return [File(os.path.join(self.path, name)) 
                for name in os.listdir(self.path)]

















