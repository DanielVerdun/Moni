# Moni


MoniApp - Simulación. 
-------------------------------------------------------------------

Esta App  permite solicitar un prestamo cargando los datos del usuario en un formulario y luego 
de hacer POST los guarda el registro en una BBDD. Trabaja con models, views, templates

Contiene un Usuario administrador, el cual tiene  permisos de acceso a la lista de prestamos validando
su identidad por medio de un login permitiendo
realizar un CRUD sobre cada uno de los prestamos solicitados.

Pre requisitos: Python / Django
Para poder correr el proyecto se recomienda crear un entorno virtual
$ virtualenv venv

Activiacion de entorno 
$ source venv/bin/activate

Luego clonar le proyecto en el directorio donde creamos el entorno virtual y debemos instalar en archivo requirements.txt
$ pip install -r requirements.txt

Correr las migraciones 
$ python manage.py migrate

Arrancar el servidor 
$ python manage.py runserver
