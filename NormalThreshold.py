import cv2


img=cv2.imread(r'D:\ROS Assignment\Open CV\Threshold\OldNewsPaper.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)

gaussian_blur=cv2.GaussianBlur(gray,(11,11),5)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)

T, simple_thres =cv2.threshold(gaussian_blur, 95, 95, cv2.THRESH_BINARY)
cv2.imshow("Threshold", simple_thres)
cv2.imwrite("simple.jpg", simple_thres)
cv2.waitKey(0)