from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_ollama.llms import OllamaLLM
import re

prompt_template = PromptTemplate.from_template('''Create an AI system that takes raw user input (e.g., dictated notes or thoughts) and processes it to produce clean, concise, and well-structured text. The system should handle corrections, remove filler words or phrases (e.g., 'no scratch that'), and incorporate relevant emojis or formatting to reflect the tone or intent of the user. For example:

Input:
'What is LangChain? no scratch that, what do you mean by Langchain? Is it a way for humanity to tap into the power of AI? thinking emote'

Processed Output:
'What do you mean by LangChain? Is it a way for humanity to tap into the power of AI? 🤔'

The system should focus on natural language understanding, context retention, and user intent to deliver polished and meaningful output.'

Now, process the following input text: {user}.''')

model = OllamaLLM(model="deepseek-r1:8b")

chain = prompt_template | model

def output_Cleaner(text):
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()

def text_preprocess(text):
    return output_Cleaner(chain.invoke({"user": text}))