import time
from PIL import Image

cTime = int(time.time())
RandomNumber = (cTime % 100) + 50

# if it is even
if RandomNumber % 2 == 0:
    RandomNumber += 10

print(f"Generated Number: {RandomNumber}")

# Open and path of image
#please change the path of image according to your path
  
imageP = r'D:\assgn\group-assignment-python-code\image1.png'
image = Image.open(imageP)
pixels = image.load()

newImage = Image.new("RGB", image.size)

# Modify the pixels
for i in range(image.width):
    for j in range(image.height):
        r, g, b = pixels[i, j]
        new_r = min(r + RandomNumber, 255)
        new_g = min(g + RandomNumber, 255)
        new_b = min(b + RandomNumber, 255)
        newImage.putpixel((i, j), (new_r, new_g, new_b))

# Save the new image
outPath = r'D:\assgn\group-assignment-python-code\outimage.png'
newImage.save(outPath)

# new image creation way
totalRedValue = 0

for i in range(newImage.width):
    for j in range(newImage.height):
        r, g, b = newImage.getpixel((i, j))
        totalRedValue += r

print(f"Total Changed Red Pixel Value: {totalRedValue}")
