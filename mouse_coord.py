import pyautogui as pg
import tkinter as tk
import keyboard
import time
import pygame
import cv2
import numpy as np

filename = 'filename'

frame_list = []
x_array = []
y_array = []
#i = 1 #frame number
i = 1
delay = 1/30

def beep():
    pygame.mixer.init()
    sounda= pygame.mixer.Sound("beep.wav")
    sounda.play()
    time.sleep(0.2)
    sounda.stop()


####################  EXPLORE  #######################

def explore():

    print('Type CRTL-C to stop the program.')

    try:

        #while True: #RETIRER ?

        while(cap.isOpened()):

            ret, frame = cap.read()

            if ret == True:

                
                cv2.imshow('Frame',frame)

            
                x, y= pg.position()

                
                ###############################

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                
                x, y= pg.position()

            

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)
             
                x, y= pg.position()

            
                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

            
                x, y= pg.position()

                

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

             
                x, y= pg.position()

                
                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

         
                x, y= pg.position()

         
                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

          
                x, y= pg.position()

           

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                x, y= pg.position()


                #################################

                coordinates  = 'X: ' + str(x).ljust(4) + 'Y: ' + str(y).ljust(4)

                print(coordinates, end = '')

                print('\b'*len(coordinates), end= '', flush = True)
                time.sleep(delay)

                if cv2.waitKey(25) & 0xFF == ord('a'):

                    while(cv2.waitKey(25) & 0xFF != ord('z')):
                        print('Pause')
                        time.sleep(1)


                if cv2.waitKey(25) & 0xFF == ord('p'):
                    print(i)

                    break


            else:

                break

        cap.release()

        cv2.destroyAllWindows()
        print('Frame numer is ' + str(len(frame_list)) + ' and, X array size is: ' + str(len(x_array)))

    except KeyboardInterrupt:
        print('\n End')
        print('X array size is: ' + str(len(x_array)))

####################  EXPLORE  #######################

def onclick():

    i = 1
    #i  = 60188

    time.sleep(1)
    beep()
    print(str(3))
    time.sleep(1)
    beep()
    print(str(2))
    time.sleep(1)
    beep()
    print(str(1))
    time.sleep(1)

    print('Type CRTL-C to stop the program.')

    try:

        #while True: #RETIRER ?

        while(cap.isOpened()):

            ret, frame = cap.read()

            if ret == True:

                
                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ###############################

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                ret, frame = cap.read()

                if ret == False:
                    break

                cv2.imshow('Frame',frame)

                frame_list.append(i)
                i += 1
                x, y= pg.position()

                x_array.append(x)
                y_array.append(y)

                

            

                #################################

                coordinates  = 'X: ' + str(x).ljust(4) + 'Y: ' + str(y).ljust(4)

                print(coordinates, end = '')

                print('\b'*len(coordinates), end= '', flush = True)
                time.sleep(delay)

                if cv2.waitKey(25) & 0xFF == ord('a'):

                    while(cv2.waitKey(25) & 0xFF != ord('z')):
                        print('Pause')
                        time.sleep(1)


                if cv2.waitKey(25) & 0xFF == ord('p'):
                    print(i)

                    break


            else:

                break

        cap.release()

        cv2.destroyAllWindows()
        print('Frame numer is ' + str(len(frame_list)) + ' and, X array size is: ' + str(len(x_array)))


        np.savetxt("x_coordinate.csv", x_array, delimiter=",")
        np.savetxt("y_coordinate.csv", y_array, delimiter=",")
        np.savetxt("frames.csv", frame_list, delimiter=",")


    except KeyboardInterrupt:
        print('\n End')
        print('X array size is: ' + str(len(x_array)))


cap = cv2.VideoCapture(filename)
     
    # Check if camera opened successfully

if (cap.isOpened()== False):

  print("Error opening video stream or file")


##################### Button to START ##########################

root = tk.Tk()

w = 100 # width for the Tk root
h = 50 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws) - (w)
y = (hs) - (h)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.title('GUI Button')

#btn = tk.Button(root, txt = 'Start', command=onclick)
btn = tk.Button(root, text = 'Start',command=onclick)
btn.place(x = 1300, y = 1300)

btn_explore = tk.Button(root, text = 'Explore',command=explore)
btn_explore.place(x = 1000, y = 1300)

btn.pack()
btn_explore.pack()

root.mainloop()
