
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Activation, Dropout, BatchNormalization
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import RMSprop

from shuffler import Shuffler
from test import getModel

class Trainer:
    def __init__(self):
        self.reset()
        self.s = Shuffler()
        #self.model.summary()

    def reset(self):
        self.model = getModel()
        self.model.compile(optimizer=RMSprop(),loss='binary_crossentropy', metrics=['acc'])

    def train(self, epoc, dSize, bs):
        for i in range(epoc):
            deck = self.s.returnDeck(dSize)
            x = deck['x']
            y = deck['y']
            tdeck = self.s.returnDeck(50, True)
            vx = tdeck['x']
            vy = tdeck['y']
            self.model.fit(x, y, epochs=1,batch_size=bs, validation_data=(vx, vy))
            print(self.model.predict(x[:10]) > 0.5)
            print(y[:10])
    
    def test(self, dSize):
        deck = self.s.returnDeck(dSize, True)
        x = deck['x']
        y = deck['y']
        self.model.evaluate(x, y)

    def perfect_fit(self, epoc, dSize, bs):
        deck = self.s.returnDeck(dSize)
        x = deck['x']
        y = deck['y']
        for i in range(epoc):
            self.model.fit(x, y, epochs=1,batch_size=bs)
            print(self.model.predict(x[:10]) > 0.5)
            print(y[:10])

if __name__ == "__main__":
    a = Trainer()
    a.train(10, 100)