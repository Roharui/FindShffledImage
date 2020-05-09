
from PIL import Image
import numpy as np
import os
from random import shuffle, random

class Shuffler:
    def __init__(self):
        self.base = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.pimg = os.path.join(self.base, "img")

        self.imgs = [os.path.join(self.pimg, i, x, y) for i in os.listdir(self.pimg) 
            for x in os.listdir(os.path.join(self.pimg, i)) for y in os.listdir(os.path.join(self.pimg, i, x))]

        self.trlst = self.imgs[:int(len(self.imgs) * 0.8)]
        self.tslst = self.imgs[int(len(self.imgs) * 0.8):]

        print(len(self.imgs))
        self.dc = ((6, 1),(5, 5))

    def returnDeck(self, decSize, testMode=False):
        lst = self.trlst
        if testMode:
            lst = self.tslst
        x = []; y = []
        for i in range(decSize):
            if random() > 0.5:
                b = 0
                a = self.imgShuffle(lst[i])
            else:
                b = 1
                a = self.readImg(lst[i])
                a = self.expan_axis(a)
            x += [np.array(self.reduction(a)).reshape(800, 600, 1)]
            y += [b]
            shuffle(lst)
        return {'x':np.array(x), 'y':np.array(y)}

    def readImg(self, filePath) :
        img = Image.open(filePath).convert('L')
        return np.asarray(img)

    def imgShuffle(self, img):
        realimg = self.readImg(img)
        imgs = self.divide(realimg, False)
        shuffle(imgs)
        allimg = self.putTogether(imgs, False, realimg.shape)

        return allimg

    def divide(self, img, useX):
        #True = 사용, False 미사용
        ysize, xsize = img.shape

        dcY, dcX = self.dc[int(useX)]
        y = int(ysize/dcY); x = int(xsize/dcX)

        result = []
        for i in range(dcY):
            for j in range(dcX):
                result.append(img[(i * y):((i+1) * y),
                                    (j * x):((j + 1) * x)])

        return result

    def putTogether(self, imgPart, useX, shape):
        num = 0
        ysize, xsize = shape

        dcY, dcX = self.dc[int(useX)]
        y = int(ysize/dcY); x = int(xsize/dcX)

        result = np.ones((ysize, xsize, 1))
        for i in range(dcY):
            for j in range(dcX):
                result[(i * y):((i+1) * y),
                                (j * x):((j + 1) * x), :] *= imgPart[num][:,:,np.newaxis]
                
                num += 1
        return result

    def reduction(self, img):
        img = img.resize((800, 600))
        return img

    def expan_axis(self, img):
        ysize, xsize = img.shape

        result = np.ones((ysize, xsize, 1))
        result *= img[:,:,np.newaxis]

        return result


if __name__ == "__main__":
    a = Shuffler()
    a.imgShuffle(a.imgs[1])
    
