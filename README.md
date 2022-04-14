# Mouse Tracking


If you want to track an element of a video but the resolution of the video is too bad, the colours change all the time or other factors make it difficult to use an automatic approach, then this code is for you. 

This code allows the user to track an element of a video using the mouse coordinates. The code presents the video fame by frame. At each frame, in a table is saved, the frame number, and the x-y-coordinate of the mouse at that specific frame. 

When launchine the code, two options appear. "Explore" launches the program the the corrdinates are only displayed (not saved). "Start" launches the program and saves every coordinates, and frame's number.


Change the filename in your code with the name of your video.
Put the video, the python code and the beb.wav fil in the same folder. 

## Libraries Required:

pyautogui --> to get the x-y coordinates \
tkinter --> for the buttons boxes (start, explore) \
keyboard --> To use the keyboard \
time --> To use the delay 'sleep' \
pygame --> To use the "beeb.wav" file \
cv2 --> To show each frames of the video \
numpy --> To save the data as .csv files 
