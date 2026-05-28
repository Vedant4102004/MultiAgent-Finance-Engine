import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

load_dotenv()

def load_llm():
   
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="conversational", 
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        max_new_tokens=300,
        temperature=0.3,
    )

    chat_model = ChatHuggingFace(llm=llm)
    return chat_model


if __name__ == "__main__":
    chat_engine = load_llm()

    messages = [
        HumanMessage(content="Why might Reliance Industries be a good investment?")
    ]

    response = chat_engine.invoke(messages)

    print(response.content)
