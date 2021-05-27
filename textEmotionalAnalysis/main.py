import os

import MLP_Model
import cursorToPd
import tokenization
import one_hotEncoding
import MyTrain_test_split

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def textEmotionalAnalysis():

    # ----- queryAll
    tableQueryList = (f'select * from localtest.test')
    textQueryList = (f'select test.text from localtest.test')
    moodQueryList = (f'select test.mood from localtest.test')

    # ----- queryFunction
    # textQueryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')

    # ----- tokenization
    # print(tokenization.tokenization(textQueryList)[0])
    # print(tokenization.tokenization(textQueryList)[1])
    # print(type(tokenization.tokenization(tableQueryList, textQueryList)))
    # tokenization.tokenization(tableQueryList, textQueryList)

    # ----- one_hotEncoding
    X = one_hotEncoding.oneHotEncoding(tokenization.tokenization(textQueryList)[0], tokenization.tokenization(textQueryList)[1], moodQueryList)
    # print(X)

    # ----- column "mood"
    y = cursorToPd.cursorToPd(moodQueryList)

    # ----- check row amount
    # print(X.shape)
    # print(y.shape)

    # ----- MyTrain_test_split
    a = MyTrain_test_split.MyTrain_test_split(X, y)

    # print(type(a))
    # print(a)
    # print('-'*80+'\n')
    # print(a[0])
    # print('-'*80+'\n')
    # print(a[1])
    # print('-'*80+'\n')
    # print(a[2])
    # print('-'*80+'\n')
    # print(a[3])

    # ----- MLP_Model
    b = MLP_Model.MLP_Model(MyTrain_test_split.MyTrain_test_split(X, y)[0],
                        MyTrain_test_split.MyTrain_test_split(X, y)[1],
                        MyTrain_test_split.MyTrain_test_split(X, y)[2],
                        MyTrain_test_split.MyTrain_test_split(X, y)[3])

    print(type(b))
    print(b)


textEmotionalAnalysis()

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
