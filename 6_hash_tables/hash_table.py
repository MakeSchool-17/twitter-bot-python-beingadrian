
class Node(object):

        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def set_next(self, new_next):
            self.next_node = new_next


class LinkedList(object):

        def __init__(self, head=None):
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

        def search_by_key(self, key):
            current = self.head
            found = False
            while current and found is False:
                current_data = current.get_data()
                if current_data[0] == key:
                    found = True
                else:
                    current.get_next()
            return current

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
                return None
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

        def delete_by_key(self, key):
            current = self.head
            previous = None
            found = False
            while current and found is False:
                if current.get_data()[0] == key:
                    found = True
                else:
                    previous = current
                    current.get_next()
            if current is None:
                return None
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


class HashTable(object):

    # buckets
    buckets_structure = [
        LinkedList(),
        LinkedList(),
        LinkedList(),
        LinkedList(),
        LinkedList(),
        LinkedList(),
        LinkedList(),
        LinkedList()
    ]

    def __init__(self, buckets_array=buckets_structure):
        self.buckets_array = buckets_array

    def search(self, key):
        bucket_index = hash(key) % 8
        try:
            # if search is successful and key exists
            bucket = self.buckets_array[bucket_index]
            searched_data = bucket.search_by_key(key).get_data()
            return searched_data
        except:
            # if key doesn't exist
            return None

    def set_value(self, key, val):
        # find hash of key
        bucket_index = hash(key) % 8
        try:
            # if key exists, replace key
            self.buckets_array[bucket_index].delete(key)
            self.buckets_array[bucket_index].insert((key, val))
        except:
            # if key doesn't exist, create key
            self.buckets_array[bucket_index].insert((key, val))

    def items(self):
        items = []
        for linked_list in self.buckets_array:
            current = linked_list.head
            try:
                while current or current.get_next() is not None:
                    items.append(current.get_data())
                    current = current.get_next()
            except:
                pass
        return items

    def keys(self):
        keys = []
        items = self.items()
        for item in items:
            keys.append(item[0])
        return keys

    def values(self):
        values = []
        items = self.items()
        for item in items:
            values.append(item[1])
        return values

if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.set_value("test", 0)
    hash_table.set_value("love", 1)
    search = hash_table.search("test")
    print(search)
    keys = hash_table.keys()
    print(keys)
    values = hash_table.values()
    print(values)
