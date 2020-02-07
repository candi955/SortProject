# For the course MS549 Data Structures and Testing, this is Phases 1-5, implementing Merge Sort, Quick Sort
# and Timsort on doubly linked list sets of one-hundred, one-thousand, ten-thousand, and one hundred-thousand
# random numbers.

# References I'm starting with:
# https://stackoverflow.com/questions/18761766/mergesort-with-python
# https://www.programiz.com/python-programming/methods/list/sort
# https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
# https://pypi.org/project/pysort/
# https://www.npmjs.com/package/timsort


import random
import time
import numpy as np
from sorting_techniques import pysort
# in order to utilize the installed timsort, uploaded the 'require' package to use in the code
import require
# Appears bower deprecated for timsort install, had started with bower; switching to npm install
# references: https://www.jetbrains.com/help/pycharm/using-bower-package-manager.html
# https://libraries.io/bower/timsort
# In Pycharm IDE terminal:
# pip install npm
# npm install --save timsort
# npm install timsort

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

# Starting by creating the doubly linked list classes and functions (the Node() and DoublyLinkedList() classes from
# previous projects
# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
Node(data=None)

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    # inserting data into an empty list (Insert at end of list)
    def insert_in_emptylist(self, data):
            if self.start_node is None:
                new_node = Node(data)
                self.start_node = new_node
            else:
                print("list is not empty")


    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n


    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;

     # deleting elements at the end of the list
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    # deleting elements by value
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    # Reversing a doubly linked list
    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

    # Attempting to create a function for 'find'
    def find_element_by_value(self, x):

        # for checking first node and finding the beginning number
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                print('Item found.')

            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            print("The number", x, "is the first number located on the list.")
            self.start_node = self.start_node
            self.start_node.pref = None
            return
        # for finding the middle numbers
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                print("The number", x, "is one of the numbers located in the middle of the list.")
                break
            n = n.nref

        # for finding the end number
        if n.nref is not None:
            #n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                print("The number", x, "is the last number on the list.")
            else:
                print("Element not found")

    def delete_AllElementsOfList(self, object):

        for i in object:
            if i + 1:
                while True:
                    try:


                        if self.start_node is None:
                            print("The list has no element to delete")
                            return
                        if self.start_node.nref is None:
                            self.start_node = None
                            return
                        self.start_node = self.start_node.nref
                        self.start_prev = None;

                    except ValueError:
                        print('There has been an error')
                    else:
                        break

DoublyLinkedList()


# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

class Main():

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced
    new_linked_list = DoublyLinkedList()

    # 100 random numbers
    array100 = np.array(random.sample(range(1, 101), 100))
    print(startBlue + 'Entering 100 numbers into the doubly linked list:\n' + endColor, array100, '\n')

    # 1,000 random numbers
    array1_000 = np.array(random.sample(range(1, 1001), 1000))
    print(startBlue + 'Entering 1,000 numbers into the doubly linked list:\n' + endColor, array1_000, '\n')
    copiedArray1_000 = array1_000.copy()

    # 10,000 random numbers
    array10_000 = np.array(random.sample(range(1, 10001), 10000))
    print(startBlue + 'Entering 10,000 numbers into the doubly linked list:\n' + endColor, array10_000, '\n')
    copiedArray10_000 = array10_000.copy()

    # 100,000 random numbers
    array100_000 = np.array(random.sample(range(1, 100001), 100000))
    print(startBlue + 'Entering 100,000 numbers into the doubly linked list:\n' + endColor, array100_000, '\n')
    copiedArray100_000 = array100_000.copy()

    # In order to begin sorting the various random numbers using the Pysort library, a variable
    # is being created
    # reference: https://pypi.org/project/pysort/

    sortObj = pysort.Sorting()

    #-------------------------------------------------------------------------------------------------------------
    # Sorting and timing sort duration of 100 random numbers
    print(startGreen + '------------------------------------------------------------' +
          startBold + ' Sorting and timing sort duration of 100 random numbers ' +
          '------------------------------------------------------------' + endColor)

    print('\nOriginal dataset:\n', array100)

    # Creating a copy (variable newarray100) of the original array list, with the python list() constructor, so that
    # the array of random numbers does not create a whole new list
    # references: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
    # https://www.programiz.com/python-programming/methods/built-in/list
    newArray100 = list(array100)
    print('\nCreated a copy of the original dataset using list() called newarray100,\n so that the ' +
          'dataset of random numbers cannot be changed upon repeat:\n\n', newArray100)

    # Sorting the new array with Pysort package Merge Sort
    # reference: https://pypi.org/project/pysort/
    newmergeSort100 = sortObj.mergeSort(newArray100)
    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'the newarray100 list:\n\n', newmergeSort100)

    # Sorting the new array with Pysort package Quick Sort (using the indexes as the low and high pivots
    # in the parameters
    # references: https://pypi.org/project/pysort/
    # https://www.geeksforgeeks.org/quick-sort/
    newmergeSort100 = sortObj.quickSort(newArray100, 0, 99)
    print('\nUsing the Pysort package to ' + startCyan + startBold + 'Quick Sort 100 numbers ' +
          endColor + 'the newarray100 list:\n\n', newmergeSort100)

    # Sorting the new array using the Timsort algorithm, as referenced from the Timsort author's page
    # The author's explanation quoted:
    #
    # -----"In a nutshell, the main routine marches over the array once, left to right,
    # alternately identifying the next run, then merging it into the previous
    # runs "intelligently".  Everything else is complication for speed, and some
    # hard-won measure of memory efficiency.-----
    # reference: https://github.com/python/cpython/blob/master/Objects/listsort.txt

    # To install Timsort in Pycharm IDE, installed in terminal:
    # npm install -g bower
    # bower install --save timsort
    # Appears bower deprecated; switching to npm install
    # references: https://www.jetbrains.com/help/pycharm/using-bower-package-manager.html
    # https://libraries.io/bower/timsort
    # In Pycharm IDE terminal:
    # pip install npm
    # npm install --save timsort
    # npm install timsort
    # in order to utilize the installed timsort, uploaded the 'require' package to use in the code
    # import require, shown at top of program

    # Python sort() method utilizes the Timsort algorithm:
    # references: https://www.quora.com/Which-sorting-algorithm-is-used-by-Python-in-the-sort-method
    # https://stackoverflow.com/questions/10948920/what-algorithm-does-pythons-sorted-use
    #

    timSort100 = sorted(newArray100, reverse=False)
    print('\nTimsort 100 numbers in order:\n', timSort100)

    timSort100 = sorted(newArray100, reverse=True)
    print('\nTimsort 100 numbers in reverse:\n', timSort100)



Main()