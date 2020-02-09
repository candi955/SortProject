# Attempting to use a linked list library
# reference: https://stackoverflow.com/questions/13835267/why-python-doesnt-have-a-native-linked-list-implementation
# https://github.com/teroqim/linkedlist/blob/2b44fd596b08b20c714bcd009911836694a20f17/linkedlist/linked_list.py

import numpy as np
import random
import time
from sorting_techniques import pysort
import linkedlist
from linkedlist import LinkedList

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



# --------------------------------------------------------------------------------------

print(startBlue + startBold + "\nAttemptng to use linkedlist() library now\n" + endColor)

newlist = LinkedList()