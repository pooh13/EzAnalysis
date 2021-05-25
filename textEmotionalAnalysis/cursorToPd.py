import cursorToList
import pandas as pd

def cursorToPd(queryList):

    contextRowList = list()

    for contextRow in cursorToList.cursorToList(queryList):

        contextRowList.append(contextRow)
        contextRowSeries = pd.Series(contextRowList)
        # print(type(contextRowList))
        # print(contextRowList)

    return contextRowSeries
