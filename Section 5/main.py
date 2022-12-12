from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import gaussian, sobel

img_gaussian = data.astronaut()

# gaussian has 2 parameters(in our case)
# 1- The image
# 2- sigma -> this is Standard deviation for Gaussian kernel
# كل ما هزودها كل ما الـ Blur هيزيد والعكس صحيح (جربوها)
filtered_gaussian_img = gaussian(img_gaussian, 2)

# subplots -> دي بتخليني ارسم (اعرض) اكتر من حاجة جوة الشكل الابيض اللي بيظهر لنا
# ببعت عليها عدد الصفوف والاعمدة وهو حرفيًا بيعمل ماتريكس عشان اقدر أعمل أكسز للفيجر
# لما بخلي الصف بـ 1 بقدر أعمل أكسز أكنها أراي مش مالتي أراي
# fig -> this is the figur (الحجم اللي عايز اعمله)
# ax -> لو عايز أكسز على فيجر معين

fig, ax = plt.subplots(1, 2, figsize=(50, 50))
ax[0].inshow(filtered_gaussian_img)
ax[1].imshow(img_gaussian)
plt.show()

# ---- #

img_sobel = data.coins()

filtered_sobel_img = sobel(img_sobel)

fig_sobel, ax_sobel = plt.subplots(1, 2, figsize=(50, 50))
ax_sobel[0].imshow(filtered_sobel_img, cmap='gray')
ax_sobel[1].imshow(img_sobel, cmap='gray')
plt.show()
