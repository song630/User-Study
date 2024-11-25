import cv2
import numpy as np
import os, sys
from tqdm import tqdm


N = 146

def crop_image():
    for i in tqdm(range(0, N)):
        img = cv2.imread(f'onestage/{i}_0_all.png')
        # each image has 4 512x512 images in a row; only keep the rightmost one:
        img = img[:, 3*512:4*512]
        cv2.imwrite(f'onestage/{i}.png', img)


if __name__ == '__main__':
    crop_image()
