import sqlite3
import sys
from back.liste_ville import list_ville
from back.create_schema import create_schema  
from back.refresh import refresh



def main():
    """This function connect to the the
    database 'transport.db' create the table
    and refresh the row in the table
    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    create_schema(c)
    refresh(list_ville[0], c, conn)
    refresh(list_ville[1], c, conn)    

if __name__ == "__main__":
    sys.exit(main())