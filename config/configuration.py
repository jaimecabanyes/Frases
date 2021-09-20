import os
import dotenv
import sqlalchemy as alch
from getpass import getpass
 

password = getpass("Introduce tu pass de sql: ")
dbName="mydb"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
print("me conecté")





