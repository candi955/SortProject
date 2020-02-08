# references:
# https://likegeeks.com/numpy-array-tutorial/
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
# https://ajakubek.github.io/python-llist/index.html
# https://pypi.org/project/llist/
# https://stackoverflow.com/questions/54780632/python-converting-a-linked-list-to-a-list-using-a-list-comprehension

import random
import time
import numpy as np
from sorting_techniques import pysort
from llist import dllist
from llist import sllist
import pandas as pd

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

    randomNums100 = np.array(random.sample(range(1, 101), 100))
    print('\nRandom numbers:\n', randomNums100)
    randomNumsAsList = randomNums100.tolist()
    print('\nRandom numbers as a list:\n', randomNumsAsList)

    lst = dllist([randomNums100])
    print('\nDoubly linked list:\n', lst)

    listedAgain = lst.nodeat(0)
    print(startBlue + '\nlistedAgain:' + endColor, listedAgain)

    sortObj = pysort.Sorting()
    mergeSort100 = sortObj.mergeSort(randomNums100)

    timSort100 = sorted(randomNums100, reverse=False)
    print(startPurple + startBold + '\nTimsort 100 numbers:\n' + endColor, timSort100)

    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'the newarray100 list:\n\n', mergeSort100)

    linked = DoublyLinkedList()
    linked.insert_in_emptylist(randomNums100)
    linked.traverse_list()
    print('\nhello\n')
    linked.traverse_list()
    print('\nhelloagain\n')
    print(np.array(listedAgain))
    print('what')
    updatedMergeList = np.array(listedAgain).tolist()
    print(np.array(listedAgain).tolist())
    print('why')
    print(randomNums100)

    print('whhhhhhaaaaaattttt')

    ranNum100 = np.array(random.sample(range(1, 101), 100))
    print('\nRandom numbers:\n', ranNum100)

    ranNum100AsList = randomNums100.tolist()
    print('\nRandom numbers as a list:\n', ranNum100AsList)

    dblLinkedList = dllist([ranNum100])
    print('\nDoubly linked list:\n', dblLinkedList)

    dbllistedAgain = dblLinkedList.nodeat(0)
    print(startBlue + '\nlistedAgain:' + endColor, dbllistedAgain)

    print('\nwho\n')

    dblListedAgainArray = np.array(dbllistedAgain)
    print('where that at?')
    print('\nDbl listed as array: ', dblListedAgainArray)
    print('\nDbl listed again array as list(): ', dblListedAgainArray.tolist())
    n = dblListedAgainArray.tolist()
    l = len(dblLinkedList)
    arandom = np.array(random.sample(range(1, 101), 100))
    a = len(arandom)
    aStr = str(arandom)

    print('\nLength of Dbl length list list(): ', l)
    print('\nLength of array(): ', a)
    print('\nRegular array as string:', a)
    print('\nwhat happened here?')

    sep = ','

    splitted = aStr.split()
    print("\nHere is the regular array split by ',': ", splitted)
    Strlinked = str(dblLinkedList)
    splittedLinked = Strlinked.split()
    print("\nLinked list as string, splitted: ", splittedLinked)


    # iloc
    #dblListedAgainIloc = dblListedAgainArray.iloc[:, 0]
    #print('dblListedAgain Iloc: ', len(dblListedAgainIloc))

    # merging doubly linked list as splitted string
    merging = sortObj.mergeSort(splittedLinked)
    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'the string dbl linked list:\n\n', merging)
    mergingAgain = sortObj.mergeSort(merging)
    mergingAgainArray = np.array(mergingAgain)
    mergingAgainArrayList = list(mergingAgainArray)
    mergingAgainArrayListMerged = sortObj.mergeSort(mergingAgainArrayList)
    # merging the doubly linked splitted string list as an array list() also
    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'again in the dbl linked list:\n\n', mergingAgainArrayListMerged)

    # attempting to turn the arrays of mergingAgainArray into separate columns, then concatenate before
    # turning into a list
    mergingAgainArrayDF = pd.DataFrame(mergingAgainArray)
    print('\nMergingAgainArrayDF dataframe through pandas library: ', mergingAgainArrayDF)
    mergingAgainArrayDFIloc1 = mergingAgainArrayDF.iloc[:, 0]
    print('\nColumn 1 of the dataframe: ', mergingAgainArrayDFIloc1)
    print('\nmore\n')
    m = mergingAgainArrayDF.iloc[0:101, 0]
    mDF = pd.DataFrame(m)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    print(mDF)
    # print("\nColumn 1 mergingAgainArray: ", np.concatenate(mergingAgainArrayListMerged))

    #####
    print('\n\n####### Attempting again with splittedLinkList ######')
    # attempting to turn the arrays of mergingAgainArray into separate columns, then concatenate before
    # turning into a list
    mergingSplittedLinkDF = pd.DataFrame(splittedLinked)
    print('\nMergingAgainArrayDF dataframe through pandas library: ', mergingSplittedLinkDF)
    mergingSplittedLinkIloc = mergingSplittedLinkDF.iloc[:, 0]
    print('\nColumn 1 of the dataframe: ', mergingSplittedLinkIloc)
    print('\nmore\n')
    m2 = mergingSplittedLinkDF.iloc[0:101, 0]
    m2DF = pd.DataFrame(m)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    print(m2DF)
    # print("\nColumn 1 mergingAgainArray: ", np.concatenate(mergingAgainArrayListMerged))

    c = mergingSplittedLinkDF.iloc[:, 0]
    print('\n\n', c, '\n\n')
    d = mergingSplittedLinkDF.head()
    print('\n\n', d, '\n\n')
    # e = mergingSplittedLinkDF.
    # print('\n\n', e, '\n\n')
    f = str(c)
    g = list(f)


    # merging doubly linked list as splitted string
    merging = sortObj.mergeSort(g)
    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'the the iloc 0 of a split linked list:\n\n', merging)

    print('-------------------------------------------------------')

    linking = DoublyLinkedList()
    rNums100 = np.array(random.sample(range(1, 101), 100))
    linking.insert_in_emptylist(rNums100)
    linking.traverse_list()
    print('hello')
    list = np.array(linking.traverse_list())
    print('blah')
    print(list)
    print('blahblahblah')
    # merging doubly linked list as splitted string
    data = []
    data2 = np.array(linking.traverse_list())
    datalist= data2.tolist()
    print(data2.size)
    newdata = np.array(linking.traverse_list())
    newdataDF = pd.DataFrame(newdata)
    newerdata = newdataDF.iloc[1:, 0]
    print('weasel')
    print(newdataDF)

    print('whoohooo')
    merging = sortObj.mergeSort(newdata)
    print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
          endColor + 'the the iloc 0 of a split linked list:\n\n', merging)









Main()