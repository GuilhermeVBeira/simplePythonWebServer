import sys, os
from server import start_server
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.models.tables import DataBase
from app.settings import DATA_BASE

if __name__ == '__main__':
    PORT = "8080"
    HOST = "0.0.0.0"
    db = DataBase(DATA_BASE)
    db.boot_database()
    try :
        start_server(sys.argv[1])
    except :
        start_server("%s:%s" % (HOST,PORT))