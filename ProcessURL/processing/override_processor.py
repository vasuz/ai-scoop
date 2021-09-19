import json;

# from nltk.tokenize import word_tokenize

REPLACE_WORD_OVERRIDE = "ProcessURL/processing/replace_word_override.json"
REPLACE_LINE_OVERRIDE = None

def __process_word_override(text):
    split_text = text.split(" ")
    
    with open(REPLACE_WORD_OVERRIDE) as json_file:
        data = json.load(json_file)

        for i in range(0, len(split_text) - 1):
            word = split_text[i]
            if (str.lower(word) in data):
                if (word[0].isupper()):
                    split_text[i] = data[str.lower(word)].capitalize()
                else:
                    split_text[i] = data[str.lower(word)]

    return " ".join(split_text)


def __process_sentence_override(text):
    print("hi i stub!")


# The limitations of this code are numerous. Since we only tokenize by spaces, we suffer from issues for words
# followed by punctuation. For the sake of this hackathon, I'm not going to change that. However, this is something
# that should be documented for the sake of posterity

# A better approach would be to use nltk tokenization, but combining that together with spaces is a little tricky
# so I didn't do it
def process_override(text):
    processed_text = __process_word_override(text)
    return processed_text