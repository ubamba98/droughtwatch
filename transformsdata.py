import random
import cv2
import numpy as np


class DualCompose:
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, x):
        for t in self.transforms:
            x = t(x)
        return x

class CenterCrop:
    def __init__(self, size):
        if isinstance(size, int):
            size = (size, size)

        self.height = size[0]
        self.width = size[1]

    def __call__(self, img):
        h, w, c = img.shape
        dy = (h - self.height) // 2
        dx = (w - self.width) // 2

        y1 = dy
        y2 = y1 + self.height
        x1 = dx
        x2 = x1 + self.width
        img = img[y1:y2, x1:x2]

        return img


class HorizontalFlip:
    def __init__(self, prob=0.5):
        self.prob = prob

    def __call__(self, img):
        if random.random() < self.prob:
            img =cv2.flip(img, 1)
        return img

class Resize:
    def __init__(self, size=224, interpolation=cv2.INTER_AREA):
        self.size = size
        self.interpolation = interpolation

    def __call__(self, img):
        img = cv2.resize(img, (self.size, self.size) , interpolation=self.interpolation)
        return img
    
class VerticalFlip:
    def __init__(self, prob=0.5):
        self.prob = prob

    def __call__(self, img):
        if random.random() < self.prob:
            img = cv2.flip(img, 0)
        return img
    
    
class Rotate:
    def __init__(self, limit=90, prob=0.5):
        self.prob = prob
        self.limit = limit

    def __call__(self, img):
        if random.random() < self.prob:
            angle = random.uniform(-self.limit, self.limit)

            height, width = img.shape[0:2]
            mat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1.0)
            img = cv2.warpAffine(img, mat, (height, width),
                                 flags=cv2.INTER_LINEAR,
                                 borderMode=cv2.BORDER_REFLECT_101)

        return img

class ImageOnly:
    def __init__(self, trans):
        self.trans = trans

    def __call__(self, x):
        return self.trans(x)
    
    
class Normalize:
    def __init__(self, in_ch=None):
        self.mean=np.array([0.720, 0.675, 0.644, 0.654, 0.734, 0.718, 0.679, 0.640, 0.249, 0.969, 0.971])
        self.std=np.array([0.197, 0.195, 0.186, 0.192, 0.168, 0.172, 0.183, 0.187, 0.417, 0.108, 0.108])
        self.mean = self.mean[in_ch]
        self.std = self.std[in_ch]

            
    def __call__(self, img):
        img= img.astype(np.float32)
        max_pixel_value = 255
        img = img/max_pixel_value 
        img -= np.ones(img.shape) * self.mean
        img /= np.ones(img.shape) * self.std
        return img



class RandomRotate90:
    def __init__(self, prob=0.5):
        self.prob = prob

    def __call__(self, img):
        if random.random() < self.prob:
            factor = random.randint(0, 4)
            img = np.rot90(img, factor)
        return img.copy()



