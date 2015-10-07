import sys
from hash_table import HashTable


def tokenize(text_file_dir):
    text_file = open(text_file_dir, 'r')
    text = text_file.read()
    text_file.close()
    tokenized_array = text.split(" ")
    return tokenized_array


def count_tokens(tokenized_array):
    histogram = HashTable()
    for word in tokenized_array:
        searched_word_data = histogram.search(word)
        if searched_word_data is not None:
            histogram.set_value(word, searched_word_data[1] + 1)
        else:
            histogram.set_value(word, 1)
    return histogram

if __name__ == "__main__":
    user_input = sys.argv[1]
    tokenized_array = tokenize(user_input)
    histogram = count_tokens(tokenized_array)
    print(histogram.items())
