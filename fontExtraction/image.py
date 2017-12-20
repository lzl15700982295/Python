import cv2
# ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# cv2.imwrite("thresh" + str(n) + ".jpg", thresh)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

gray1 = cv2.imread("./new/1.png", 0)
gray2 = cv2.imread("./new/2.png", 0)
gray3 = cv2.imread("./new/3.png", 0)
gray4 = cv2.imread("./new/4.png", 0)
gray5 = cv2.imread("./new/5.png", 0)

c = 0
for i in range(0, 2293, 116):
    for j in range(0, 1780, 89):
        c += 1
        temp = cv2.blur(cv2.resize(gray1[i+2:i+87, j+2:j+87], (150, 150)), (5,5))
        ret, thresh = cv2.threshold(temp, 200, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./result/" + str(c) + ".png", thresh)

for i in range(0, 2293, 116):
    for j in range(0, 1780, 89):
        c += 1
        temp = cv2.blur(cv2.resize(gray2[i+2:i+87, j+2:j+87], (150, 150)), (5,5))
        ret, thresh = cv2.threshold(temp, 200, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./result/" + str(c) + ".png", thresh)
#
for i in range(0, 2293, 116):
    for j in range(0, 1780, 89):
        c += 1
        temp = cv2.blur(cv2.resize(gray3[i+2:i+87, j+3:j+87], (150, 150)), (5,5))
        ret, thresh = cv2.threshold(temp, 200, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./result/" + str(c) + ".png", thresh)
#
for i in range(0, 2293, 116):
    for j in range(0, 1780, 89):
        c += 1
        temp = cv2.blur(cv2.resize(gray4[i+2:i+87, j+2:j+87], (150, 150)), (5,5))
        ret, thresh = cv2.threshold(temp, 200, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./result/" + str(c) + ".png", thresh)
#
for i in range(0, 2293, 116):
    for j in range(0, 1780, 89):
        c += 1
        temp = cv2.blur(cv2.resize(gray5[i+2:i+87, j+2:j+87], (150, 150)), (5,5))
        ret, thresh = cv2.threshold(temp, 200, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./result/" + str(c) + ".png", thresh)