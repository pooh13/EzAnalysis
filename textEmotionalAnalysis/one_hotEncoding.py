import numpy as np
from sklearn.preprocessing import OneHotEncoder


def oneHotEncoding(comment_bow, bow):
    comment_bowLen = len(comment_bow) - 1

    bow_array = np.array(list(bow)).reshape(-1, 1)
    onehot = OneHotEncoder().fit(bow_array)

    X = np.ndarray((len(bow), len(bow)))
    for i in range(len(bow)):
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

    # print(type(X))
    # print(X)

    return X
