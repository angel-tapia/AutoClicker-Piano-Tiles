import pyautogui
import numpy as np
import keyboard
import cv2
from PIL import ImageGrab,Image 

screenCoords = (515, 171, 783, 640)
column = [489, 572, 652, 742]

while True: 
    flag = False
    possible = False
    screen = ImageGrab.grab()
    screen_np = np.array(screen)
    screen_np = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    if(keyboard.is_pressed('q')):
        exit()
    '''x, y = pyautogui.position()
    print(x, y)
    print(screen_np[x][y])
    if keyboard.is_pressed('s'):
        screen.show()
        exit()
    '''
    for y in range(530, 173, -2):
        for x in column:
            if screen_np[y][x] <= 10 and screen_np[y-25][x]==screen_np[y][x]:
                pyautogui.click(x,y)
                flag = True
                break
            if(keyboard.is_pressed('q')):
                exit()
        if flag is True:
            break      




