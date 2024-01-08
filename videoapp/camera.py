import cv2
import threading
import cvlib as cv
from cvlib.object_detection import draw_bbox


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            raise ValueError(
                "Unable to access the camera. Check if it's connected properly."
            )
        self.grabbed, self.frame = self.video.read()
        self.thread = threading.Thread(target=self.update)
        self.thread.daemon = True  # Set as a daemon to stop when the main thread stops
        self.thread.start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        #bbox, label, conf = cv.detect_common_objects(image)
        #output_image = draw_bbox(image, bbox, label, conf)
        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()

    def update(self):
        while True:
            grabbed, frame = self.video.read()
            if not grabbed:
                break  # If unable to grab frames, break the loop
            self.frame = frame


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
