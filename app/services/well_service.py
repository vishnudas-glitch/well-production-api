from typing import Dict, List
import logging
from app.config.db.database import get_db

logger = logging.getLogger(__name__)

def get_well_data_from_db(api_number: str) -> Dict:
    try:
        db = get_db()
        query = """
            SELECT OIL, GAS, BRINE
            FROM well_production
            WHERE "API WELL  NUMBER" = ?
        """
        row = db.execute(query, (api_number,)).fetchone()
        return dict(row) if row else None
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise
