# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import create_database

def create_databases():
    create_database("main")
    create_database("audit")