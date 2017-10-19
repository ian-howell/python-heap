#!/usr/bin/python


class Heap(object):
    def __init__(self):
        self.heap = []
        self.__size = 0

    def get(self):
        ret_val = None
        if self.__size > 0:
            self.__size -= 1
            ret_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify(0)
        return ret_val

    def put(self, x):
        self.__size += 1
        self.heap.append(x)

        i = self.__size - 1
        parent = (i - 1) // 2
        while (i > 0 and self.heap[i] < self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = (i - 1) // 2
            parent = (i - 1) // 2

    def size(self):
        return self.__size

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.__size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.__size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = \
                          self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def __repr__(self):
        return '<Heap object>'

    def __str__(self):
        ret_val = 'Size = {0}\n'.format(self.__size)
        ret_val += 'Contents: [ '
        for x in self.heap:
            ret_val += str(x) + ' '
        ret_val += ']'
        return ret_val
