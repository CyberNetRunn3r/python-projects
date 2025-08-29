import pyautogui
import time
import keyboard

target_color_green = (75, 219, 106)
target_color_blue = (43, 135, 209)

while True: 
        if keyboard.is_pressed("q"):
             print("stopped by user")
             break
        
        x, y = pyautogui.position()
        px = pyautogui.pixel(x, y)

        if px == target_color_blue:
            pyautogui.click()

        elif px == target_color_green:
            pyautogui.click()


 