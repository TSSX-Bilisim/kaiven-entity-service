from fastapi import APIRouter
from api.schema import NerEntity, AnalyzeRequest
from typing import Dict, List
from analyzer.engine import AnalyzerEngineFactory
from analyzer.post_processor import PostProcessor

router = APIRouter()

analyzerEngineFactory = AnalyzerEngineFactory()
analyzer = analyzerEngineFactory.create()
post_processor = PostProcessor(score_threshold=0.55)

@router.post("/extract", response_model=Dict[str, List[NerEntity]])
async def analyze_text(request: AnalyzeRequest):
    raw_results = analyzer.analyze(text=request.text, language='en')

    for entity in raw_results:
        print(f"{entity}")

    results = post_processor.resolve_overlaps(raw_results)

    return {
        "entities": [
            NerEntity(
                text=request.text[result.start:result.end],
                label=result.entity_type,
                start=result.start,
                end=result.end,
                score=result.score,
            )
            for result in results
        ]}

