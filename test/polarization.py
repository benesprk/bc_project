from show_image import show_img
from demosaicing import demosaic_img
from block_proc import block_proccessing

image_adress = 'images/test2.raw'

grayscale_image = show_img(image_adress)

demosaiced_image = demosaic_img(grayscale_image)

processed_image = block_proccessing(demosaiced_image)