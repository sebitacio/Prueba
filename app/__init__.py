from flask import Flask
import os

def create_app():
    ''' Configuracion de la aplicacion'''
    app = Flask(
        __name__,
        instance_relative_config=False)
    app.config.from_object('config.Config')

    # Inicializar plugins

    # Se asegura que la carpeta instance exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        # Incluir rutas, filtros y demas
        from . import routes

        # Registrar blueprints

    return app