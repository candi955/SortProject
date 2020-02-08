# Code won't complete run: receive the error:
# RecursionError: maximum recursion depth exceeded while calling a Python object
# I knew this could be an issue due to the memory it takes to run merge
# reference: https://stackoverflow.com/questions/23578541/python-recursion-test-in-pycharm-process-finished-with-exit-code-139

# -------------------------------------------------------------------------------------------------------------------
# Program for merge sort on doubly linked list 10,000 random numbers
# reference: https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/

import numpy as np
import random
import time
import sys
sys.setrecursionlimit(100000)

# Using the color class in python, in assigned variable form, to make the headings bold, underline, and various colors
# reference: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
endColor = "\033[0m"

startBold = "\033[1m"
startUnderline = '\033[4m'
startDarkCyan = '\033[36m'
startPurple = '\033[95m'
startCyan = '\033[96m'
startBlue = '\033[94m'
startGreen = '\033[92m'
startYellow = '\033[93m'
startRed = '\033[91m'

# A node of the doubly linked list
# reference: https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Function to merge two linked list
    def merge(self, first, second):

        # If first linked list is empty
        if first is None:
            return second

            # If second linked list is empty
        if second is None:
            return first

            # Pick the smaller value
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

            # Function to do merge sort

    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead

        second = self.split(tempHead)

        # Recur for left and righ halves
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        # Merge the two sorted halves
        return self.merge(tempHead, second)

        # Split the doubly linked list (DLL) into two DLLs

    # of half sizes
    def split(self, tempHead):
        fast = slow = tempHead
        while (True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

        # Given a reference to the head of a list and an

    # integer,inserts a new node on the front of list
    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

            # 5. move the head to point to the new node
        self.head = new_node

    def printList(self, node):
        temp = node
        print("Forward Traversal using next pointer")
        while (node is not None):
            print(node.data)
            temp = node
            node = node.next
        # This program will also print in reverse, but I didn't need it for timing duration so hashed it out
        #print("\nBackward Traversal using prev pointer")
        #while (temp):
            #print(temp.data)
            #temp = temp.prev

# reference: https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/

print(startBlue +
      '------------------------------------------ Merge Sort 10,000 items ------------------------------------------' +
      endColor)

dll3 = DoublyLinkedList()

for item in range(10000):
    randomNum10_000 = np.array(random.sample(range(1, 10001), 1))
    dll3.push(randomNum10_000)

start10_000 = time.time()
dll3.head = dll3.mergeSort(dll3.head)
end10_000 = time.time()
duration10_000 = end10_000 - start10_000
print(startRed + "Duration in seconds: " + endColor)
print(duration10_000)

print("Linked List after sorting")
dll3.printList(dll3.head)

# Code won't complete run: receive the error:
# # RecursionError: maximum recursion depth exceeded while calling a Python object
# # I knew this could be an issue due to the memory it takes to run merge
# # reference: https://stackoverflow.com/questions/23578541/python-recursion-test-in-pycharm-process-finished-with-exit-code-139