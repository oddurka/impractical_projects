import load_dictionary

def clean_dictionary():
    word_list = load_dictionary.load("words.txt")
    exception = ["a", "i"]

    clean_list = [word for word in word_list if len(word) != 1 or word in exception]

    return clean_list

print(clean_dictionary())
