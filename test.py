
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

import tensorflow as tf
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Activation, Dropout, BatchNormalization, Input, MaxPool2D

#600, 800

def getModel():
    inputs = Input(shape=(800, 600, 1))
    x = inputs

    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    x = _x
    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    x = _x + x
    x = MaxPool2D((4, 3))(x)
    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    x = _x + x
    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    x = _x + x
    x = MaxPool2D((4, 3))(x)
    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = BatchNormalization()(x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    _x = Conv2D(128, (4, 3), padding='same', activation='relu')(_x)
    x = _x + x
    x = MaxPool2D((4, 3))(x)
    x = Conv2D(64, (1, 1), padding='same')(x)
    x = Flatten()(x)
    x = Dense(100)(x)
    x = Dropout(0.5)(x)
    x = Dense(1, activation='sigmoid')(x)

    outputs = x

    model = Model(inputs, outputs)
    return model
'''
model = getModel()

model.summary()
'''