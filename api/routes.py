from fastapi import APIRouter
from api.schema import NerEntity, AnalyzeRequest
from typing import List
from analyzer.engine import AnalyzerEngineFactory

router = APIRouter()

analyzerEngineFactory = AnalyzerEngineFactory()
analyzer = analyzerEngineFactory.create()

@router.post("/analyze", response_model=List[NerEntity])
async def analyze_text(request: AnalyzeRequest):
    results = analyzer.analyze(text=request.text, language=request.language)

    return [
        NerEntity(
            text=request.text[result.start:result.end],
            label=result.entity_type,
            start=result.start,
            end=result.end,
            score=result.score,
        )
        for result in results
    ]


