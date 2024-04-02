from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from functools import cache
import glob
import os
import pickle
import random

# using PyPy as the "interpreter" would be much faster but numpy is currently experimental
# using the cache decorator should also speed things up, will be implemented later


# @cache
def RGBAtoL(x: Image) -> Image:
    '''
    function to convert an RGBA PIL mode image to 1 PIL mode image
    '''
    im = []
    y = np.asarray(x)
    for i in y:
        one_row = []
        for j in i:
            if j[0] == 0 and j[1] == 0 and j[2] == 0:
                one_row.append(False)
            else:
                one_row.append(True)
        im.append(one_row)
    im = np.asarray(im)
    return Image.fromarray(im)

x = Image.open("D:\Wallpapers\RE4wB6C.jpg")
black = Image.new(mode="RGB", size=x.size)

def blur(x: Image, use_noise: bool = False) -> Image:
    if not use_noise:
        x = x.filter(ImageFilter.BoxBlur(random.randint(3, 7)))
    else:
        noise_texture = Image.open(r"Noise Textures (L)\\" + random.choice(os.listdir("Noise Textures (L)")))
        x = Image.composite(x, black, noise_texture)
        x = x.filter(ImageFilter.BoxBlur(random.randint(3, 7)))
    return x

def exposure(x: Image, use_noise: bool = False) -> Image:
    if not use_noise:
        exposure = ImageEnhance.Brightness(x)
        x = exposure.enhance(random.randint(1, 3)/2)
    else:
        noise_texture = Image.open(r"Noise Textures (L)\\" + random.choice(os.listdir("Noise Textures (L)")))
        x = Image.composite(x, black, noise_texture)
        exposure = ImageEnhance.Brightness(x)
        x = exposure.enhance(random.randint(1, 3)/2)
    return x

#* had to run only once
# os.mkdir(r"C:\Users\lenovo\Desktop\code\cunning\Noise Textures (L)")
# for i, textures in enumerate(glob.glob("C:\\Users\\lenovo\\Desktop\\code\\cunning\\Noise Textures\\Untitled.*.png")):
#     y = Image.open(textures)
#     y = y.resize(size=x.size)
#     y = RGBAtoL(y)
#     t = r"C:\Users\lenovo\Desktop\code\cunning\Noise Textures (L)" + r"\Texture" + str(i) + ".png"
#     y.save(t)