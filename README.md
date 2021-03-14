# Django

Configuración simple para un proyacto con Django

## Installation

Clone el proyecto

1. Creé Virtual env
```bash
python -m venv .venv
```

2. Instale las dependecnias
```bash
pip install -r requirements.txt
```

3. Configura tu base de datos

En este ejemplo, una base de datos de Postgres ya está configurada solo para el entorno de producción.

Para el entorno de desarrollo utiliza SQLite3

4. Crea un archivo ```.env``` en el directorio root. Esto manejará sus variables de configuración.
Ejemplo:
```
ENVIRONMENT=dev
SECRET_KEY=N0t_A_S3Cr3T
DEBUG=True
DATABASE_NAME=db_name
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
LANGUAGE_CODE=es-mx
TIME_ZONE=America/Mexico_City
DEFAULT_EMAIL_FROM=correo@correo.com
SERVER_EMAIL=server.com
EMAIL_HOST=
EMAIL_PORT=465
EMAIL_HOST_USER=email_user
EMAIL_HOST_PASSWORD=email_passwd
EMAIL_USE_TLS=True
```

Para la variable `ENVIRONMENT`, los valores pueden ser: `dev` o `production`

5. Cree las carpetas de migraciones en cada app

6. Corre migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Crea un super usuario
```bash
python manage.py createsuperuser
```

Puede ser que quiera crear un super usuario desde GitBash, para ese caso se usa el comando
```
winpty python manage.py createsuperuser
```

8. Esto sirve unicamente para correr django en un ambiente de desarrollo, no incluye configuraciones de Vue Js, React o algún otro framework para la reactividad

9. Configure su correo y servidor smtp en esta parte del .env
```
SERVER_EMAIL=smtp.gmail.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=correo@correo.com
EMAIL_HOST_PASSWORD=tu_clave_de_tu_correo_de_smtp
EMAIL_USE_TLS=True
```

10. En el archivo apps > mail > utils linea 194, ponga el correo del receptor

11. En el navegador de su preferencia ejecute el siguiente endpoint
```
http://localhost:8000/api/v1/mails/
```
e indique los datos te titulo(String), Fecha de la cita y hora de la cita (DateTime), Duración de la cita(int)

NOTA: este proyecto está no está configurado ni optimizado para un entorno de producción, no sirve para iniciar proyectos, no sirve para crear la documentación automática de el código; la configuración que tiene es para un entorno de desarrollo pero no es funcional del todo; tomese este proyecto como un ejemplo para enviar correos con formato outlook y no para iniciar un proyecto nuevo. El módulo de usuarios solo está configurado para poder entrar al administrador de Django en caso de que el endpoint no se pueda ejecutar. Este proyecto es solo un ejemplo de como realizar una tarea especifica y no representa un sistema terminado o una solución para su empresa.