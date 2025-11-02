from pydantic import BaseModel
from typing import Optional

class AnalyzeRequest(BaseModel):
    text: str
    labelsToFind: Optional[list[str]] = None

class NerEntity(BaseModel):
    text: str
    label: str
    start: Optional[int] = None
    end: Optional[int] = None
    score: Optional[float] = None