#!/usr/bin/python3
#
# Created by Ian Howell on 10/19/17.
# File name: main.py
from random import randrange
import heap


def main():
    test_heap_creation()
    test_heap_sort()


def test_heap_creation():
    min_heap = heap.Heap()

    for i in range(10):
        min_heap.put(randrange(1, 100))
    print(min_heap)

    first_item = min_heap.get()

    print('Got {0} from the heap'.format(first_item))
    print(min_heap)


def test_heap_sort():
    ARR_SIZE = 20
    random_arr = [None] * ARR_SIZE
    for i in range(ARR_SIZE):
        random_arr[i] = randrange(1, 100)

    print("Array before heap sort: {}".format(random_arr))
    heap.heap_sort(random_arr)
    print("Array after heap sort: {}".format(random_arr))


if __name__ == "__main__":
    main()
