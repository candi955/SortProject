# Program for insertion sort on doubly linked list 10,000 random numbers
# reference: https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/

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

# Node of a doubly linked list
# reference: https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# function to create and return a new node
# of a doubly linked list
def getNode(data):
    # allocate node
    newNode = Node(0)

    # put in the data
    newNode.data = data
    newNode.prev = newNode.next = None
    return newNode


# function to insert a new node in sorted way in
# a sorted doubly linked list
def sortedInsert(head_ref, newNode):
    current = None

    # if list is empty
    if (head_ref == None):
        head_ref = newNode

    # if the node is to be inserted at the beginning
    # of the doubly linked list
    elif ((head_ref).data >= newNode.data):
        newNode.next = head_ref
        newNode.next.prev = newNode
        head_ref = newNode

    else:
        current = head_ref

        # locate the node after which the new node
        # is to be inserted
        while (current.next != None and
               current.next.data < newNode.data):
            current = current.next

        """Make the appropriate links """
        newNode.next = current.next

        # if the new node is not inserted
        # at the end of the list
        if (current.next != None):
            newNode.next.prev = newNode

        current.next = newNode
        newNode.prev = current

    return head_ref;


# function to sort a doubly linked list
# using insertion sort
def insertionSort(head_ref):
    # Initialize 'sorted' - a sorted
    # doubly linked list
    sorted = None

    # Traverse the given doubly linked list
    # and insert every node to 'sorted'
    current = head_ref
    while (current != None):
        # Store next for next iteration
        next = current.next

        # removing all the links so as to create
        # 'current' as a new node for insertion
        current.prev = current.next = None

        # insert current in 'sorted' doubly linked list
        sorted = sortedInsert(sorted, current)

        # Update current
        current = next

    # Update head_ref to point to
    # sorted doubly linked list
    head_ref = sorted

    return head_ref

# function to print the doubly linked list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


# function to insert a node at the
# beginning of the doubly linked list
def push(head_ref, new_data):
    """ allocate node """
    new_node = Node(0)

    """ put in the data """
    new_node.data = new_data

    """ Make next of new node as head 
    and previous as None """
    new_node.next = (head_ref)
    new_node.prev = None

    """ change prev of head node to new node """
    if ((head_ref) != None):
        (head_ref).prev = new_node

    """ move the head to point to the new node """
    (head_ref) = new_node
    return head_ref
# reference: https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/#
# This code is contributed by Arnab Kundu
# Driver Code

print(startBlue +
      '------------------------------------------- Insertion Sort 10,000 items -------------------------------------------' +
      endColor)
if __name__ == "__main__":
    """ start with the empty doubly linked list """

    head = None
    # reference: https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/
    # This code is contributed by Arnab Kundu

    for item in range(10000):
        randomNum = np.array(random.sample(range(1, 10001), 1))
        head = push(head, randomNum)

    print("Doubly Linked List Before Sorting")
    printList(head)

    start10000 = time.time()
    head = insertionSort(head)
    end10000 = time.time()
    duration10000 = end10000 - start10000

    print("\nDoubly Linked List After Sorting")
    printList(head)

    print(startRed + "\n\nTime duration of Insertion Sort, 10,000 random numbers, in seconds:\n" + endColor)
    print(duration10000)


