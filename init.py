# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

import os

def create_ini(user, password):
    try:
        os.remove("main.ini")
        os.remove("audit.ini")
        os.remove("postgres.ini")

    except FileNotFoundError:
        pass

    template = """
        [postgresql]
        host=localhost
        database={database}
        user={user}
        password={password}
    """

    with open("main.ini", "w") as f:
        f.write(template.format(database="main", user=user, password=password))

    with open("audit.ini", "w") as f:
        f.write(template.format(database="audit", user=user, password=password))

    with open("postgres.ini", "w") as f:
        f.write(template.format(database="postgres", user=user, password=password))
    
def ask():
    user = input("Nombre de usuario de postgres: ")
    password = input("Contraseña de postgres: ")
    create_ini(user, password)

if __name__ == '__main__':
    ask()