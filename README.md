```
python3.11 -m pip install python-dotenv
python3.11 -m pip install langchain    
python3.11 -m pip install llama_index
python3.11 -m pip install gradio
python3.11 -m pip install hugchat
python3.11 -m pip install sentence_transformers
```

Set your ‘OPENAI_API_KEY’ Environment Variable using bash. Run the following command in your terminal, replacing yourkey with your API key. 
```
echo "export OPENAI_API_KEY='yourkey'" >> ~/.bash_profile
```

You’re all set! You can now reference the key in curl or load it in your Python:

```
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]
```
