from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def MyTrain_test_split(X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
    print(X_train.shape)

    y_train = to_categorical(y_train, num_classes=5)
    y_test = to_categorical(y_test, num_classes=5)
    print(y_train.shape)

    return y_train, y_test
