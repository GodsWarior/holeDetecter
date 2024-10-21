import cv2 as cv
import time


def frameHandler(frame):
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray_frame, 100, 250)
    return edges


def videoLoader(Path):
    cap = cv.VideoCapture(Path)
    if not cap.isOpened():
        return None
    return cap


def usageForVideo(Path):
    cap = videoLoader(Path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        edges = frameHandler(frame)

        cv.imshow('Computer Vision', edges)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        if cv.waitKey(1) & 0xFF == ord('p'):
            run = True
            time.sleep(0.5)
            while run:
                if cv.waitKey(1) & 0xFF == ord('p'):
                    run = False

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    usageForVideo('videoTest1.mp4')
