import re
from flask import (
    current_app as app,
    redirect, url_for, render_template, request, session, flash)
import requests as rq
import json


@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")


@app.route('/create-validation', methods=["POST"])
def create_validation():
    # leer valores del formulario
    country = request.form["country"]
    document_type = request.form["document-type"]
    user_authorized = request.form.get("user-authorized", False)
    id_front = request.files["front-input"]
    id_back = request.files["back-input"]

    # Crear validación
    url = "https://api.validations.truora.com/v1/validations"

    headers = {
        'Truora-API-Key': app.config['TRUORA_API_KEY'],
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = f"type=document-validation&country={country}&document_type={document_type}&user_authorized={'true' if user_authorized else 'false'}"

    response = rq.post(
        url=url,
        headers=headers,
        data=payload
    )

    if response.status_code == 200:
        document_validation = json.loads(response.text)
        validation_id = document_validation.get("validation_id","")
        session['validation_id'] = validation_id

        # Aqui va el codigo para subir la foto de la id frontal

        # Aqui va el codigo para subir la foto de la id trasera

        # Get validation
        url = f"https://api.validations.truora.com/v1/validations/{validation_id}"
        response = rq.get(
            url=url,
            headers=headers,
        )
        validation = json.loads(response.text)
        validation_status = validation.get('validation_status',"")
        if response.status_code == 200:
            flash(f'Your validation is {validation_status}')
            return redirect(url_for('index'))
        else:
            flash('Sorry, something went wrong')
            redirect(url_for('index'))
    else:
        flash('Sorry, something went wrong')
        return redirect(url_for('index'))