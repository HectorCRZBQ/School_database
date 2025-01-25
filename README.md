# Proyecto: Aplicación FLASK con BBDD de un Colegio (School_database)

## Instrucciones de Ejecución
1. Abre una terminal y ejecuta el script `main.py`.
2. Introduce en la terminal el usuario y la contraseña de PostgreSQL.

Si tenemos instalado PostgreeSQL avnzar al paso **6**

3. Si no tenemos instalado PostgreSQL se puede isntalar con los siguientes comandos:
  ```
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```
Cambiamos al usuario **postgres** y acedemos al psql:
```
sudo -i -u postgres
psql
```
Creamos el usuario con los credenciales que le añados declarado, usuario y contraseña:
```
CREATE USER username WITH PASSWORD 'password';
```
Otorgamos permisos necesarios y salimos:
```
ALTER USER username CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE main TO username;
\q
exit
```
4. Abre una terminal y ejecuta el script `main.py`.
5. Introduce en la terminal el usuario y la contraseña de PostgreSQL.
![img](images/image.png)


6. Ejecuta el script `app.py`.

(Conexión con Atlas MongoDB)

Modificamos el valor de **uri** en el archivo **mongo.py**:
"mongodb+srv://username:password@atlascluster.wmcjicr.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

(Conexión con Base de Datos Local de PostgreSQL)

Modificamos el valor de **uri** en el archivo **mongo.py**:
uri = "mongodb://username:password@localhost:27017/main"


Se necesita una conexión con la base de datos de Atlas, para ello se usa una URI como la siguiente: 

Al completar estos pasos:
- Se crearán automáticamente las bases de datos, tablas, índices y triggers necesarios.
- Se abrirá la aplicación en el navegador.

Terminal (esta preuba es en local):
![img](images/image-2.png)

Aplicación en el navegador:
![img](images/image-3.png)

## Modificar el numero de elementos creados con Faker

Dentro del código de `insert.py` se declaran los siguientes valores:

```
num_courses = 150
num_alumns = 1000
num_teachers = 10
alumns_per_course = 50
```

* Donde **num_courses** nos marca el numero de cursos que queremos que se creen, en este caso son **150**.

* Donde **num_alumns** nos marca el numero de alumnos que queremos que se creen, en este caso son **1000**.

* Donde **num_teachers** nos marca el numero de profesores que queremos que se creen, en este caso son **10**.

* Donde **alumns_per_course** nos marca el numero de alumnos por curso que queremos que se asignen, en este caso son **50**.


## Funcionalidades Principales

### Menú Principal

**Si hacemos la prueba en local asegurarnos de que esta iniciado correctamente, sino ejecutar los siguientes comandos:**

```
sudo systemctl status mongod
sudo systemctl start mongod
```

Una vez registrado e iniciado sesión, podrás acceder a las siguientes secciones:
![img](images/image-4.png)

#### **Buscador**
- Permite buscar palabras clave en la página principal de la web de la UCJC almacenada en una base de datos Elasticsearch.

![img](images/image-5.png)

#### **Universidad**
- Visualización de las tablas principales:
![img](images/image-6.png)

  - **Alumnos**
  ![img](images/image-7.png)

  - **Profesores**
  ![img](images/image-8.png)

  - **Asignaturas**
  ![img](images/image-9.png)

#### **Consultas**
- Acceso a las siguientes consultas sobre la base de datos:
![img](images/image-10.png)

  1. Número de alumnos diferentes y cursos asociados a un profesor.
  ![img](images/image-11.png)

  2. Relación entre curso, alumno y profesor.
  ![img](images/image-12.png)

  3. Número de cursos y profesores asociados a un alumno.
  ![img](images/image-13.png)


#### **Auditoría**
- Visualización de las operaciones realizadas (inserciones, eliminaciones y actualizaciones) en las tablas de alumnos, profesores y asignaturas.

![img](images/image-14.png)

## Características Adicionales

- Navegación: Puedes regresar al menú principal desde cualquier sección de la aplicación.
- Seguridad: Los campos de entrada están protegidos contra inyección de código.
- Registro de Actividad: Cada acción realizada por el usuario se registra en una base de datos MongoDB con:
  - Nombre del usuario.
  - Ruta accedida.
  - IP del dispositivo.
  - Fecha y hora.
  - Datos resultantes de la operación, si aplica.

## Funcionalidades Opcionales

### **Mejora de Interfaz**
Permite realizar las siguientes acciones directamente desde la aplicación:
1. Inserción de un elemento.
2. Eliminación de un elemento.
3. Actualización de un elemento.
4. Consulta del historial de cambios de un elemento.
5. Búsqueda de un elemento.

![img](images/image-15.png)

Estas funciones están disponibles para las tablas:
- Alumnos.
- Profesores.
- Asignaturas.
- Auditoría y consultas específicas.

### **Optimización con Paginación**
- Al acceder a una tabla, solo se cargará un número limitado de filas.
- Navegación entre páginas mediante botones "anterior" y "siguiente".
- Visualización del número de página actual, total de páginas y total de elementos.

### Detalles de Actualización
- No es necesario rellenar todos los campos; los campos vacíos mantienen su valor original.
- Actualización de asignaturas:
  - Solicita el ID del profesor.
  - Modifica en cascada las relaciones asociadas.

### Eliminación en Cascada
- La eliminación de un alumno, profesor o asignatura también elimina sus referencias en otras tablas relacionadas.

##Aquí tienes una sección para los autores, más profesional y formal:  

## **Autores**

Este proyecto ha sido desarrollado por:  

- **Álvaro Rivas Álvarez**  
  [GitHub: Alvaro5473](https://github.com/Alvaro5473)  

- **Héctor de la Cruz Baquero**  
  [GitHub: HectorCRZBQ](https://github.com/HectorCRZBQ)  

---
¡Disfruta explorando la aplicación! 🚀