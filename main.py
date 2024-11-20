from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")

# result = model.invoke(input="hello world")

# print(result)

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

result = chain.invoke({"context": "", "question": "how are you?"})

print(result)
