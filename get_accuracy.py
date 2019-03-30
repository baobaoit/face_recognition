# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
                help="path to serialized db of facial encodings")
ap.add_argument("-t", "--examples", required=True,
                help="path to input input directory of faces + images example")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
                help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["examples"]))

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# getting list sub items
print("[INFO] getting list of sub items...")
subItemCounter = sum([len(item) for r, d, item in os.walk(args["examples"])])
print("[INFO] there are {} items".format(subItemCounter))

# initialize counter for right recognize face
rightRecognizeFace = 0

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # load the input image and convert it from BGR to RGB
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # get the true name of image through path
    name = str(imagePath).split("\\")[1].split(".")[0]

    # detect the (x, y)-coordinates of the bounding boxes corresponding
    # to each face in the input image, then compute the facial embeddings
    # for each face
    print("[INFO] recognizing faces {}/{}...".format(i + 1, subItemCounter))
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    encodings = face_recognition.face_encodings(rgb, boxes)

    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        recognizeName = "Unknown"

        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                recognizeName = data["names"][i]
                counts[recognizeName] = counts.get(recognizeName, 0) + 1

            # determine the recognized face with the largest number of
            # votes (note: in the event of an unlikely tie Python will
            # select first entry in the dictionary)
            recognizeName = max(counts, key=counts.get)

            if recognizeName == name:
                rightRecognizeFace += 1

# calculate percentage
print("[INFO] calculating percentage...")
percentage = (rightRecognizeFace / subItemCounter) * 100
print("[INFO] percentage is: {}%".format(percentage))
