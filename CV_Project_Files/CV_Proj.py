#Computer Vision Semester Project 
#Project Driver Drowsiness Detection
#Project Nickname:  "Project Ai" (Project Active informer)
#Developed by M033, M031, M047

# Image processing functions
import cv2
# Mathematics and Array functions
import numpy as np
# Face and landmark detection
import dlib
#face_utils for basic operations of conversion
from imutils import face_utils

def GetEucDist(A,B):
	EucDist = np.linalg.norm(A - B)
	return EucDist

def ProcessEyeData(L,S1,S2,s1,s2,l):
	SumEyeShortDist = GetEucDist(S1,s1) + GetEucDist(S2,s2)
	EyeLongDist = GetEucDist(L,l)
	ratio = SumEyeShortDist/(2.0*EyeLongDist)
    
	#Checking if it is blinked
	if(ratio>0.25):
		return 2 #Active Flag
	elif(ratio>0.21 and ratio<=0.25):
		return 1 #Drowsy Flag
	else:
		return 0 #Sleepy Falg

def GetArray (landmarks):
    array = face_utils.shape_to_np(landmarks)
    return array

def PrintText (Frame,Msg,Color):
    cv2.putText(Frame, Msg, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, Color,3)

# Capturing the video
cap = cv2.VideoCapture(0)

# Face  and landmark detector
DetectFace = dlib.get_frontal_face_detector()
PredictLandmarks = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Status and Notification Variables
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)
FaceFrame = 0;

while True:
    _, frame = cap.read()
    GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    FaceArray = DetectFace(GrayFrame)
    for face in FaceArray:
        Lboundary = face.left()
        Tboundary = face.top()
        Rboundary = face.right()
        Bboundary = face.bottom()

        # saving frame for later use
        FaceFrame = frame.copy()
        cv2.rectangle(FaceFrame, (Lboundary, Tboundary), (Rboundary, Bboundary), (0, 255, 0), 2)

        landmarks = PredictLandmarks(GrayFrame, face)
        landmarks = GetArray(landmarks)

        # Sending the landmarks of each eye seperately and carefully based on Landmark Indeces
        LeftEyeResult = ProcessEyeData(landmarks[36],landmarks[37], 
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        
        RightEyeResult = ProcessEyeData(landmarks[42],landmarks[43], 
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        # Set Notification variables as per flag results
        if(LeftEyeResult==0 or RightEyeResult==0):
        	sleep+=1
        	drowsy=0
        	active=0
        	if(sleep>6):
        		status="Dont SLEEP!"
        		color = (0,0,255)

        elif(LeftEyeResult==1 or RightEyeResult==1):
        	sleep=0
        	active=0
        	drowsy+=1
        	if(drowsy>6):
        		status="Drowsy!"
        		color = (255,0,0)

        else:
        	drowsy=0
        	sleep=0
        	active+=1
        	if(active>6):
        		status="Active :)"
        		color = (0,255,0)
        	
        # Notify the results on the frame
        PrintText(frame,status,color)

        # Indication 68 unique Landmarks on Frame using CV2
        for n in range(0, 68):
        	(x,y) = landmarks[n]
        	cv2.circle(FaceFrame, (x, y), 1, (255, 255, 255), -1)
    
    # Show marked Landmarks on cam instance
    cv2.imshow("Result of detector",FaceFrame)
    
    #Show Notified use frame on cam instance
    cv2.imshow("Frame", frame)
    
    # Press ESC key to quit the program
    key = cv2.waitKey(1)
    if key == 27:
      	break