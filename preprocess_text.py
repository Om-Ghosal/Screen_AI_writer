import re
from ai import text_preprocess,output_Cleaner

def add_newline(text):
    temp_text = text.lower().replace("newline ", "\n")
    return temp_text

def stopword_removal(text):
    stopwords = ["scratch that","no no no","remove that","cut that out"] 
    pattern = rf".*?\b(?:{'|'.join(map(re.escape, stopwords))})\b.*\n?"
    result = re.sub(pattern, "", text).strip()
    result = re.sub(r'\n+', '\n', result)

    return result




if __name__ == "__main__":
    text = """What is consciousness? No, wait scratch that. newline What do we really mean by being truly aware? Is it just neurons firing, or is there something deeper at play?newline Are we just biological machines processing inputs, or is there a spark of something more? thinking emote."""

    text = add_newline(text)
    text= stopword_removal(text)
    text = text_preprocess(text)

    print(output_Cleaner(text))