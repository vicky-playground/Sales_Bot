import os
from langchain import LLMChain
from llama_index import StorageContext, load_index_from_storage
import gradio as gr
import openai

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

#Storing the conversation history in a List
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

def ask_bot(input_text):
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

with gr.Blocks() as demo:
    gr.Markdown('# IBM Help Assistant')
    gr.Markdown('## Your assistant to guide you to the right product.')
    gr.Markdown('### Sample messages:')
    gr.Markdown('#### :) I want to deploy an app for free')
    gr.Markdown('#### :) any advice on analytics?')
    gr.Markdown('#### :) what products do you have?')
    gr.Markdown('#### :) I want to contact a real person')
    gr.Markdown('#### many more......')

    inputs=gr.inputs.Textbox(lines=4, label="Input Box", placeholder="Enter your text here")
    submit_btn = gr.Button("Submit") 
    submit_btn.click(fn=ask_bot, outputs=gr.Textbox(lines=4, label="Output Box") )

demo.launch()
