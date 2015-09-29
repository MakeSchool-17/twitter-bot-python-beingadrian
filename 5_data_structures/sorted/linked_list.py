from node import Node


class LinkedList(object):

    def __init__(self, head=None):
        # Head is a Node()
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current

    def search_word(self, word):
        current = self.head
        current_word = ""
        found = False
        while current and found is False:
            current_word = current.get_data()[0]
            if current_word == word:
                found = True
            else:
                current = current.get_next()
                if current is None:
                    return ""
        return current_word

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current.get_next()
        if current is None:
            raise ValueError("Data is not in the list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
