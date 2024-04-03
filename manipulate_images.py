from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from functools import cache
import glob
import os
import random

# using PyPy as the "interpreter" would be much faster but numpy is currently experimental
# using the cache decorator should also speed things up, will be implemented later

class manipulateImage:
    def __init__(self, path_to_image: str):
        self.x = Image.open(path_to_image)
        self.black = Image.new(mode="RGB", size=self.x.size)

    # @cache
    def RGBAtoL(self, x: Image) -> Image:
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


    def excluded_random(self, min: int, max: int) -> float:
        '''
        gives a random number between min and max but does not give a number between min+0.5 and max-0.5
        so we do not get similar looking images
        '''
        x = random.random()
        if x <= 0.5:
            return x+min
        else:
            return x+max-1

    def blur(self, x: Image = None, use_noise: bool = False) -> Image:
        x = x or self.x
        b = x.filter(ImageFilter.BoxBlur(random.randint(3, 7)))
        if use_noise:
            noise_texture = Image.open(r"Noise Textures (L)\\" + random.choice(os.listdir("Noise Textures (L)")))
            b = Image.composite(x, b, noise_texture)
        return b

    def exposure(self, x: Image = None, use_noise: bool = False) -> Image:
        x = x or self.x
        exposure = ImageEnhance.Brightness(x)
        e = exposure.enhance(self.excluded_random(0.3, 1.7))
        if use_noise:
            noise_texture = Image.open(r"Noise Textures (L)\\" + random.choice(os.listdir("Noise Textures (L)")))
            e = Image.composite(x, e, noise_texture)
        return e

    # * had to run only once
    def handle_noise_textures(self, dir_target: str, dir_source: str) -> None:
        os.mkdir(dir_target)
        for i, textures in enumerate(glob.glob(dir_source + "Untitled.*.png")):
            y = Image.open(textures)
            y = y.resize(size=self.x.size)
            y = self.RGBAtoL(y)
            t = dir_target + r"\Texture" + str(i) + ".png"
            y.save(t)

if __name__ == '__main__':
    d = manipulateImage("D:\Wallpapers\RE4wB6A.jpg")
    q = Image.open("D:\Wallpapers\RE4wppZ.jpg")
    e = d.exposure(q)
    e.show()
    e = d.exposure(q, use_noise=True)
    e.show()
    e = d.blur(q)
    e.show()
    e = d.blur(q, use_noise=True)
    e.show()