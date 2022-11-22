# 파이썬 패키지 
import math
import cv2

# 그림 속 원 검출
src1 = cv2.imread("/Users/ijeongseog/Downloads/moon.jpg")
dst1 = src1.copy()
gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100,
                            param1 = 300, param2 = 30, minRadius = 20, maxRadius= 100)
# 검출된 원 그리기
for circle in circles[0]:
    x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
    cv2.circle(dst1, (x,y),r, (123,42,78), 3)


# 그림 속 선 검출
canny = cv2.Canny(gray, 5000, 3000, apertureSize=5, L2gradient= True)
lines = cv2.HoughLinesP(canny, 0.9, math.pi/180, 45, minLineLength=10, maxLineGap=100)

print('Number of detected lines =', len(lines))

# 선 그리기
for i in lines:
   cv2.line(dst1, (int(i[0] [0]), int(i[0] [1])), (int(i[0] [2]), int(i[0] [3])), (0,255,255), 2)

#화면에 출력
cv2.imshow("Detected", dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()