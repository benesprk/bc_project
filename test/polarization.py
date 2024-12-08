from show_image import show_img
from demosaic import demosaic_img
from block_proc import block_processing
from blokproc2 import blockproc
from polar import plot_polarized_images

import numpy as np
import matplotlib.pyplot as plt

image_adress = 'images/test2.raw'
# image_adress = 'images/test_display.raw'
# plot = False
angle = -1

grayscale_image = show_img(image_adress, plot=False)

demosaiced_image = demosaic_img(grayscale_image, plot=False)

processed_image = block_processing(demosaiced_image, angle, plot=True)

# processed_image = blockproc(demosaiced_image, (2,2), np.mean) #average and possibly demosaic unsure


plt.figure("")
plt.imshow(processed_image)
plt.title("Average and demosaic")
plt.axis('off')
plt.show()

# plot_polarized_images(processed_image)