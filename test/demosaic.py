import cv2
import matplotlib.pyplot as plt

def demosaic_img(image, plot):
    result_image = cv2.cvtColor(image, cv2.COLOR_BayerBG2RGB)

    if plot:
        plt.figure("Demosaic")
        plt.imshow(result_image)
        plt.title("demosaic")
        plt.axis('off')
        plt.show()
    return result_image