# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import create_database, delete_database
from init import ask
import create_main_tables
import create_audit_tables
from insert import insert_all

if __name__ == '__main__':
    ask()
    # delete_database("main")
    # delete_database("audit")
    create_database("main")
    create_database("audit")
    create_main_tables.create_tables()
    insert_all()
    create_audit_tables.create_tables()
