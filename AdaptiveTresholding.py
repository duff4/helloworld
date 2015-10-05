from skimage import data, io, filter
from os import listdir, path, makedirs
from os.path import isfile, join, exists
from PIL import Image
import scipy.misc
import datetime

pathToTestImages = r"C:\Users\Davydov\PycharmProjects\helloworld\Test images"
pathToUpdatedImages = pathToTestImages + "\\AdaptiveThresholding\\" + datetime.datetime.utcnow().strftime("%m%d%H%M%S")

if not path.exists(pathToUpdatedImages):
    makedirs(pathToUpdatedImages)

fileNames = listdir(pathToTestImages)
print(fileNames)
for fileName in fileNames:
    if fileName.endswith('.jpg') or fileName.endswith('.png'):
        fullFileName = pathToTestImages + '\\' + fileName
        grayImage = Image.open(fullFileName).convert('L')
        grayImage = scipy.misc.fromimage(grayImage)
        updatedImage = filter.threshold_adaptive(grayImage, 30, offset=10)
        updatedImage = scipy.misc.toimage(updatedImage)
        updatedImage.save(pathToUpdatedImages + '\\' + fileName)