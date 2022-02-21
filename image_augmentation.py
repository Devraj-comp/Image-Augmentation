from PIL import Image
import os
import skimage
import numpy as np
import imgaug.augmenters as iaa



class Augmentation:
    def __init__(self, inPath):
        self.inPath = inPath

    # DARK AUGMENTAION
    def dark_augment(self, outPath, gamma, gain):
        for imagePath in os.listdir(self.inPath):
            inputPath = os.path.join(self.inPath, imagePath)
            img = np.asarray(Image.open(inputPath))

            ski_img = Image.fromarray(skimage.exposure.adjust_gamma(img, gamma, gain))
            finalPath = os.path.join(outPath, 'invert_' + imagePath)
            ski_img.save(finalPath)
        return ski_img

    # BRIGHT AUGMENTAION
    def bright_augment(self, outPath, gamma, gain):
        for imagePath in os.listdir(self.inPath):
            inputPath = os.path.join(self.inPath, imagePath)
            img = np.asarray(Image.open(inputPath))
            
            ski_img = Image.fromarray(skimage.exposure.adjust_gamma(img, gamma, gain))
            finalPath = os.path.join(outPath, 'bright_' + imagePath)
            ski_img.save(finalPath)
        return ski_img


    # MOTION BLUR
    def motion_blur(self, outPath, k, angle):
        for imagePath in os.listdir(self.inPath):
            inputPath = os.path.join(self.inPath, imagePath)
            img = np.asarray(Image.open(inputPath))

            auge = iaa.MotionBlur(k, angle)
            motion_blurimg = Image.fromarray(auge(image=img))
            finalPath = os.path.join(outPath, 'blur_' + imagePath)
            motion_blurimg.save(finalPath)

        return motion_blurimg
        
    # FOGGY IMAGES
    def foggy(self, outPath):
        for imagePath in os.listdir(self.inPath):
            inputPath = os.path.join(self.inPath, imagePath)
            img = np.asarray(Image.open(inputPath))
            
            auge = iaa.Fog(250)
            foggy_img = Image.fromarray(auge(image=img))
            finalPath = os.path.join(outPath, 'foggy_' + imagePath)
            foggy_img.save(finalPath)

        return foggy_img
    
    # SNOWFLAKES
    def snow_flake(self, outPath, flake_size, speed):
        for imagePath in os.listdir(self.inPath):
            inputPath = os.path.join(self.inPath, imagePath)
            img = np.asarray(Image.open(inputPath))
            
            auge = iaa.Snowflakes(flake_size, speed)
            snowy_img = Image.fromarray(auge(image=img))
            finalPath = os.path.join(outPath, 'invert_' + imagePath)
            snowy_img.save(finalPath)

        return snowy_img

if __name__ == "__main__":
    darks = Augmentation('input_images') #provide input data path
    darks.dark_augment('output_images/dark_images',gamma=3, gain=1) #provide output data path
    darks.bright_augment('output_images/bright_images',gamma=0.3, gain=1)
    darks.motion_blur('output_images/motionblur_images', k=13, angle=45)
    darks.snow_flake('output_images/snowy_images',flake_size=0.2, speed=0.05)
    darks.foggy('output_images/foggy_images')
