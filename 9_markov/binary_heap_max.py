class Binary_Heap_Max():

    def __init__(self):
        self.list = [None]  # Add null object to make tree arithmetic simpler
        self.size = 0

    def peek(self, n):
        # look at first n nodes of heap
        return self.list[1:n+1]

    def insert(self, node):
        # push item onto heap
        self.list.append(node)
        self.size += 1
        self.perc_up(self.size)

    def delete_max(self):
        # remove the root and restructure heap
        key = self.list[1]
        self.list[1] = self.list.pop()
        self.size -= 1
        self.perc_down(1)
        return key

    def perc_down(self, index):
        while index * 2 <= self.size:
            key = self.list[index]
            max_child_index = self.max_child(index)
            max_child = self.list[max_child_index]
            if max_child > key:
                self.swap(index, max_child_index)
            index = max_child_index

    def perc_up(self, index):
        while index // 2 > 0:
            key = self.list[index]
            parent_index = index // 2
            parent_key = self.list[parent_index]
            if key > parent_key:
                self.swap(index, parent_index)
            index = parent_index

    def max_child(self, index):
        left_index = index * 2
        right_index = index * 2 + 1
        if right_index > self.size:
            return left_index
        if self.list[right_index] > self.list[left_index]:
            return right_index
        else:
            return left_index

    def swap(self, index_a, index_b):
        key = self.list[index_a]
        self.list[index_a] = self.list[index_b]
        self.list[index_b] = key

    def build_heap(self, a_list):
        index = len(a_list) // 2
        self.size = len(a_list)
        self.list = [0] + a_list[:]
        while (index > 0):
            self.perc_down(index)
            index = index - 1

if __name__ == "__main__":
    max_heap = Binary_Heap_Max()
    sample_list = [2, 9, 4, 5, 3]
    max_heap.build_heap(sample_list)
    # max_heap.insert(1)
    # max_heap.insert(7)
    # max_heap.insert(3)
    print(max_heap.delete_max())
    print(max_heap.delete_max())
    print(max_heap.delete_max())
