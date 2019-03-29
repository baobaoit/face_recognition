# import the necessary packages
from imutils import paths
from random import randint
import argparse
import os
import shutil

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of faces + images")
ap.add_argument("-d", "--destination", required=True,
                help="path to store the examples")
args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
print("[INFO] getting faces...")
imagePaths = list(paths.list_images(args["dataset"]))
print("[INFO] there is {} faces in dataset!".format(imagePaths.__len__()))

# get name of face
print("[INFO] getting name of face...")
name = imagePaths[0].split(os.path.sep)[-2]
print("[INFO] name is {}".format(name))

# generate random index
randomIdx = randint(0, imagePaths.__len__() - 1)

# get random image path
print("[INFO] getting random image for examples...")
imagePath = imagePaths[randomIdx]

# set destination path
print("[INFO] setting destination path...")
destinationPath = args["destination"] + "\\" + os.path.basename(imagePath.rstrip(os.sep))

# copy file to destination path
print("[INFO] copying to destination path...")
shutil.copy(imagePath, destinationPath)
print("[INFO] copied!")
