import cursorToList

def rowCount(queryList):

    return[(contextRowLen+1) for contextRowLen in range(len(cursorToList.cursorToList(queryList)))][-1]
