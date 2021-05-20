import os
import JiebaResult
import tokenization
import one_hotEncoding

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def textEmotionalAnalysis():
    # -----queryAll
    tableQueryList = (f'select * from localtest.test')
    textQueryList = (f'select test.text from localtest.test')

    # -----queryFunction
    # textQueryList = (f'select test.text from localtest.test where id = ' + line_id)

    # args = (b'test.text', b'localtest.test')

    # -----tokenization
    print(tokenization.tokenization(textQueryList)[0])
    print(tokenization.tokenization(textQueryList)[1])
    # print(type(tokenization.tokenization(tableQueryList, textQueryList)))
    # tokenization.tokenization(tableQueryList, textQueryList)

    # one_hotEncoding.oneHotEncoding(JiebaResult())




textEmotionalAnalysis()

# main.py original
# def textEmotionalAnalysis():
#     pass
#
# textEmotionalAnalysis()
