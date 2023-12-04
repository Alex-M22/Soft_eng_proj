import cv2 as cv
from reader import read_plate
from roboflow import Roboflow
from finder import find_plate


def main():

    # License plate recognition model
    rf = Roboflow(api_key="QlNTkXMtD5ifeiNhia0A")
    project = rf.workspace().project("yolov7-license-plate-detection")
    model = project.version(3).model

    running = True
    count = -1
    # Currently a video but would be the camera capture
    vidcap = cv.VideoCapture('pics/carvid.MOV')
    success, img = vidcap.read()

    # Continuously running until video ends/camera is turned off
    while(running):
        count += 1
        # Grabs frame from video and reads next frame
        cv.imwrite("frame.jpg", img)
        success, img = vidcap.read()

        # If it cannot read a frame then end 
        if not success:
            running = False

        # Skip 20 frames to limit amount of processing needing to be done
        if count % 20 != 0:
            continue

        # Find plate location in picture, returns array for location
        b = find_plate(model, "frame.jpg")
        # if no license plate is found then go to next frame
        if b == None:
            continue
        # Words/characters returned from reader 
        numbers = read_plate(b, "frame.jpg")








main()