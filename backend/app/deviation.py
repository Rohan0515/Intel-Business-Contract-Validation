def detect_deviations(parsed_content, template_structure):
    deviations = []
    for clause in parsed_content:
        label = clause['label']
        if label in template_structure and clause['text'].lower() not in template_structure[label]:
            deviations.append(clause)
    return deviations
