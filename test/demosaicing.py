import cv2
import matplotlib.pyplot as plt

def demosaic_img(image):
    orange_image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
    final_image = cv2.cvtColor(orange_image, cv2.COLOR_BGR2RGB)

    plt.figure("Demosaic")
    plt.imshow(final_image)
    plt.title("demosaic")
    plt.axis('off')
    plt.show()
    return final_image