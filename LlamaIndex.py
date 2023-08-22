from llama_index import SimpleDirectoryReader
# load the document
documents = SimpleDirectoryReader(input_files=["catalog.txt"]).load_data()

from llama_index import GPTVectorStoreIndex
import openai

# use `OpenAI` to create the embedding for each node and store it in a Vector Store.
openai.api_key = 'OPENAI_API_KEY'

# build index
index = GPTVectorStoreIndex.from_documents(documents)

index.storage_context.persist() 
