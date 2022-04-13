import re
from datetime import datetime
from http import HTTPStatus

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.configs.database import db
from app.models.leads_model import Lead


def create_leads():
    data = request.get_json()
    valid_keys = ["name", "email", "phone"]

    check_type_values = [key for key in data.values() if type(key) != str]
    if len(check_type_values) > 0:
        return {"Error": "All fields passed must be a string"}, HTTPStatus.BAD_REQUEST

    data_keys = [key for key in data.keys()]
    if data_keys != valid_keys:
        return {
            "Error": "They must be sent only and obligatorily name, cpf and phone"
        }, HTTPStatus.BAD_REQUEST

    regex = r"^\(\d{2}\)\d{5}-\d{4}$"
    phone = data["phone"]

    match = re.fullmatch(regex, phone)
    if not match:
        return {
            "Error": "Phone must be in the format (xx)xxxxx-xxxx"
        }, HTTPStatus.BAD_REQUEST

    data["name"] = data["name"].title()

    new_lead = Lead(**data)

    try:
        session: Session = db.session()
        session.add(new_lead)
        session.commit()
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return jsonify({"Error": e.args[0][99:152]}), HTTPStatus.CONFLICT

    return jsonify(new_lead), HTTPStatus.CREATED


def retrieve_leads():
    base_query = db.session.query(Lead)

    leads = base_query.order_by(Lead.visits.desc()).all()

    return jsonify(leads), HTTPStatus.OK


def update_leads():
    data = request.get_json()
    check_key = [key for key in data.keys()]
    check_values = [value for value in data.values()]

    if check_key != ["email"]:
        return {"Error": "Only the email should be sent"}, HTTPStatus.BAD_REQUEST
    if type(check_values[0]) != str:
        return {"Error": "The email must be a string only"}, HTTPStatus.BAD_REQUEST

    session: Session = db.session

    lead = session.query(Lead).filter_by(email=data["email"]).first()

    if not lead:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND

    update_lead = {"last_visit": datetime.now(), "visits": lead.visits + 1}

    for key, value in update_lead.items():
        setattr(lead, key, value)

    session.add(lead)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


def delete_leads():
    data = request.get_json()

    check_key = [key for key in data.keys()]
    check_values = [value for value in data.values()]

    if check_key != ["email"]:
        return {"Error": "Only the email should be sent"}, HTTPStatus.BAD_REQUEST
    if type(check_values[0]) != str:
        return {"Error": "The email must be a string only"}, HTTPStatus.BAD_REQUEST

    session: Session = db.session

    lead = session.query(Lead).filter_by(email=data["email"]).first()

    if not lead:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND

    session: Session = db.session()
    session.delete(lead)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
