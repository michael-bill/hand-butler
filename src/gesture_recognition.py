import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def process_frame(frame):
    """
    Processes frame with mediapipe

    Args:
        frame (np.ndarray): frame

    Returns:
        np.ndarray: processed frame
    """
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    return results

def get_distance(hand_landmarks, frame):
    """
    Calculates distance between thumb and index fingers in frame

    Args:
        hand_landmarks: landmarks
        frame (np.ndarray): frame

    Returns:
        tuple: distance, thumb coords, index coords
    """
    h, w, _ = frame.shape
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
    index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
    distance = np.linalg.norm(np.array([thumb_x - index_x, thumb_y - index_y]))
    return distance, (thumb_x, thumb_y), (index_x, index_y)

def draw_landmarks(frame, hand_landmarks):
    """
    Draws landmarks on frame

    Args:
        frame (np.ndarray): frame
        hand_landmarks: landmarks
    """
    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
