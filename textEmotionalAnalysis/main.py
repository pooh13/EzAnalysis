import os

import MLP_Model
import RNN_Model
import cursorToPd
import tokenization
import one_hotEncoding
import twoTypeClassify
import MyTrain_test_split

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def textEmotionalAnalysis():

    # ----- queryAll
    # tableQueryList = (f'SELECT * FROM localtest.test')
    # textQueryList = (f'SELECT test.text FROM localtest.test')
    # moodQueryList = (f'SELECT test.mood FROM localtest.test')

    tableQueryList = (f'SELECT * FROM localtest.test ORDER BY dmsc_zh.ID LIMIT 100')
    textQueryList = (f'SELECT dmsc_zh.Comment FROM localtest.dmsc_zh ORDER BY dmsc_zh.ID LIMIT 100')
    moodQueryList = (f'SELECT dmsc_zh.Star FROM localtest.dmsc_zh ORDER BY dmsc_zh.ID LIMIT 100')

    # tableQueryList = (f'SELECT * FROM localtest.test')
    # textQueryList = (f'SELECT dmsc_zh.Comment FROM localtest.dmsc_zh')
    # moodQueryList = (f'SELECT dmsc_zh.Star FROM localtest.dmsc_zh')

    # ----- queryFunction
    # textQueryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')

    # ----- tokenization
    # print(tokenization.tokenization(textQueryList)[0])
    # print(tokenization.tokenization(textQueryList)[1])
    # print(type(tokenization.tokenization(tableQueryList, textQueryList)))
    # tokenization.tokenization(tableQueryList, textQueryList)

    # ----- one_hotEncoding
    X = one_hotEncoding.oneHotEncoding(tokenization.tokenization(textQueryList)[0],
                                       tokenization.tokenization(textQueryList)[1],
                                       twoTypeClassify.twoTypeClassify(moodQueryList, 0, '正負評'))
    # print(X)
    # print(twoTypeClassify.twoTypeClassify(moodQueryList, 0, '正負評'))

    # ----- column "mood"
    y = twoTypeClassify.twoTypeClassify(moodQueryList, 0, '正負評')
    # print(y)

    # ----- check row amount
    # print(X.shape)
    # print(y.shape)

    # ----- MyTrain_test_split
    # a = MyTrain_test_split.MyTrain_test_split(X, y)

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
    a1 = MLP_Model.MLP_Model(MyTrain_test_split.MyTrain_test_split(X, y)[0],
                        MyTrain_test_split.MyTrain_test_split(X, y)[1],
                        MyTrain_test_split.MyTrain_test_split(X, y)[2],
                        MyTrain_test_split.MyTrain_test_split(X, y)[3])

    print(type(a1))
    print(a1)

    # ----- RNN_Model
    # b1 = RNN_Model.RNN_Model(MyTrain_test_split.MyTrain_test_split(X, y)[0],
    #                     MyTrain_test_split.MyTrain_test_split(X, y)[1],
    #                     MyTrain_test_split.MyTrain_test_split(X, y)[2],
    #                     MyTrain_test_split.MyTrain_test_split(X, y)[3])

    # print(type(b1))
    # print(b1)


textEmotionalAnalysis()

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
