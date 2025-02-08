from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_ollama.llms import OllamaLLM
import re
prompt_template = ChatPromptTemplate([
    ('system','''Just fix any Gramtical errors, any spelling errors and add emotes where ever user asked for it.
'''),
    ('user',"{user}")
])

model = OllamaLLM(model="mistral")

chain = prompt_template | model

def output_Cleaner(text):
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()

def text_preprocess(text):
    return output_Cleaner(chain.invoke({"user": text}))