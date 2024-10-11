from show_image import show_img
from demosaicing import demosaic_img
image_adress = 'images/test2.raw'

grayscale_image = show_img(image_adress)

demosaiced_image = demosaic_img(grayscale_image)
