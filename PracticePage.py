# references:
# https://likegeeks.com/numpy-array-tutorial/
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
# https://ajakubek.github.io/python-llist/index.html
# https://pypi.org/project/llist/

import random
import time
import numpy as np
from sorting_techniques import pysort
from llist import dllist
from llist import sllist

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

randomNums100 = np.array(random.sample(range(1, 101), 100))
print('\nRandom numbers:\n', randomNums100)
randomNumsAsList = randomNums100.tolist()
print('\nRandom numbers as a list:\n', randomNumsAsList)

lst = sllist([randomNums100])
print('\nSingly linked list:\n', lst)

listToList = lst.tolist()

listed = list(lst)
print('\nSingly linked list copied to list():\n', listed)

sortObj = pysort.Sorting()
mergeSort100 = sortObj.mergeSort(listed)

print('\nUsing the Pysort package to ' + startPurple + startBold + 'Merge Sort 100 numbers ' +
      endColor + 'the newarray100 list:\n\n', mergeSort100)