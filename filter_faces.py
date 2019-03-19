# import necessary packages
from imutils import paths
import face_recognition
import argparse
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of faces + images")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
                help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # show the processing image
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    # extract the person name from the image path
    name = imagePath.split(os.path.sep)[-2]

    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # detect the (x, y)-coordinates of the bounding boxes
    # corresponding to each face in the input image
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])

    # if can not detect the face
    if not boxes:
        print("[WARNING] Can't detect face on this image!")
        print("[INFO] This image will be delete...")
        print("[INFO] Deleting image...")
        # deleting this image
        os.remove(imagePath)
        print("[INFO] Image was deleted!")
        continue

    # loop over the recognized faces
    for (top, right, bottom, left) in boxes:
        # draw the predicted face name on the image
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # show the output image
    cv2.imshow(name, image)
    if cv2.waitKey(0) == ord('r'):
        print("[INFO] Deleting this image...")
        os.remove(imagePath)
        print("[INFO] Image was deleted!")
    else:
        print("[INFO] Continue...")
        continue
