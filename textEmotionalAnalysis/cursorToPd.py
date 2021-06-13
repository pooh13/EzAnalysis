import pandas as pd
import cursorToList

def cursorToPd(queryList, pdType):

    contextRowList = list()

    for contextRow in cursorToList.cursorToList(queryList):

        contextRowList.append(contextRow)
        if pdType == 1:
            contextRowResult = pd.Series(contextRowList)
        elif pdType == 2:
            contextRowResult = pd.DataFrame(contextRowList)
        else:
            print('NO THIS "pdType"！')
            break
        # print(type(contextRowList))
        # print(contextRowList)

    return contextRowResult
