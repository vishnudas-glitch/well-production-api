GET_WELL_DATA_DOC = {
    'parameters': [
        {
            'name': 'well',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'API WELL NUMBER'
        }
    ],
    'responses': {
        200: {
            'description': 'Well data response',
            'examples': {
                'application/json': {
                    "status": "success",
                    "status_code": 200,
                    "comment": "Well data retrieved successfully",
                    "data": {
                        "OIL": 862,
                        "GAS": 230195,
                        "BRINE": 2050
                    }
                }
            }
        },
        400: {
            'description': 'Missing or invalid well number'
        },
    }
}