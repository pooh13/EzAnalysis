from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

import cursorToPd
import one_hotEncoding
import tokenization


def MyTrain_test_split(X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
    # print(y_train.shape)
    # print(y_test.shape)

    y_train = to_categorical(y_train, num_classes=5)
    y_test = to_categorical(y_test, num_classes=5)
    # print(y_train.shape)
    # print(y_test.shape)

    return X_train, X_test, y_train, y_test

# MyTrain_test_split(one_hotEncoding.oneHotEncoding(tokenization.tokenization('SELECT dmsc_hant.Comment FROM localtest.dmsc_hant ORDER BY RAND() LIMIT 200')[0], tokenization.tokenization('SELECT dmsc_hant.Comment FROM localtest.dmsc_hant ORDER BY RAND() LIMIT 200')[1], 'SELECT dmsc_hant.Star FROM localtest.dmsc_hant ORDER BY RAND() LIMIT 200'), cursorToPd.cursorToPd('SELECT dmsc_hant.Star FROM localtest.dmsc_hant ORDER BY RAND() LIMIT 200'))

# MyTrain_test_split(one_hotEncoding.oneHotEncoding(tokenization.tokenization('SELECT test.text FROM localtest.test')[0], tokenization.tokenization('SELECT test.text FROM localtest.test')[1], 'SELECT test.mood FROM localtest.test'), cursorToPd.cursorToPd('SELECT test.mood FROM localtest.test'))
