from presidio_analyzer.predefined_recognizers import GLiNERRecognizer
from config.gliner_config import GlinerConfig


def load_gliner_recognizer():
    config = GlinerConfig()

    recognizer = GLiNERRecognizer(
        model_name='urchade/gliner_multi_pii-v1',
        entity_mapping=config.entity_mapping,
        flat_ner=False,
        multi_label=True,
        map_location='cpu'
    )

    recognizer.supported_language='en'

    return recognizer
