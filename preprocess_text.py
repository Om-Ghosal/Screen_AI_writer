import re

def add_newline(text):
    temp_text = text.lower().replace("newline ", "\n")
    return temp_text

def stopword_removal(text):
    stopwords = ["the", "is", "example"] 
    pattern = rf".*?\b(?:{'|'.join(map(re.escape, stopwords))})\b.*\n?"
    result = re.sub(pattern, "", text).strip()
    result = re.sub(r'\n+', '\n', result)

    return result




if __name__ == "__main__":
    text = """hello world.newline This is a test sentence.newline Another line before example stopword.newline Keep this line intact."""

    text = add_newline(text)
    print(stopword_removal(text))