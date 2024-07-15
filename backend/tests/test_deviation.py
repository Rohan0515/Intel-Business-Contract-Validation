from app.deviation import detect_deviations

def test_detect_deviations():
    parsed_content = [
        {'text': 'This agreement is made between the first party and the second party.', 'label': 'party'},
        {'text': 'The payment will be made in installments.', 'label': 'payment'},
        {'text': 'Each party has certain obligations under this contract.', 'label': 'obligation'}
    ]
    
    template = {
        "party": ["party"],
        "agreement": ["agreement"],
        "assignment": ["assignment"],
        "payment": ["payment"],
        "obligation": ["obligation"]
    }
    
    deviations = detect_deviations(parsed_content, template)
    assert len(deviations) == 0  

    parsed_content.append({'text': 'Unauthorized clause', 'label': 'other'})
    deviations = detect_deviations(parsed_content, template)
    assert len(deviations) == 1
    assert deviations[0]['text'] == 'Unauthorized clause'
