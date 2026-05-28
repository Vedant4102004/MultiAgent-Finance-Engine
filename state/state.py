from typing import TypedDict

class FinanceState(TypedDict):
    query: str
    market_data: dict
    news: list
    rag_context: str

    bull_case: str
    bear_case: str
    risk_case: str
    final_decision: str