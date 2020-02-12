# Program for Timsort on doubly linked list 100 random numbers
# reference: https://www.youtube.com/watch?v=Xk0Tgh1AbfE
# reference: https://github.com/joeyajames/Python/tree/master/LinkedLists
# reference: https://github.com/joeyajames/Python/blob/master/LinkedLists/LinkedList1.py

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

# reference: https://github.com/joeyajames/Python/blob/master/LinkedLists/LinkedList1.py

class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def to_string(self):
        return "Node value: " + str(self.data);

    def has_next(self):
        if self.get_next() is None:
            return False;
        return True;

    def compare_to(self, y):
        if self.to_string() < y.to_string():
            return -1;
        elif self.to_string() > y.to_string():
            return 1;
        return 0;


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root);
        self.root = new_node;
        self.size += 1;

    def add_node(self, n):
        n.set_next(self.root);
        self.root = n;
        self.size += 1;

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:  # removing node that is not the root
                    prev_node.set_next(this_node.get_next())
                else:  # removing root node
                    self.root = this_node.get_next()
                self.size -= 1
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        print("Print List..........");
        if self.root is None:
            return;
        current = self.root;
        print(current.to_string());
        while current.has_next():
            current = current.get_next();
            print(current.to_string());

    def sort(self):
        if self.size > 1:
            newlist = [];
            current = self.root;
            newlist.append(self.root);
            while current.has_next():
                current = current.get_next();
                newlist.append(current);
            newlist = sorted(newlist, key=lambda node: node.get_data(), reverse=True);
            newll = LinkedList();
            for node in newlist:
                newll.add_node(node);
            return newll;
        return self;


myList = LinkedList()

for item in range(100):
    randomNum = np.array(random.sample(range(1, 1001), 1))
    myList.add(randomNum)

print("\n\nBefore sorting:")
myList.print_list()

print("\n\n100 Random numbers in a linked list, sorted using the Timsort method:")
myList.sort()
myList.print_list()