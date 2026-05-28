from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_judge_agent(llm):

    prompt = ChatPromptTemplate.from_template("""
You are the HEAD INVESTMENT COMMITTEE MEMBER.

You will evaluate:

Bull Case:
{bull_case}

Bear Case:
{bear_case}

Risk Analysis:
{risk_case}

Your job:
1. Compare arguments
2. Weigh risk vs reward
3. Give final verdict

Return format:

Recommendation: (BUY / HOLD / SELL)
Confidence: (0-100%)
Reason:
- short explanation
""")

    return prompt | llm | StrOutputParser()