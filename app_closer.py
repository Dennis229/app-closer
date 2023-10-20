import keyboard
import pyautogui
import time
import webbrowser
import os
import psutil

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))

#check if chrome run
def chrome_running():
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] =='chrome.exe':
            return True
    return False

if chrome_running():
    keyboard.add_hotkey("AltGr", lambda: os.system('taskkill /im chrome.exe /f'))
    keyboard.wait()
  
else:
    print("Chrome is not running")