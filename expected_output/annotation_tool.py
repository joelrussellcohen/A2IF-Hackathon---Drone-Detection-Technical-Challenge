import cv2
import sys

video_path = sys.argv[1] if len(sys.argv) > 1 else quit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
annotations = ["N/A"] * total_frames
current_idx = 0

def get_frame(idx):
    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ret, frame = cap.read()
    return frame if ret else None

# print("Controls: [0-3] Annotate | [Left/Right] Browse | [Backspace] Undo | [Enter] Finish")

while True:
    frame = get_frame(current_idx)
    if frame is None:
        break

    # Prepare display overlay
    display_frame = frame.copy()
    h, w, _ = display_frame.shape
    
    # Display previous 3 and current annotation
    for i in range(4):
        lookback_idx = current_idx - (3 - i)
        if lookback_idx >= 0:
            val = str(annotations[lookback_idx])
            color = (0, 255, 0) if i < 3 else (0, 0, 255) # Green for past, Red for current
            label = f"F{lookback_idx}: {val}"
            cv2.putText(display_frame, label, (10, 30 + (i * 30)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Completion prompt
    if "N/A" not in annotations:
        cv2.putText(display_frame, "PRESS ENTER TO COMPLETE", (w//4, h-50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

    cv2.imshow("Video Annotator", display_frame)
    
    # Use waitKeyEx to capture Arrow Keys
    key = cv2.waitKeyEx(0)

    if key in [ord('0'), ord('1'), ord('2'), ord('3')]:
        annotations[current_idx] = chr(key)
        if current_idx < total_frames - 1:
            current_idx += 1
    elif key == 8:  # Backspace
        if current_idx > 0:
            current_idx -= 1
    elif key == 2424832:  # Left Arrow (Windows/Linux code may vary)
        if current_idx > 0:
            current_idx -= 1
    elif key == 2555904:  # Right Arrow
        if current_idx < total_frames - 1:
            current_idx += 1
    elif key == 13:  # Enter
        if "N/A" not in annotations:
            break
    elif key == 27:  # Esc to quit early
        break

cap.release()
cv2.destroyAllWindows()

# print("\nFinal Annotation List:")
print(*annotations, sep=',')