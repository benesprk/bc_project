def show_img(image_adress):
    import numpy as np
    import matplotlib.pyplot as plt
    
    rows = 2048
    cols = 2448
    
    with open('images/test2.raw', 'rb') as file:
        raw_data = file.read()
    
    image = np.frombuffer(raw_data, dtype=np.uint8)
    image = image.reshape((rows, cols))
    
    plt.imshow(image, cmap='gray')
    plt.show()
    return None