import os
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

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

#Storing the Conversation History in a List
conversation_history = []


PROMPT_QUESTION = """
Your name is IBM Help Assistant. You work for IBM. You are dedicated to every client's success.
You are an expert in IBM products and helping a client to find the product they need.
Your conversation with the human is recorded in the chat history below.

History:
"{history}"

Now continue the conversation with the human. If you do not know the answer, say "I don't know" in a polite way.
Human: {input}
Assistant:"""

def chatbot(input_text):
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)

    history_string = "\n".join(conversation_history)

    print(f"history_string: {history_string}")

    output = index.as_query_engine().query(PROMPT_QUESTION.format(history=history_string, input=input_text))
    print(f"output: {output}")
    print(f"conversation_history: {conversation_history}")

    conversation_history.append(input_text)
    conversation_history.append(output.response)

    return output.response

iface = gr.Interface(fn=chatbot,
                      inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                      outputs="text",
                      title="IBM Help Bot")

iface.launch(share=True)



