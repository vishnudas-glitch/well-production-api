from flask import Blueprint, request, jsonify
from flasgger import swag_from
import logging

from app.helpers.utils import make_response
from app.services.well_service import get_well_data_from_db
from app.routes.swagger.well_production import GET_WELL_DATA_DOC

logger = logging.getLogger(__name__)
well_api_bp = Blueprint('api', __name__)

@well_api_bp.route('/data', methods=['GET'])
@swag_from(GET_WELL_DATA_DOC)
def get_well_data():
    well_number = request.args.get('well')
    
    if well_number:
        try:
            records = get_well_data_from_db(well_number)
            if records:
                return records
                

            return make_response(
                data=None,
                status="error",
                code=404,
                comment=f"No data found for well: {well_number}"
            )
            
            
        except Exception as e:
            logger.exception(f"Error retrieving well data: {e}")
            return make_response(
                data=None,
                status="error",
                code=400,
                comment="Something went wrong"
            )
    else:
        return make_response(
            data=None,
            status="error",
            code=400,
            comment="Missing 'well' parameter"
        )

