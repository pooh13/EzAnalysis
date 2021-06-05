import numpy as np
from sklearn.preprocessing import OneHotEncoder
import cursorToPd

def oneHotEncoding(comment_bow, bow, queryList):

    comment_bowLen = len(comment_bow) - 1

    bow_array = np.array(list(bow)).reshape(-1, 1)
    onehot = OneHotEncoder(handle_unknown='ignore').fit(bow_array)

    df = cursorToPd.cursorToPd(queryList)
    # print(len(df))

    X = np.ndarray((len(df), len(bow)))
    for i in range(len(df)):
        if (len(comment_bow[i]) < comment_bowLen):
            # 少數僅含空白、標點符號之類而被刪除完內容的評論
            if (len(comment_bow[i]) == 0):
                X[i] = np.zeros((len(bow)))
            else:
                comment_array = np.array(list(comment_bow[i])).reshape(-1, 1)
                comment_onehot = onehot.transform(comment_array).toarray().sum(axis=0)
                X[i] = comment_onehot
        else:
            break

    return X
