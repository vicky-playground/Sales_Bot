import openai
openai.api_key = 'OPENAI_API_KEY'

from llama_index import StorageContext, load_index_from_storage

# Store the conversation history in a List
conversation_history = []

def ask_bot(input_text):

    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)

    PROMPT_QUESTION = """
    
        Your name is IBM Help Assistant. You work for IBM. You are dedicated to every client's success.
        You are an expert in IBM products and helping a client to find the product they need.
        Your conversation with the human is recorded in the chat history below.

        History:
        "{history}"

        Now continue the conversation with the human. If you do not know the answer based on the chat history and the new input from the client, politely admit it and therefore you need more information.
        Human: {input}
        Assistant:"""

    # update conversation history
    global conversation_history
    history_string = "\n".join(conversation_history)
    print(f"history_string: {history_string}")
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    output = index.as_query_engine().query(PROMPT_QUESTION.format(history=history_string, input=input_text))
    print(f"output: {output}")
    
    # update conversation history with user input and AI's response
    conversation_history.append(input_text)
    conversation_history.append(output.response)
    

    return output.response

import gradio as gr 

with gr.Blocks() as demo:
    gr.Markdown('# IBM Help Assistant')
    gr.Markdown('## Your assistant to guide you to the right product.')
    gr.Markdown('### Sample messages:')
    gr.Markdown('#### :) I want to deploy an app for free')
    gr.Markdown('#### :) any advice on analytics?')
    gr.Markdown('#### :) who are you?')
    gr.Markdown('#### :) what products do you have?')
    gr.Markdown('#### :) what\'s my first request?')
    gr.Markdown('#### many more......')
    
    # create an input textbox and a submit button
    inputs=gr.inputs.Textbox(lines=4, label="Input Box", placeholder="Enter your text here")
    submit_btn = gr.Button("Submit") 
    # define the behavior of the submit button using the ask_bot function
    submit_btn.click(fn=ask_bot, inputs=[inputs], outputs=gr.Textbox(lines=4, label="Output Box") )

# launch the Gradio interface
demo.launch()
