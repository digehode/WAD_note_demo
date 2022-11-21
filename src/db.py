""" Module to help connect to the MySQL database management system """
import sqlalchemy
import models

# You shouldn't need to change anything in this file

def create_engine(user,password,port,dbname):
    """ Create a DB engine and return it. Mostly for internal use.

    Arguments:

     - user: username for the database
     - password: password for the database
     - port: port for the database
     - dbname: name of the database

    """
    return sqlalchemy.create_engine(f"mariadb+mariadbconnector://{user}:{password}@127.0.0.1:{port}/{dbname}")


def create_db(user, password, port, dbname):
    """ Create the database according to the models in the models.py file """
    engine = create_engine(user,password,port,dbname)    
    models.Base.metadata.create_all(engine)


def connect(user,password,port,dbname):
    """ Connect to the database and return a session object for making queries

    Arguments:

     - user: username for the database
     - password: password for the database
     - port: port for the database
     - dbname: name of the database

    """
    engine = create_engine(user,password,port,dbname)
    session = sqlalchemy.orm.sessionmaker()
    session.configure(bind=engine)
    return session()
