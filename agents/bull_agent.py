from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_bull_agent(llm):
    prompt = ChatPromptTemplate.from_template("""
You are a BUY-SIDE financial analyst.

Your job is to argue WHY this stock is a GOOD investment.

Use:
- Market data
- News context
- RAG research

Be logical, data-driven, and optimistic but realistic.

Query:
{query}

Market Data:
{market_data}

News:
{news}

RAG Insights:
{rag_context}

Now provide a strong BULLISH case:
""")
    
    return prompt | llm | StrOutputParser()