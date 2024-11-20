from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def handle_conversation():
  model = OllamaLLM(model="llama3")
  context = ""
  template = """
  Answer the question below.

  Here is the conversation history: {context}

  Question: {question}

  Answer:
  """

  prompt = ChatPromptTemplate.from_template(template)

  chain = prompt | model
  print("Welcome to the AI chatbot. Type exit to quit")
  while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
      break
    result = chain.invoke({"context": context, "question": user_input})
    print("Bot: ", result)
    context += f"\nUser:{user_input}\n AI: {result}"


handle_conversation()

