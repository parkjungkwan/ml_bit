import tensorflow as tf
import keras

from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense

class IrisModel:
    def __init__(self):
        iris = datasets.load_iris()
        self._X = iris.data
        self._Y = iris.target

    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()


        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, Y_1hot, epochs=300, batch_size=10)
        print('Model training is complete')

        file_name = 'saved_model/iris_model.h5'
        model.save(file_name)  # model을 저장한다
        print('Model Saved in ' + file_name)