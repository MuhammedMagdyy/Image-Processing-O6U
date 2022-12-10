from skimage import io, color, util
from skimage import exposure as exp
import matplotlib.pyplot as plt

# Read An Image, You can also read from the full path
img = io.imread('Nature.jpg')

# Show Image
plt.imshow(img)
plt.title('Nature Image')
plt.show()

# Convert RGB to Gray level
gray = color.rgb2gray(img)
plt.imshow(gray, cmap='gray')
plt.title('Gray Nature')
plt.show()

# Convert an image to 8-bit unsigned integer format
bit = util.img_as_ubyte(gray)

# Apply Linear Rule (S = L - 1 - r)
linear = 255 - bit
plt.imshow(linear, cmap='gray')
plt.title('Linear Rule')
plt.show()

# Apply Logarithmic Rule (S = c * log(1 + r))
c = 1.1  # put any number
log = exp.adjust_log(bit, c)
plt.imshow(log, cmap='gray')
plt.title('Logarithmic Rule')
plt.show()

# Apply Power (gamma) Rule (s = c * r ^ y), y -> gamma
c = 3.1
y = 1.1
power = exp.adjust_gamma(bit, y, c)
plt.imshow(power, cmap='gray')
plt.title('Power (gamma) Rule')
plt.show()
