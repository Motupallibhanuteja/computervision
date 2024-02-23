import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage.filters

pic_num       = 1
def show_abs(I, plot_title, pic_num):
    plt.figure(pic_num)
    plt.title(plot_title)
    plt.tight_layout()
    plt.axis('off')
    plt.imshow(abs(I), plt.cm.gray)
    return pic_num+1

A0           = scipy.misc.imread('moon1.jpg', flatten=True)

A0           = (A0 - np.amin(A0))*255.0 /(np.amax(A0)-np.amin(A0)) 

kernel      = np.ones((3,3))*(-1)
kernel[1,1] = 8

Lap        = scipy.ndimage.filters.convolve(A0, kernel)

ShF         = 100                
Laps        = Lap*ShF/np.amax(Lap) 

A           = A0 + Laps 
A = np.clip(A, 0, 255)

pic_num = show_abs(Laps, 'Scaled Laplacian', pic_num)
pic_num = show_abs(A, 'Sharpened image', pic_num)
plt.show()
