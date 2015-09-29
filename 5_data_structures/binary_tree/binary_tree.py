import sys
sys.path.append('../')

import converter
from linked_list import LinkedList

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


class Node(object):

    __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree(object):

    __init__(self):
        print()

    def add(self):
        print()

    def search(self):
        print()

    def remove(self):
        print()

    def get_values(self):
        print()


def histogram(words_list):
    print()


if __name__ == "__main__":
    print()
