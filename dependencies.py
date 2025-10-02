from fastapi import Depends
from analyzer.engine import get_analyzer_engine

def analyzer_engine_dependency():
    return get_analyzer_engine()
