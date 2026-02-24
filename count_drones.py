# Sample solution
# This solution 

import cv2
import numpy as np
from sys import argv
import argparse
import os

from ultralytics import YOLO

if __name__ == "__main__":
    # Change current working directory to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

from sample_solutions.count_drones_yolo import process_video

model = YOLO("./sample_solutions/yoloe-26s-seg.pt")


def extract_frame_count(video_path):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return total_frames

def process_video_1(input_path):
    video = cv2.VideoCapture(input_path)
    total_frames = extract_frame_count(input_path)
    print(process_video(input_path, model=None, output_video=False))

def process_video_2(input_path):
    video = cv2.VideoCapture(input_path)
    total_frames = extract_frame_count(input_path)
    print(process_video(input_path, model=None, output_video=False))

def process_video_3(input_path):
    video = cv2.VideoCapture(input_path)
    total_frames = extract_frame_count(input_path)
    print(process_video(input_path, model=None, output_video=False))





if __name__ == "__main__":
    # Create the ArgumentParser object
    parser = argparse.ArgumentParser(description="A script using argparse with flags.")

    # An optional argument (flag): "--verbose" or "-v"
    parser.add_argument(
        "-i1",
        "--input1",
        help="The path of the first input video file."
    )

    parser.add_argument(
        "--input2",
        "-i2",
        help="The path of the second input video file."
    )

    parser.add_argument(
        "--input3",
        "-i3",
        help="The path of the third input video file."
    )

    args = parser.parse_args()

    if args.input1:
        process_video_1(args.input1)

    if args.input2:
        process_video_2(args.input2)

    if args.input3:
        process_video_3(args.input3)
