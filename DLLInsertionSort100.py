# Program for insertion sort on doubly linked list 100 random numbers
# reference: https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/

import numpy as np
import random
import time

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
# reference: https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/
# Python implmentation of above algorithm

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# function to sort a singly linked list using insertion sort
def insertionSort(head_ref):
    # Initialize sorted linked list
    sorted = None

    # Traverse the given linked list and insert every
    # node to sorted
    current = head_ref
    while (current != None):
        # Store next for next iteration
        next = current.next

        # insert current in sorted linked list
        sorted = sortedInsert(sorted, current)

        # Update current
        current = next

    # Update head_ref to point to sorted linked list
    head_ref = sorted
    return head_ref


# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
def sortedInsert(head_ref, new_node):
    current = None

    # Special case for the head end */
    if (head_ref == None or (head_ref).data >= new_node.data):

        new_node.next = head_ref
        head_ref = new_node

    else:

        # Locate the node before the point of insertion
        current = head_ref
        while (current.next != None and
               current.next.data < new_node.data):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return head_ref


# BELOW FUNCTIONS ARE JUST UTILITY TO TEST sortedInsert

# Function to print linked list */
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next


# A utility function to insert a node
# at the beginning of linked list
def push(head_ref, new_data):
    # allocate node
    new_node = Node(0)

    # put in the data
    new_node.data = new_data

    # link the old list off the new node
    new_node.next = (head_ref)

    # move the head to point to the new node
    (head_ref) = new_node
    return head_ref

# This code is contributed by Arnab Kundu
# reference: https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/


print(startBlue +
      '------------------------ Insertion Sort 100 items Singly Linked List-------------------------' +
      endColor)
SLL = None

for item in range(100):
    # Placing 100 random numbers into the singly linked list and assigning a variable
    randomNum = np.array(random.sample(range(1, 101), 1))
    SLL = push(SLL, randomNum)
    print(SLL.data)

print("\nSingly linked list before sorting:\n")
print(SLL.data)

print("\nSingly linked list after sorting:\n")
start100 = time.time()
SLL = insertionSort(SLL)
end100 = time.time()
duration100 = end100 - start100
print(SLL.data)

print(startRed + "\nTime duration of Insertion Sort (Singly linked list), 100 random numbers, in seconds:\n" + endColor)
print(duration100)




