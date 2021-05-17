import MySQL_DB_Link
import MyJieba_hant
import cursorToList
import toList


def textEmotionalAnalysis():
    # queryAll
    queryList = (f'select test.text from localtest.test')

    # queryFunction
    # queryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')
    a = cursorToList.cursorToList(queryList)
    print(a)

    # for contextRow in cursorToList.cursorToList(queryList):
    #     jiebaResult = str(MyJieba_hant.MyJieba_hant(str(contextRow)))
    #     # print(type(jiebaResult))
    #     print(jiebaResult)
    #     word = list.append(context)
    #     print(word)
    # print(type(context))
    # word = MyJieba_hant.MyJieba_hant(context)
    # print(word)

    # print(type(queryList))
    # print(type(word))
    #
    # print(queryList)
    # print(word)


textEmotionalAnalysis()

# word = MyJieba_hant.MyJieba_hant(context)
# print(word)

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
