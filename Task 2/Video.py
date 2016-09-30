'''
Task 2 - Video Read and Write


#VideoCapture(DeviceIndex)

Video read is a simple task and requires no external resources. The argument to the VideoCapture object determines which
camera/video file you intend to use in your application.

Device Indices:
0 -> Refers to the primary camera/webcam.
1 -> Refers to the secondary camera/webcam.
...
<file_path> -> Refers to a video file you are trying to open.


#VideoWrite(Path, FOURCC, frameRate, frameSize, isColor)

Video write is a bit more complicated as you need to specify the video codec for your system. The other arguments are simply the
file path, frame rate, frame size and the isColor variable to indicate if the frame is in color or not.

In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
In Windows: DIVX
In OSX: MJPG
'''
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('result.avi', fourcc, 20.0, (640,480), False)

while(True):
    flag, frame = capture.read()

    if not flag:
        exit(1)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    output.write(grayFrame)

    cv2.imshow('Result', grayFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
output.release()
cv2.destroyAllWindows()