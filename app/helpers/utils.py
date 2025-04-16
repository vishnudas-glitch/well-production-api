from flask import jsonify

from app.models.base import OutModel


def make_response(data=None, status="success", code=200, comment=""):
    """Create a standardized API response."""
    response = OutModel(
        status=status,
        status_code=code,
        comment=comment or None,
        data=data
    )
    return jsonify(response.dict(exclude_none=True))
