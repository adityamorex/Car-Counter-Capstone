# Capstone Project: Real-Time Vehicle Counter with Computer Vision

![Car Counter](https://github.com/ansh-sharmaa/Car-Counter/assets/126788870/8ed6b35c-2802-4854-8f7b-6747f156d95e)

## Overview

The real-time vehicle counter project employs computer vision techniques, utilizing YOLO (You Only Look Once) object detection and SORT (Simple Online and Realtime Tracking) algorithm to detect, track, and count vehicles in video streams. It accurately identifies cars, trucks, buses, and motorbikes while showcasing the count in real-time on the video feed.

### Features

- **Object Detection:** Utilizes the YOLO (You Only Look Once) model, specifically YOLOv8, to perform accurate and efficient identification and classification of various types of vehicles, such as cars, trucks, buses, and motorbikes within video streams.

- **Real-Time Tracking:** Employs the SORT (Simple Online and Realtime Tracking) algorithm, a sophisticated tracking technique that enables the system to maintain the identity of vehicles across frames in real-time, ensuring accurate and consistent tracking throughout the video feed.

- **Counting Logic:** Implements a robust counting logic that accurately counts vehicles as they cross a predefined line or region of interest (ROI) in the video, providing precise and reliable vehicle count statistics.

- **Visualization:** Offers a user-friendly interface that displays the ongoing vehicle count in real-time directly overlaid on the video feed, allowing users to visualize and monitor the count as vehicles are detected and tracked.

- **Customization:** Provides flexibility and configurability in adjusting various parameters related to both detection and tracking, enabling users to fine-tune settings according to specific requirements, such as confidence thresholds, tracking precision, or ROI adjustments.

- **Performance:** Optimized for real-time processing, ensuring swift and efficient processing of video streams while maintaining high accuracy in vehicle detection, tracking, and counting. The system aims to strike a balance between speed and precision, delivering accurate results in real-time scenarios.


## Prerequisites

To run this project, ensure you have:

- Python 3.x
- OpenCV
- NumPy
- Ultralytics YOLOv8
- SORT algorithm
- Pre-trained YOLO model and corresponding configuration files
- Video input source

## Setup

1. Clone/download this project repository.
2. Install required Python libraries and dependencies via pip.
3. Download the pre-trained YOLO model and configuration files.
4. Specify paths to the YOLO model, configuration, video source, etc., in the code.

## Usage

1. Run the Python script to initiate real-time vehicle counting.
2. The application processes the video source, detects, tracks vehicles, and displays the count in real-time.
3. Adjust parameters like confidence thresholds or tracking settings if needed.

## Configuration

- **model:** Path to pre-trained YOLO model and configuration files.
- **classNames:** Class names for object detection (e.g., "car," "truck," "bus," "motorbike").
- **mask:** Load a mask image to define the region of interest (ROI) for vehicle counting.
- **tracker:** Configure SORT tracking parameters (maximum age, minimum hits).
- **limits:** Set line coordinates for counting vehicles crossing a specific point in the video.

## JIRA Timeline

[JIRA Timeline](https://adityamore.atlassian.net/jira/software/projects/OBJ/boards/1/timeline)

## Results

- Video stream displays bounding boxes around detected vehicles.
- Real-time update of vehicle count on the video feed.
- Tracking and display of vehicle identities.

## Acknowledgments

- Ultralytics for YOLO framework.
- Alex Bewley for SORT tracking algorithm.

## License

This project is open-source and available under the MIT License.
