from presidio_analyzer import RecognizerRegistry
from recognizers.gliner_loader import load_gliner_recognizer

def build_registry(supported_languages: list[str]) -> RecognizerRegistry:
    registry = RecognizerRegistry()
    registry.supported_languages = supported_languages

    # GLiNER tanıyıcısı
    gliner_recognizer = load_gliner_recognizer()
    registry.add_recognizer(gliner_recognizer)

    return registry