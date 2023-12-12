import cv2 as cv
from reader import read_plate
from roboflow import Roboflow
from finder import find_plate
import db_search
from popup import Popup
from PyQt5 import QtWidgets
import sys


def main():

    # License plate recognition model
    rf = Roboflow(api_key="wHc4MvTyretYQy00UxqU")
    project = rf.workspace().project("yolov7-license-plate-detection")
    model = project.version(3).model

    running = True
    count = -1
    # Currently a video but would be the camera capture
    vidcap = cv.VideoCapture('pics/carvid.MOV')
    success, img = vidcap.read()
    app = QtWidgets.QApplication(sys.argv)

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
        for num in numbers:
            in_db = db_search.search(num)
            print(f"{'db search: '}{in_db}")
            if len(in_db) == 0:
                poppy = Popup(num)
                poppy.show()
                app.exec_()

            elif in_db[0][3] != "Student":
                pop2 = Popup(in_db[0])
                pop2.show()
                app.exec_()


if __name__ == "__main__":
    main()