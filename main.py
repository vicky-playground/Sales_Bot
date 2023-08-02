import dotenv
from langchain.schema import messages_from_dict, messages_to_dict, AIMessage
from langchain.memory import ConversationBufferMemory, ChatMessageHistory
from langchain import ConversationChain, LLMChain
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from llama_index import LLMPredictor, PromptHelper, SimpleDirectoryReader, StorageContext, load_index_from_storage
import gradio as gr
import openai
from langchain.agents import initialize_agent

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

#HUGGINGFACEHUB_API_TOKEN = config['HUGGINGFACEHUB_API_TOKEN']


def chatbot(input_text):
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)

    
    return response.response

iface = gr.Interface(fn=chatbot,
                      inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                      outputs="text",
                      title="IBM Help Bot")

iface.launch(share=True)
