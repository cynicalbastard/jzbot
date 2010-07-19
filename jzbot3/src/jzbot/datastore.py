
import pymongo #@UnresolvedImport


# A hack to get pydev to stop reporting errors about the module global db not
# existing when we try to access it
class _Dummy(object):
    def __getattr__(self, name):
        raise Exception()

db_name, connection, db = _Dummy(), _Dummy(), _Dummy()


def init(local_db_name):
    global db_name, connection, db
    db_name = local_db_name
    connection = pymongo.Connection()
    db = connection[db_name]



    
