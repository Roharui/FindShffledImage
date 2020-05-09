
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

import tensorflow as tf
from tensorflow.keras import Sequential
import matplotlib.pyplot as plt
import numpy as np

class Tester:
    def __init__(self, model, shuf):
        self.model = model
        self.s = shuf

    def test(self, dSize, testlayer):
        deck = self.s.returnDeck(dSize)
        model = self.makeTestModel(range(testlayer))

        a = model.predict(deck['x'])
        
        print(a.shape)
        for i in range(dSize):
            c = deck['x'][i]
            ax = plt.subplot(2,dSize, i + 1)
            ax.set_title(str(deck['y'][i]))
            ax.imshow(c.reshape(c.shape[:-1]), cmap='gray')
        for i in range(dSize):
            c = a[i]
            ax = plt.subplot(2,dSize, i + dSize + 1)
            ax.set_title(str(deck['y'][i]))
            ax.imshow(c[:,:,0], cmap='gray')
        plt.show()

    
    def makeTestModel(self, rag):
        model = Sequential()

        for i in rag:
            model.add(self.model.layers[i])

        return model
        

