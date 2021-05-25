import os
import cursorToPd
import tokenization
import one_hotEncoding
import MyTrain_test_split

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def textEmotionalAnalysis():

    # -----queryAll
    tableQueryList = (f'select * from localtest.test')
    textQueryList = (f'select test.text from localtest.test')
    moodQueryList = (f'select test.mood from localtest.test')

    # -----queryFunction
    # textQueryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')

    # -----tokenization
    # print(tokenization.tokenization(textQueryList)[0])
    # print(tokenization.tokenization(textQueryList)[1])
    # print(type(tokenization.tokenization(tableQueryList, textQueryList)))
    # tokenization.tokenization(tableQueryList, textQueryList)

    # ----- one_hotEncoding
    X = one_hotEncoding.oneHotEncoding(tokenization.tokenization(textQueryList)[0], tokenization.tokenization(textQueryList)[1], moodQueryList)
    # print(X)

    y = cursorToPd.cursorToPd(moodQueryList)

    # print(X.shape)
    # print(y.shape)

    a = MyTrain_test_split.MyTrain_test_split(X, y)

    print(type(a))
    print(a)




textEmotionalAnalysis()

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
