import sys
sys.path.append('../')

import converter
import timer
from linked_list import LinkedList

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


def histogram(list_of_words):
    linked_list = LinkedList()
    for word in list_of_words:
        try:
            searched_word = linked_list.search_word(word)
            tuple_val = (word, 0)
            linked_list.insert(tuple_val)
        except:
            if searched_word == word:
                new_count = 1  # supposed to add but not working
                linked_list.insert((word, new_count))
                linked_list.delete((word, 0))

if __name__ == "__main__":
    histogram(words_list)
