from presidio_analyzer.predefined_recognizers import GLiNERRecognizer


def load_gliner_recognizer():
    entity_mapping = {
        "person": "PERSON",
        "name": "PERSON",
        "organization": "ORGANIZATION",
        "location": "LOCATION"
    }

    recognizer = GLiNERRecognizer(
        model_name='urchade/gliner_multi_pii-v1',
        entity_mapping=entity_mapping,
        flat_ner=False,
        multi_label=True,
        map_location='cpu'
    )

    recognizer.supported_language='en'

    return recognizer
