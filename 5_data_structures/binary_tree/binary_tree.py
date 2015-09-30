import sys
sys.path.append('../')

import converter
from linked_list import LinkedList

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


class Node(object):

    __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):

    __init__(self, head=None):
        self.head = head

    def add(self):
    node = Node()
        self.head = node


    def search(self):
        ...

    def remove(self):
        ...

    def get_values(self):
        ...


def histogram(words_list):
    ...


if __name__ == "__main__":
    ...
