from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_bear_agent(llm):

    prompt = ChatPromptTemplate.from_template("""
You are a SELL-SIDE financial analyst.

Your job is to argue WHY this stock is a RISKY or BAD investment.

Use:
- Market data
- News context
- RAG research

Be critical, realistic, and risk-focused.

Query:
{query}

Market Data:
{market_data}

News:
{news}

RAG Insights:
{rag_context}

Now provide a strong BEARISH case:
""")

    return prompt | llm | StrOutputParser()