```
python3.11 -m pip install langchain    
python3.11 -m pip install llama_index
python3.11 -m pip install gradio
```
# Use Environment Variables in place of your API key
Set your ‘OPENAI_API_KEY’ Environment Variable using bash. Run the following command in your terminal, replacing yourkey with your API key. 
```
export OPENAI_API_KEY='yourkey'
```

You’re all set! You can now reference the key in curl or load it in your Python:

```
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]
```
