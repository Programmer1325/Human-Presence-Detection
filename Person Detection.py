import cv2, time

Face_Cascade = cv2.CascadeClassifier('Upper_Body_Set.xml')

VidCapture = cv2.VideoCapture(0)

while True:
    time.sleep(5)
    _, Frame = VidCapture.read()

    GrayscaleImage = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    Faces = Face_Cascade.detectMultiScale(GrayscaleImage, 1.01, 6)

    if len(Faces) > 0:
        print("In Seat")
    else:
        print("Not in Seat")


    Keypress = cv2.waitKey(30) & 0xff
    if Keypress == 27:
        break

VidCapture.release()
