from app.nlp import classify_clauses

def test_classify_clauses():
    content = """
    This agreement is made between the first party and the second party.
    The payment will be made in installments.
    Each party has certain obligations under this contract.
    """
    clauses = classify_clauses(content)
    
    assert len(clauses) == 3
    assert clauses[0]['label'] == 'party'
    assert clauses[1]['label'] == 'payment'
    assert clauses[2]['label'] == 'obligation'
