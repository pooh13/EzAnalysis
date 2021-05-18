import os
import MyJieba_hant
import cursorToList

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def textEmotionalAnalysis():
    # queryAll
    queryList = (f'select test.text from localtest.test')

    # queryFunction
    # queryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')

    # jieba
    for contextRow in cursorToList.cursorToList(queryList):
        JiebaResult = str(MyJieba_hant.MyJieba_hant(str(contextRow)))

        # # print(type(JiebaResult))
        print(JiebaResult)
        # return JiebaResult




textEmotionalAnalysis()

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
