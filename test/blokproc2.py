import numpy as np
import matplotlib.pyplot as plt
from colour_demosaicing import demosaicing_CFA_Bayer_bilinear
import cv2

def blockproc(im, block_sz, func):
    # h, w, c = im.shape
    # m, n = block_sz
    # for x in range(0, h, m):
    #     for y in range(0, w, n):
    #         block = im[x:x+m, y:y+n]
    #         block[:,:] = func(block)
    h, w, c = im.shape
    processed = im.copy()
    m, n = block_sz
    for ch in range(c):  # Iterate over channels
        for x in range(0, h, m):
            for y in range(0, w, n):
                block = im[x:x+m, y:y+n, ch]
                processed[x:x+m, y:y+n, ch] = func(block)
    return im