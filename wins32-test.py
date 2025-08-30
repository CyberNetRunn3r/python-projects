from pyautogui import *
import pyautogui
import win32api, win32con
import time
import keyboard
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import pyautogui
import time
import keyboard

# Corrected the usage of add_experimental_option
options = Options()
options.add_experimental_option("detach", True)

# Create a new Chrome driver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the game page
driver.get("https://www.spelletjes.nl/spel/magische-pianotegels#gameinfo")
driver.maximize_window()

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(536, 442) [0] == 0:
        click(536, 442)
    if pyautogui.pixel(629, 442) [0] == 0:
        click(629, 442)
    if pyautogui.pixel(733, 442) [0] == 0:
        click(733, 442)
    if pyautogui.pixel(819, 442) [0] == 0:
        click(819, 442)