from flask import Blueprint

from app.controllers.leads_controller import (
    create_leads,
    delete_leads,
    retrieve_leads,
    update_leads,
)

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.post("")(create_leads)
bp.get("")(retrieve_leads)
bp.patch("")(update_leads)
bp.delete("")(delete_leads)
