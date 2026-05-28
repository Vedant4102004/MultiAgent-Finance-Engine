from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_risk_agent(llm):

    prompt = ChatPromptTemplate.from_template("""
You are a RISK ANALYST for financial markets.

Your job is to identify EXTERNAL RISKS such as:
- macroeconomic risks
- regulatory risks
- geopolitical risks
- industry risks

Do NOT repeat bull or bear arguments.

Focus only on risk factors.

Query:
{query}

Market Data:
{market_data}

News:
{news}

RAG Insights:
{rag_context}

Now provide a structured RISK analysis:
""")

    return prompt | llm | StrOutputParser()