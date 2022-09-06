# CV_Drowsiness_Detection

This repository hosts a Computer Vision Project that detects drowsiness in drivers using OpenCV and Python. 
The project is divided into 3 parts:
1. Detecting facial landmarks using dlib's pre-trained facial landmark detector.
2. Computing the Eye Aspect Ratio (EAR) to quantify eye closure.
3. Detecting drowsiness by monitoring EAR values over time.

## Dependencies
The project requires the following dependencies:
1. Python 3.6
2. OpenCV 3.4.2
3. dlib 19.16.0
4. imutils 0.5.2
5. numpy 1.15.4


## Project Setup
You need to install Dlib and CMake library for running .DAT File. Only then, project will be runnable.
For installing Dlib, follow the steps given below:
1. Open Command Prompt
2. Type "pip install cmake" and press enter
3. Type "pip install dlib" and press enter

## Project Run
After installing all the dependencies, you can run the project in PyCharm.

## Project Output
1. If you are using a laptop, you will see a window with a camera feed. If you are using a desktop, you will see a window with a camera feed.
2. If you are using a laptop, you can use the "Q" key to quit the program.
3. If you are using a desktop, you can use the "Esc" key to quit the program.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.