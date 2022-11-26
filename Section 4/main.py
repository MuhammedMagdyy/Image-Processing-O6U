from skimage import io
from skimage.transform import rotate
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

# Read An Image, You can also read from the full path
img = io.imread('Nature.jpg')

# Draw a rectangle on an image
# [from pixel:to pixel] #[R   G   B]
img[50:200, 10:110, :] = [0, 255, 0]
plt.imshow(img)
plt.title('Green Rectangle')
plt.show()

# Make a rotation for an image
# resize = true -> why ? if True no blank edges will appear and vice versa (try it)
rotate_img = rotate(img, angle=90, resize=True)
plt.imshow(rotate_img)
plt.title('Rotated Image')
plt.show()

# Make Convolution and Correlation on an image
new_img = np.array([[2, 2, 2, 3],
                    [2, 1, 3, 3],
                    [2, 2, 1, 2],
                    [1, 3, 2, 2]])

kernal = np.array([
    [1, -1, -1],
    [1, 2, -1],
    [1, 1, 1]
])

# Filter will rotate 180 degree when convolution executed
# We have 4 modes {‘reflect’, ‘constant’, ‘nearest’, ‘mirror’, ‘wrap’}
# You can read from here: [https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.convolve.html]
# constant -> default value for cval is [0]
correlation = ndimage.correlate(new_img, kernal, mode='constant')
convolution = ndimage.convolve(new_img, kernal, mode='constant')

print(correlation)
print('----------')
print(convolution)
