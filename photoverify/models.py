from __future__ import unicode_literals
import logging
logger = logging.getLogger(__name__)
import cv2, os

classifier_path = os.path.join(os.path.dirname(__file__), 'haarcascades', 'haarcascade_frontalface_default.xml')

def verify_image(imagePath):
    image = cv2.imread(imagePath)
    detector = cv2.CascadeClassifier(classifier_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(classifier_path)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    return faces
