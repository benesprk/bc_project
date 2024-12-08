from block_proc import block_processing
import matplotlib.pyplot as plt

def plot_polarized_images(image):
    angles = [90, 45, 135, 0]
    titles = ['90°', '45°', '135°', '0°']

    for i, angle in enumerate(angles):
        plt.figure("Polarized images", figsize=(10, 8))
        proc = block_processing(image, angle, plot=False)
        plt.subplot(2,2,i+1)
        plt.imshow(proc)
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()
