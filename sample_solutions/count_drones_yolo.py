from ultralytics import YOLO
import cv2
import os

import time

def process_video(video_path, model, output_video=False, output_path=None):
    cap = cv2.VideoCapture(video_path)
    frame_counts = []

    if not output_path:
        output_path = f"output_video.mp4"

    if output_video:
        output_video = cv2.VideoWriter(output_path, 
                                       cv2.VideoWriter_fourcc(*'mp4v'), 
                                       30.0, 
                                       (320, 320))

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Run YOLO tracking on the frame, persisting tracks across frames
        # The 'drones' class ID needs to be specified if you're using a custom model
        # For a generic model, it will track all objects it knows
        resized_frame = cv2.resize(frame, (320, 320))

        # results = counter(resized_frame)

        results = model.track(resized_frame, persist=True, show=False, conf=0.05)

        # print(results)
        
        # Get the boxes and track IDs
        boxes = results[0].boxes

        # Get the current frame's drone count (number of unique track IDs)
        drone_count = len(boxes)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        # Display the count on the frame
        cv2.putText(annotated_frame, f'Drone Count: {drone_count}', (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Write the frame to the output video
        if output_video:
            output_video.write(annotated_frame)
            
        frame_counts.append(drone_count)

        # Show the frame
        # cv2.imshow("YOLO Drone Counter", annotated_frame)
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture object and close display windows
    cap.release()
    if output_video:
        output_video.release()
    cv2.destroyAllWindows()

    return frame_counts

if __name__ == "__main__":
    # Get the absolute path of the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change the current working directory to the script's directory
    os.chdir(script_dir)

    model = YOLO("./yoloe-26s-seg.pt")

    start_time = time.time()

    print("Processing video...", " Start time:", start_time)
    print(time.time())

    video_path = "../sample solutions/Sample challenge 1 (muted).mp4"
    OUTPUT_PATH = f"output_video_yoloe-26s-seg.mp4"

    drone_counts = process_video(video_path, model, output_video=True, output_path=OUTPUT_PATH)

    end_time = time.time()

    print("DONE. Time elapsed:", end_time - start_time, "seconds")

    print(drone_counts)