import json
import pytest
from app import create_app, db
from app.models import Contract, Template

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_upload_contract(client):
    data = {'file': (io.BytesIO(b"sample contract text"), 'contract.pdf')}
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert 'id' in response.get_json()

def test_upload_template(client):
    template = {
        'name': 'Sample Template',
        'structure': json.dumps({
            "agreement": ["agreement"],
            "confidentiality": ["confidentiality"],
            "party": ["party"],
            "termination": ["termination"],
            "liability": ["liability"],
            "governing law": ["governing law"],
            "jurisdiction": ["jurisdiction"],
            "indemnity": ["indemnity"],
            "warranty": ["warranty"],
            "obligation": ["obligation"],
            "payment": ["payment"],
            "force majeure": ["force majeure"],
            "amendment": ["amendment"],
            "assignment": ["assignment"],
            "severability": ["severability"],
            "dispute resolution": ["dispute resolution"],
            "arbitration": ["arbitration"],
            "intellectual property": ["intellectual property"],
            "limitation of liability": ["limitation of liability"],
            "entire agreement": ["entire agreement"]
        })
    }
    response = client.post('/template', data=json.dumps(template), content_type='application/json')
    assert response.status_code == 200
    assert 'id' in response.get_json()

def test_validate_contract(client):
    contract = Contract(content='sample contract text', parsed_content=[])
    db.session.add(contract)
    db.session.commit()
    
    response = client.get(f'/validate/{contract.id}')
    assert response.status_code == 200
