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

time.sleep(15)

target_color_black = (0, 0, 0)

while True: 
    screenshot = pyautogui.screenshot()

    pixel_color_1 = screenshot.getpixel((531, 565))
    pixel_color_2 = screenshot.getpixel((628, 565))
    pixel_color_3 = screenshot.getpixel((716, 570))
    pixel_color_4 = screenshot.getpixel((808, 574))

    if pixel_color_1 == target_color_black:
        pyautogui.moveTo(531, 565)
        pyautogui.click()
        time.sleep(0.00001)

    if pixel_color_2 == target_color_black:
        pyautogui.moveTo(628, 565)
        pyautogui.click()
        time.sleep(0.00001)

    if pixel_color_3 == target_color_black:
        pyautogui.moveTo(716, 570)
        pyautogui.click()
        time.sleep(0.00001)

    if pixel_color_4 == target_color_black:
        pyautogui.moveTo(808, 574)
        pyautogui.click()
        time.sleep(0.00001)

    if keyboard.is_pressed('q'):
        print("Exiting script...")
        break