from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Presidio NLP Server",
    description="GLiNER + PatternRecognizer destekli KVKK/GDPR uyumlu sunucu",
    version="1.0.0",
)

app.include_router(router, prefix='/ner')