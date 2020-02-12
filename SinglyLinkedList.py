import numpy as np
import random
import time
from sorting_techniques import pysort

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

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

        # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

        # print method for the linked list


    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

    def _changeBack_(self):

        if self.head:
            current = self.head
            if current is None:
                current.remove()
                while (current.next):
                    current = current.next
                    if current.next is None:
                        current.next.remove()
                        return
                    else:
                        print('hello')
            elif current is not None:
                while (current.next):
                    current = current.next
                    if current.next is not None:
                        return
                    else:
                        print('hello')
            else:
                print('whaat')
        else:
            print('who')




# --------------------------------------------------------------------

# Creating a single node
first = Node(3)
print(first.data)

# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()

# reference: https://stackoverflow.com/questions/40749869/linked-list-sorting-error
def bubbleSortLinkedList(LL):
    pointer = LL
    swapped = True
    while swapped:
        pointer = LL['next']
        swapped = False
        for i in range(4):
            if pointer['data'] > pointer['next']['data']:
                pointer['data'], pointer['next']['data'] = pointer['next']['data'], pointer['data']
                swapped = True
            pointer = pointer['next']

        pointer = LL  # This line was wrong!!!!!

    return LL


sortObj = pysort.Sorting()
merging = sortObj.bubbleSort(LL)
print('\nUsing the Pysort package to ' + startPurple + startBold + 'Quick Sort 100 numbers ' +
      endColor + ':\n\n', merging)

