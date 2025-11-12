import os
import json
import time
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError('API não encontrada')

modelo = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

with open("Chatbot/config.json", 'r', encoding='utf-8') as f:
    config = json.load(f)

parser = StrOutputParser()
chain = modelo | parser

workflow = StateGraph(state_schema=MessagesState)

def call_mode(state: MessagesState):
    response = modelo.invoke(state['messages'])
    return {'messages': response}

workflow.add_edge(START, "modelo")
workflow.add_node("modelo", call_mode)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

def efeito_digitando(texto, atraso=0.02):
    """Imita o efeito de digitação no console."""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(atraso)
    print()

print('Chat iniciado, digite (SAIR) para encerrar.')

while True:
    user_input = input('Você: ')
    if user_input.lower() == 'sair':
        print('Encerrando chatbot...')
        break

    input_messages = [HumanMessage(content=user_input)]
    output = app.invoke({"messages": input_messages}, config=config)
    resposta = output["messages"][-1]

    print("Bot: ", end='', flush=True)
    efeito_digitando(resposta.content)
