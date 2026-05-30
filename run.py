from models.load_models import load_llm
from agents.bull_agent import create_bull_agent
from agents.bear_agent import create_bear_agent
from agents.risk_agent import create_risk_agent
from agents.judge_agent import create_judge_agent

from langchain_core.runnables import RunnableParallel

llm = load_llm()

bull = create_bull_agent(llm)
bear = create_bear_agent(llm)
risk = create_risk_agent(llm)
judge = create_judge_agent(llm)

parallel = RunnableParallel(
    bull_case=bull,
    bear_case=bear,
    risk_case=risk
)

def run(query):

    results = parallel.invoke({
        "query": query,
        "market_data": {},
        "news": [],
        "rag_context": ""
    })

    final = judge.invoke({
        "bull_case": results["bull_case"],
        "bear_case": results["bear_case"],
        "risk_case": results["risk_case"]
    })

    return final
if __name__ == "__main__":
    print(run("Should I invest in Reliance?"))
