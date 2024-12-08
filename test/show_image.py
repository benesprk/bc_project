def show_img(image_adress, plot ):
    import numpy as np
    import matplotlib.pyplot as plt
    
    rows = 2048
    cols = 2448
    
    with open(image_adress, 'rb') as file:
        raw_data = file.read()
    
    image = np.frombuffer(raw_data, dtype=np.uint8)
    image = image.reshape((rows, cols))
    
    if plot:
        plt.figure('Input RAW image')
        plt.imshow(image, cmap='gray')
        plt.title('Input RAW image')
        plt.axis('off')
        plt.show()
    return image