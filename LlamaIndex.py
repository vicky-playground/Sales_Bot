"""
Before you can use LlamaIndex, you’ll need to access an LLM. By default, LlamaIndex uses GPT. You can get an OpenAI API key from their website. In the example code, I load my OpenAI API key from a .env file. However, you may directly input your key for your example locally if you’d like. Remove your key from the code before uploading it anywhere though!
"""
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import dotenv
import openai

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

documents = SimpleDirectoryReader(input_files=["./data/catalog.txt"]).load_data()
index = GPTVectorStoreIndex.from_documents(documents) # create the index 

query_engine = index.as_query_engine()
response=query_engine.query("What's the file about?")
print(response)

# Saving and Loading Your Index
##  Saving your index saves on GPT tokens and lowers your LLM cost. Saving your index is remarkably easy. Call .storage_context.persist() on your index
index.storage_context.persist() # This creates a folder called storage that contains three files: docstore.json, index_store.json, and vector_store.json. These files contain the documents, the index metadata, and the vector embeddings respectively. 

"""
The point of saving your index is so you can load it later. To load an index, we need two more imports from llama_index. We need StorageContext and load_index_from_storage. To rebuild the storage context, we pass the persistent storage directory to the StorageContext class. Once we’ve loaded the storage context, we call the load_index_from_storage function on it to reload the index.
"""