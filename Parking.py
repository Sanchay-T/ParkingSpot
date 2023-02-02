import cv2
import pickle

# h = 157-50 , w = 240-192
width, height = 107, 48

try:
    with open("storedPositions", 'rb') as f:
        finalPositions = pickle.load(f)
except:
    finalPositions = []


def mouseClick(click, x, y, *args, **kwargs):
    if click == cv2.EVENT_LBUTTONDOWN:
        finalPositions.append((x, y))
    if click == cv2.EVENT_RBUTTONDOWN:
        for index, position in enumerate(finalPositions):
            x1, y1 = position
            if x1 < x < x1 + width and y1 < y < y1 + height:
                finalPositions.pop(index)
    with open("storedPositions", "wb") as f:
        pickle.dump(finalPositions, f)


while True:
    image = cv2.imread('Demo.png')

    for initialPosition in finalPositions:
        cv2.rectangle(image, initialPosition, (initialPosition[0] + width, initialPosition[1] + height), (0, 0, 255), 2)

    cv2.imshow("window1", image)
    cv2.setMouseCallback("window1", mouseClick)
    cv2.waitKey(1)
