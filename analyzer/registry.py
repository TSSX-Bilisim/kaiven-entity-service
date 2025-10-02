from presidio_analyzer import RecognizerRegistry
from recognizers.gliner_loader import load_gliner_recognizer


def build_registry():
    registry = RecognizerRegistry()

    # GLiNER tanıyıcısı
    gliner_recognizer = load_gliner_recognizer()
    registry.add_recognizer(gliner_recognizer)

    return registry