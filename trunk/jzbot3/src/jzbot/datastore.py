
import pymongo #@UnresolvedImport

def init(local_db_name):
    global db_name, connection, db
    db_name = local_db_name
    connection = pymongo.Connection()
    db = connection[db_name]



    
