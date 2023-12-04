import cv2 as cv
import matplotlib.pyplot as plt
import easyocr


def read_plate(bounds, img_path):

    # Limits easyocr characters it can read
    characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    img = cv.imread(img_path)

    H, W, _ = img.shape

    # plot
    reader = easyocr.Reader(['en'], verbose=False)
    xc, yc, w, h = bounds

    # creates a new image of just the license plate
    license_plate = img[int(yc - (h / 2)):int(yc + (h / 2)), int(xc - (w / 2)):int(xc + (w / 2)), :].copy()

    # Draws a rectangle around the license plate in the original image
    img = cv.rectangle(img,
                        (int(xc - (w / 2)), int(yc - (h / 2))),
                        (int(xc + (w / 2)), int(yc + (h / 2))),
                        (0, 255, 0),
                        15)

    # converts image into greyscale and threshold for easy ocr to read
    license_plate_gray = cv.cvtColor(license_plate, cv.COLOR_BGR2GRAY)
    _, license_plate_thresh = cv.threshold(license_plate_gray, 100, 255, cv.THRESH_BINARY)


    output = reader.readtext(license_plate_thresh, allowlist=characters)

    possible_plates = []
    for out in output:
        text_bbox, text, text_score = out
        # if confidence score is over 80% then accept as a possible plate number
        if text_score > 0.8:
            # print(text, text_score)
            print(text)
            possible_plates.append(text.replace(" ", ""))

    # plotting pictures to show if it found license plate and what the easyocr sees when it runs its code

    # plt.figure()
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    # plt.figure()
    # plt.imshow(cv.cvtColor(license_plate_thresh, cv.COLOR_BGR2RGB))

    # plt.show()

    return possible_plates