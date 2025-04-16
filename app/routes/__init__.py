from flask import Blueprint
from app.routes.well_production import well_api_bp


routes_bp = Blueprint('api', __name__)

routes_bp.register_blueprint(well_api_bp)