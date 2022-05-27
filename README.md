# Prueba

#  Instalación

Primero diríjase a la carpeta donde va a instalar el proyecto.
```
C:\Users\user> cd [Direccion de la carpeta] 
```
Una vez este en la carpeta clone el proyecto.
```
C:\Users\user\..\carpeta> git clone https://github.com/sebitacio/Prueba.git
```
Ahora debe crear una virtual environment, iniciarlo y instalar los paquetes necesarios.
```
C:\Users\user\..\Prueba> python -m venv env
C:\Users\user\..\Prueba> env\Scripts\activate
(env) C:\Users\user\..\Prueba> python -m pip install --upgrade pip
(env) C:\Users\user\..\Prueba> pip install -r requirements.txt
```
Ahora debe crear el archivo config.py este debe ir en la carpeta principal
```
Prueba
|_ app
|_ config.py
```
Para crear el archivo utilice el código de abajo como plantilla
```python
class Config():
    # Configuración general
    SECRET_KEY = 'Llave secreta' # Puede ser cualquier string

    # Extensiones
    TRUORA_API_KEY = 'my api key'
```

ahora puede iniciar la aplicación de la siguiente manera

```
(venv) C:\Users\user\..\Prueba> SET FLASK_APP=wsgi.py
(venv) C:\Users\user\..\Prueba> flask run
```
Una vez hecho esto aparecera lo siguiente
```
* Serving Flask app "wsgi.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 587-035-174
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Al dirigirse a http://127.0.0.1:5000/ vera la pantalla principal.
