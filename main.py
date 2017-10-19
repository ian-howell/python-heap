#!/usr/bin/python3
#
# Created by Ian Howell on 10/19/17.
# File name: main.py
from random import randrange
import heap


def main():
    min_heap = heap.Heap()

    for i in range(10):
        min_heap.put(randrange(1, 100))
    print(min_heap)

    first_item = min_heap.get()

    print('Got {0} from the heap'.format(first_item))
    print(min_heap)


if __name__ == "__main__":
    main()
