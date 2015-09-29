import sys
sys.path.append('../')

import converter
from linked_list import LinkedList

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


def histogram(list_of_words):
    linked_list = LinkedList()
    for word in list_of_words:
        searched_word = linked_list.search_word(word)
        print(searched_word)
        if searched_word == "":
            tuple_val = (word, 0)
            linked_list.insert(tuple_val)
        else:
            pass
            # searched_word[1] += 1

s
if __name__ == "__main__":
    histogram(words_list)
