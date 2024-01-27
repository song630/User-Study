import cv2
import numpy as np
import os
import sys


dst_dir = f'/Users/song630/intern/user-study/github/User-Study/v2/anydoor/'
N = 97

for i in range(N):
    img = cv2.imread(f'{dst_dir}{i}.png')
    # each image is 1536x512, only keep the right 512x512:
    img = img[:, 1024:1536, :]
    cv2.imwrite(f'{dst_dir}{i}_0.png', img)
