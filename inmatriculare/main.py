from sys import argv
import cv2
import imutils
import numpy
import pytesseract


def main():
    img = cv2.imread(argv[1])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.bilateralFilter(gray, 13, 15, 15)
    edged = cv2.Canny(gray, 30, 200)

    outline = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    outline = imutils.grab_contours(outline)
    outline = sorted(
        outline,
        key=cv2.contourArea,
        reverse=True
    )[:10]

    screen_cnt = None
    for c in outline:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            screen_cnt = approx
            break

    if screen_cnt is None:
        print('Coult not find any outline')

    mask = numpy.zeros(gray.shape, numpy.uint8)
    cv2.drawContours(mask, [screen_cnt], 0, 255, -1)
    cv2.bitwise_and(img, img, mask=mask)
    x, y = numpy.where(mask == 255)
    crop = gray[
        numpy.min(x) :
        numpy.max(x) + 1,
        numpy.min(y) :
        numpy.max(y) + 1
    ]

    text_numar = pytesseract.image_to_string(crop, config='--psm 10')
    print('Detected registration plate number: ', text_numar)

    img = cv2.resize(img, (500, 300))
    crop = cv2.resize(crop, (400, 200))

    cv2.imshow('Crop', crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
