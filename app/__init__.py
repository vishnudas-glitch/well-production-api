import os
import logging
from flask import Flask
from flasgger import Swagger
from app.config.settings import settings
from app.config.db.database import init_app
from app.routes import routes_bp


def create_app() -> Flask:
    app = Flask(__name__)

    configure_logging()
    configure_swagger(app)

    init_app(app)
    app.register_blueprint(routes_bp)

    return app




def configure_logging() -> None:
    file_handler = logging.FileHandler(settings.LOG_FILE_NAME)
    file_handler.setLevel(logging.ERROR) 
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))
    logger = logging.getLogger()
    logger.handlers = [] 
    logger.setLevel(logging.ERROR)
    logger.addHandler(file_handler)
    
    # Add console handler for development environments
    if settings.DEBUG:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        logger.addHandler(console_handler)


def configure_swagger(app: Flask) -> None:
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": settings.API_TITLE,
            "description": settings.API_DESCRIPTION,
            "version": settings.API_VERSION
        },
        "basePath": "/"
    })