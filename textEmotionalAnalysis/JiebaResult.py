import MyJieba_hant
import cursorToList


def JiebaResult(queryList):
    # -----jieba limit
    # for contextRow in cursorToList.cursorToList(queryList):
    #     JiebaResult = str(MyJieba_hant.MyJieba_hant(str(contextRow)))
    #     print(JiebaResult)

    return[str(MyJieba_hant.MyJieba_hant(str(contextRow))) for contextRow in cursorToList.cursorToList(queryList)]

# print(type(JiebaResult('select test.text from localtest.test')))
# print(JiebaResult('select test.text from localtest.test'))
# print(JiebaResult('select test.text from localtest.test')[2])
