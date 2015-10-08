class Binary_Heap(object):

    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def perc_up(self, index):
        # keep going up until reaching the root node
        while (index // 2 > 0):
            # decide whether to go up or not
            if self.heap_list[index] < self.heap_list[index // 2]:
                parent = self.heap_list[index // 2]
                # replace parent node with child node
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = parent
            index = index // 2

    def insert(self, data):
        self.heap_list.append(data)
        self.current_size = self.current_size + 1
        # to follow the rule
        self.perc_up(self.current_size)

    def perc_down(self, index):
        # keep going down the tree
        while (index * 2) <= self.current_size:
            # get smaller child
            child = self.min_child(index)
            if self.heap_list[index] > self.heap_list[child]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[child]
                self.heap_list[child] = temp
            index = child

    def min_child(self, index):
        # get the smaller child node
        if (index * 2 + 1) > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def del_min(self):
        return_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return return_val

    def del_max(self):
        ...

    def build_heap(self, a_list):
        index = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (index > 0):
            self.perc_down(index)
            index = index - 1


if __name__ == "__main__":
    binary_heap = Binary_Heap()
    sample_list = [1, 9, 4, 5, 3]
    tuple_list = [(1, "d"), (9, "s"), (4, "a"), (5, "l")]
    binary_heap.build_heap(tuple_list)
    print(binary_heap.del_min())
    print(binary_heap.del_min())
    print(binary_heap.del_min())
    print(binary_heap.del_min())
