import MySQL_DB_Link
import MyJieba_hant
import cursorToList
import toList


def textEmotionalAnalysis(test):
    # queryList = (f'select test.text from localtest.test')
    # print(type(queryList))
    # print(queryList)
    # args = (b'test.text', b'localtest.test')
    a = cursorToList.cursorToList(MySQL_DB_Link.MySQL_DB_Link(MySQL_DB_Link.MySQLConnectInfoStr[0],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[1],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[2],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[3],
                                                     MySQL_DB_Link.MySQLConnectInfoStr[4],).query(
                                                    'select test.text from localtest.test where id ='+test))
    print(a)

    # b = cursorToList.cursorToList(a)
    # print(b)

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


textEmotionalAnalysis('1')

# word = MyJieba_hant.MyJieba_hant(context)
# print(word)


# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
