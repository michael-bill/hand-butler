import cv2

def capture_video():
    """
    Captures video from webcam

    Raises:
        Exception: if could not open video device

    Returns:
        VideoCapture: video capture object
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    return cap

def show_video(cap):
    """
    Shows video from webcam. For test.

    Args:
        cap (VideoCapture): video capture object
    """
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def release_video(cap):
    """
    Ends video capture

    Args:
        cap (VideoCapture): video capture object
    """
    cap.release()
    cv2.destroyAllWindows()
