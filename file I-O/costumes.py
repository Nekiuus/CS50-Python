from PIL import Image, ImageDraw

# Create two simple images
img1 = Image.new("RGB", (100, 100), color="red")
img2 = Image.new("RGB", (100, 100), color="blue")

img1.save("test.gif", save_all=True, append_images=[img2], duration=500, loop=0)


'''
import sys

from PIL import Image

images=[]

for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=images[1:], duration=200, loop=0)
'''