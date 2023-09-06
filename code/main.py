#%%
from PIL import Image
import numpy as np
import pandas as pd

#Gets the image
#get home dir
#home_dir = os.path.expanduser("~") + "C:\Users\datng\iCloudDrive\0. College\0.Machine Learning Projects\DigitReg"
image = Image.open("../images/gay.png") #Loads the image
image = image.convert("L") #Converts the image to grayscale
image = image.resize((28, 28)) #Resizes the image to 28x28 (if necessary)

pixels = []

#Loops through each pixel
for y in range(0, 28):
    for x in range(0, 28):
        pixel = image.getpixel((x, y))
        binary = 1 if (pixel < 255) else 0
        pixels.append(binary)
array = [pixels[i] for i in range(0, 784)]
np_array = np.array(array).ravel().reshape(1, -1)

#Print image
for row in np_array:
    for cell in row:
        if cell == 0:
            print(cell, end = " ")
        else:
            print("\033[91m" + str(cell) + "\033[0m", end=" ")
    print(end ='\n')

print("Hello")
        
