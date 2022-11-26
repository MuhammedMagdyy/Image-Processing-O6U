from skimage import io, color
import matplotlib.pyplot as plt
import skimage.transform as tf

# Read An Image, You can also read from the full path
img = io.imread('Nature.jpg')

# Show Image
plt.imshow(img)
plt.title('Nature Image')
plt.show()

# Save An Image
io.imsave(fname='C:\\path\\path\\Desktop\\newImage.jpg', arr=img)

# Convert RGB to Gray level
gray = color.rgb2gray(img)
plt.imshow(gray, cmap='gray')
plt.title('Gray Nature')
plt.show()

# Height and Width (Careful it's double)
print(f"Y (Height) -> {int(img.shape[0])}")
print(f"X (Width) -> {int(img.shape[1])}")

# Resize Image -> resize(Height, width)
new_img = tf.resize(gray, (500, 200))
plt.imshow(new_img, cmap='gray')
plt.title('New Sized Gray Image')
plt.show()

print(f"Y (Height) -> {int(new_img.shape[0])}")
print(f"X (Width) -> {int(new_img.shape[1])}")

# Histogram
plt.hist(gray.ravel())
plt.title('Histogram')
plt.show()
