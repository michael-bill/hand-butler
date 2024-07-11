import cv2
from src.capture import capture_video, release_video
from src.gesture_recognition import process_frame, get_distance, draw_landmarks
from src.volume_control import set_volume

def main():
    cap = capture_video()
    distance_range = (40, 400)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = process_frame(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    draw_landmarks(frame, hand_landmarks)
                    distance, thumb_coords, index_coords = get_distance(hand_landmarks, frame)

                    if distance_range[0] < distance < distance_range[1]:
                        norm_vulume = ((distance - distance_range[0]) / (distance_range[1] - distance_range[0]) * 10)
                        set_volume(norm_vulume)
                        print(f"volume changed to {norm_vulume}")

                    cv2.putText(frame, f'Distance: {int(distance)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        release_video(cap)

if __name__ == "__main__":
    main()
