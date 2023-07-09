# Object-Tracking-and-Positioning-System-Based-on-Vision
## System Main Functions
1. **Pedestrian Detection**: The system should accurately detect all pedestrian targets in the input video.
2. **Multi-Target Pedestrian Tracking**: The system should perform multi-target pedestrian tracking in consecutive video frames based on pedestrian detection results.
3. **Real-time Pedestrian Counting**: The system should provide real-time statistics on the number of pedestrians detected during multi-target pedestrian tracking and display it on the interface.
4. **Target Pedestrian Re-identification**: The system should accurately identify the same target pedestrian selected by the user across different scenes and times using pedestrian re-identification models, enabling cross-camera pedestrian identity recognition.
5. **Pedestrian Motion Trajectory Drawing**: The system should accurately draw the motion trajectory of pedestrians by utilizing pedestrian localization and tracking.
6. **Setting Trajectory Drawing Length**: Users can customize and adjust the length of the pedestrian motion trajectory to display trajectories during different time periods.
7. **Setting Detection Box Size**: Users can customize and adjust the size of the pedestrian detection box to accommodate pedestrian sizes in different scenes.
8. **Setting Pedestrian Detection Confidence**: Users can customize and adjust the confidence threshold for pedestrian detection to control the accuracy and sensitivity of the detection results.
9. **Setting Pedestrian Detection Intersection over Union (IoU)**: Users can customize and adjust the IoU threshold for pedestrian detection to control the matching degree of pedestrian detection boxes.
10. **Real-time Display of Frame Rate (FPS)**: The system should provide a real-time display of the current frame rate at which the system is operating, allowing performance monitoring and evaluation.
11. **Reading Detection Video Stream**: The system should allow the import of local videos or the connection of IP cameras to edge devices to obtain video frames for detection.
12. **Managing Detection Process**: The system should allow users to pause, resume, or play the pedestrian detection process.

## System Workflow
The workflow of this system is as follows:

1. Initialize the system, load the PySide2 interface, and load necessary models such as pedestrian detection, pedestrian tracking, and pedestrian re-identification models.
2. Choose the system mode:
   - **Multi-Target Tracking Mode**: Use YOLOv5 and DeepSORT for multi-target pedestrian detection and tracking.
   - **Pedestrian Re-identification Mode**: Use YOLOv5 and a pedestrian re-identification model (such as ResNet50) to track the selected target pedestrian.

### Multi-Target Tracking Mode:
1. Import local videos or connect IP cameras to edge devices to obtain video frames for detection.
2. Pedestrian Detection: Perform pedestrian detection using the YOLOv5 model and obtain bounding boxes for pedestrians.
3. Pedestrian Tracking: Perform pedestrian tracking using the DeepSORT model and associate each pedestrian's ID with its corresponding bounding box.
4. Draw Target Motion Trajectories: Draw the motion trajectories of pedestrians by connecting their historical positions.
5. Real-time statistics on the number of detected pedestrians in multi-target tracking.
6. Display the results of detection, tracking, trajectory drawing, and pedestrian counting on the system interface.
7. Perform different operations based on user requirements, such as pausing detection, terminating detection, resuming detection, reimporting detection videos, or switching modes.
![img1](https://github.com/shenllyz/Object-Tracking-and-Positioning-System-Based-on-Vision/assets/102724218/2de5a0e1-b56d-46b0-85af-0b7e7cf50ce5)
### Pedestrian Re-identification Mode:
1. Import target pedestrian images locally.
2. Import local videos or connect IP cameras to edge devices to obtain video frames for detection.
3. Pedestrian Detection: Perform pedestrian detection using the YOLOv5 model and obtain bounding boxes for pedestrians.
4. Target Pedestrian Tracking: Track the selected target pedestrian using a pedestrian re-identification model.
5. Draw Target Motion Trajectories: Draw the motion trajectories of the target pedestrian by connecting their historical positions.
6. Display the results of detection, re-identification, and trajectory drawing on the system interface.
7. Perform different operations based on user requirements, such as pausing detection, terminating detection, resuming detection, reimporting detection videos, or switching modes.
![img2](https://github.com/shenllyz/Object-Tracking-and-Positioning-System-Based-on-Vision/assets/102724218/177cc9b5-8801-48c2-88ee-bc84c26393db)
# Reference/Credits
