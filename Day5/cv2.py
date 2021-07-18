import cv2

import numpy as np

import sys

cap= cv2.Videocapture(0)

image1 = cv2.imread ('D:\\Python Programming\\OpenCV\\images\\background.jpg')

image2 = cv2.imread ('D:\\Python Programming\\OpenCV\\images\\background1.jpg')

option = input("enter : ")

while True:

    flag, frame=cap.read()

    if not flag:

        print("con not acess")

        break

    elif flag:            

            if option == 'a':

                imagi1= cv2.resize(image1,(frame.shape[1], frame.shape[0]))

                result = cv2.addWeighted(frame, 0.8, imagi1, 1, gamma=0.1 )

                cv2.imshow("new", result)

                if cv2.waitKey(10) & 0xFF == ord('c'):

                    sys.exit()

            elif option == 'b':

                imagi2= cv2.resize(image2,(frame.shape[1], frame.shape[0] ))

                result2 = cv2.addWeighted(frame, 0.8, imagi2, 1, gamma=0.1)

                cv2.imshow("neww", result2)

                if cv2.waitKey(10) & 0xFF == ord('b'):

                    sys.exit()

            else:

                print("try again")

cap.release()

cv2.destroyAllWindows()