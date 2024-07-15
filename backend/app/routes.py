from flask import request, jsonify
from app import app, db
from app.models import Contract, Template
from app.ocr import parse_document
from app.nlp import classify_clauses
from app.deviation import detect_deviations

@app.route('/upload', methods=['POST'])
def upload_contract():
    file = request.files['file']
    content = parse_document(file)
    parsed_content = classify_clauses(content)
    contract = Contract(content=content, parsed_content=parsed_content)
    db.session.add(contract)
    db.session.commit()
    return jsonify(contract.id)

@app.route('/template', methods=['POST'])
def upload_template():
    data = request.get_json()
    template = Template(name=data['name'], structure=data['structure'])
    db.session.add(template)
    db.session.commit()
    return jsonify(template.id)

@app.route('/validate/<int:contract_id>', methods=['GET'])
def validate_contract(contract_id):
    contract = Contract.query.get(contract_id)
    deviations = detect_deviations(contract.parsed_content)
    return jsonify(deviations)
