# Time Duration Page for Sorting Doubly Linked Lists (Merge Sort, Insertion Sort, and Tim Sort)

# Side notes:
# Due to memory issues Merge Sort for DLL would show error for 10,000 and 100,000 numbers.  I used the initial
# number difference of approximately two times the difference between the time duration for 100 and 1,000 random
# number processing to calculate approximate values for the higher numbers that could not be completed currently.

# Similarly, I had to approximate the value for Insertion Sort DLL 100,000 number processing duration, due to the
# length of time it was taking to process. From 100 to 1,000 numbers, the increase in time duration
# was approximately 76 times , and for the time duration between 1,000 and 10,000 random numbers,
# approximatley 109 times, 33 more times than before.  I will use the similar approximation of 109 + 33,
# or 142 times in order to come up with the final time duration for Insertion Sort DLL of 100,000 numbers.
# My finding is that it would have taken approximatly an hour to complete the sort for 100,000 random numbers.

# Pandas table and Matplotlib line plot

# Comparing time durations of the Merge Sort, Insertion Sort, and Timsort functions in python for 100, 1000, 10000, and
# 100000 random numbers.

# Main reference for the Matplotlip plot on this page:
# https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py

# Other references:
# https://matplotlib.org/api/table_api.html?highlight=table#module-matplotlib.table
# https://matplotlib.org/gallery/index.html
# https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py

import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

# Creating a variable for data being pulled from the TimeDurationComparisonSortDLL.xlsx file and placed into array format
book = xlrd.open_workbook('TimeDurationComparisonSortDLL.xlsx')
sheets = book.sheets()
for sheet in sheets:
    data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# Creating a variable for data to be transformed into excel file format
timeduration_df = pd.read_excel(book, index_col=None,
                                na_values=['NA'])

class Regression():
    def _showTable_(self):

        # Showing the data that was pulled from TimeDurationComparisonSortDLL.xlsx in array form
        print("\n\nData pulled from the excel file:\n\n", data, "\n\n")

        # Obtaining the shape of the data
        print("Data shape: ", data.shape, "\n\n")
        # Data shape:  (9, 4)

        # Showing the data that was pulled from TimeDurationComparisonSortDLL.xlsx in excel form
        print("Data put into excel format:\n\n", timeduration_df, "\n\n")

    # Reference for plot:
    # https: // matplotlib.org / gallery / lines_bars_and_markers / categorical_variables.html  # sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
    def _showPlot_(self):

        # Attempting to create a table and plot chart of the dataframe TimeDurationComparisonSortDLL.xlsx
        # using iloc (row and column slicing) for python, references:
        # https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
        # https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/
        # Rows 0-7 (0:8), and columns 1-3 (to take out column 0, shows as 1:4 in iloc) to show the main data in the
        # dataframe
        ###data = timeduration_df.iloc[0:8, 1:4]
        print("------- Splitting the dataframe into sections -------\n\nThe data of the dataframe:\n\n", data, "\n")

        # 1st data column, the Merge Sort column
        mergeSortData = timeduration_df.iloc[:, 1]
        print("Mergesort column: \n", mergeSortData, "\n")

        # 2nd data column, the Quick Sort column
        insertionSortData = timeduration_df.iloc[:, 2]
        print("Quicksort column: \n", insertionSortData, "\n")

        # 3rd data column, the Tim Sort column
        timSortData = timeduration_df.iloc[:, 3]
        print("Timsort column: \n", timSortData, "\n")

        # This is the iloc to show the entire first column, the row labels, of the dataframe, for the label column
        rowLabels_ForData = timeduration_df.iloc[:, 0]
        print("The column of the dataframe:\n\n", rowLabels_ForData, "\n")

        # This is to pull the top label for the data only, with the variable set to call the index 0.
        # You can change the index to show more rows.
        columnLabels = data[0]
        print("Showing the header labels only:\n\n", columnLabels, "\n\n")


        # saving value creation for future reference
        # Creating values for the graph
        # Creating the values variable as increments 0.125 apart, between 0 and 1.625, so that the top level value
        # shows as 1.5
        # using np.arange(bottom level #, just above top level #, increment)
        # reference: https://appdividend.com/2019/01/31/numpy-arange-tutorial-with-example-python-numpy-functions/

        fig, ax = plt.subplots()

        ax.plot(rowLabels_ForData, mergeSortData, label="Merge Sort DLL")
        ax.plot(rowLabels_ForData, insertionSortData, label="Insertion Sort DLL")
        ax.plot(rowLabels_ForData, timSortData, label="Timsort DLL")
        ax.legend()

        # x and y axis labels
        plt.xlabel("Number of Random Numbers Sorted\n")
        plt.ylabel("Amount of Time Duration in Seconds\n")

        # The top title (suptitle) and title descriptor(title)
        plt.suptitle("Duration in Seconds of Sort Doubly Linked Lists in Python")
        plt.title("\nMerge Sort, Insertion Sort, and Timsort")

        plt.show()

        # Reference for plot:
        # https: // matplotlib.org / gallery / lines_bars_and_markers / categorical_variables.html  # sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py

Regression()

show = Regression()

# Calling methods
show._showTable_()
show._showPlot_()