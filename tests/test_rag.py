from rag.build_rag import initialize_rag


rag = initialize_rag()

query = "What are the growth opportunities for Reliance Industries?"

result = rag(query)

print("\nRAG OUTPUT:\n")
print(result)