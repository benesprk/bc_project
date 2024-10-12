import numpy as np
import matplotlib.pyplot as plt
from colour_demosaicing import demosaicing_CFA_Bayer_bilinear

def block_proccessing(image):
    h,w,c = image.shape
    proc = np.zeros((h//2, w//2))

    for i in range(0, h-2, 2):
        for j in range(0, w-2, 2):
            block = image[i:i+2, j:j+2]

            proc[i//2, j//2] = np.mean(block)

    proc_normalized = (proc - np.min(proc)) / (np.max(proc) - np.min(proc)) * 255
    proc8 = np.uint8(proc_normalized)

    processed_image = demosaicing_CFA_Bayer_bilinear(proc8, 'RGGB')
    processed_image = (processed_image - np.min(processed_image)) / (np.max(processed_image) - np.min(processed_image)) * 255
    processed_image = processed_image.astype(np.uint8)

    plt.figure("Average and demosaic")
    plt.imshow(processed_image)
    plt.title("Average and demosaic")
    plt.axis('off')
    plt.show()

    return processed_image