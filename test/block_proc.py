import numpy as np
import matplotlib.pyplot as plt
from colour_demosaicing import demosaicing_CFA_Bayer_bilinear
import cv2

def block_processing(image, angle, plot):
    h,w,c = image.shape     #h=2048 w=2448
    print(h)
    print(w)
    proc = np.zeros((h//2, w//2))       #
    b, g, r = cv2.split(image)

    block = image[1:3,1:3,0]
    print(block)

    output_00 = np.zeros((h // 2, w // 2))
    output_01 = np.zeros((h // 2, w // 2))
    output_10 = np.zeros((h // 2, w // 2))
    output_11 = np.zeros((h // 2, w // 2))

    if angle == -1:
        for i in range(0, h-2):
            for j in range(0, w-2):
                for c in range(0,2):
                    block = image[i:i+2, j:j+2, c]
                    proc[i//2, j//2] = np.mean(block)
    else:
        for i in range(0, h-2, 2):
            for j in range(0, w-2, 2):    
                block = image[i:i + 2, j:j + 2]

                output_00[i // 2, j // 2] = block[0, 0]
                output_01[i // 2, j // 2] = block[0, 1]
                output_10[i // 2, j // 2] = block[1, 0]
                output_11[i // 2, j // 2] = block[1, 1]
        return 


    proc_normalized = (proc - np.min(proc)) / (np.max(proc) - np.min(proc)) * 255
    proc8 = np.uint8(proc_normalized)

    processed_image = demosaicing_CFA_Bayer_bilinear(proc8, 'RGGB')
    processed_image = (processed_image - np.min(processed_image)) / (np.max(processed_image) - np.min(processed_image)) * 255
    processed_image = processed_image.astype(np.uint8)

    if plot:
        plt.figure("Average and demosaic")
        plt.imshow(processed_image)
        plt.title("Average and demosaic")
        plt.axis('off')
        plt.show()

    return processed_image