def toList(result):

    listResult=[]

    for column in result:
        listColumn = [column]
        string = ",".join(str(v) for v in listColumn)
        string = string.replace(" ","").replace("'","").replace("(","").replace(")","")
        # listCut = string.split(',')
        listCut = string[:-1]
        listResult.append(listCut)

    return listResult
