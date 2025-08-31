import pyautogui
import time
import keyboard 

print("Move your mouse to see the RGB values. Press 'q' to quit.")


while True:
    if keyboard.is_pressed("q"):   # stop when 'q' is pressed
        print("\nStopped by user.")
        break
    
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    print(f"Position: ({x}, {y}) -> Color: {px}")
    break