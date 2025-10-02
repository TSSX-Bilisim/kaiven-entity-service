from presidio_analyzer import AnalyzerEngine
from .registry import build_registry

class AnalyzerEngineFactory:
    def __init__(self, supported_languages=None):
        self.supported_languages = ['en']
        self.registry = build_registry(self.supported_languages)

    def create(self) -> AnalyzerEngine:
        return AnalyzerEngine(
            registry=self.registry,
            supported_languages=self.supported_languages,
        )