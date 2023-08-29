from platform import python_branch
from sqlite3 import Row
import tkinter as tk
import clipboard
from colorama import Fore
import pyautogui
import webbrowser
import time

webbrowser.open('https://www.google.com.br/')
time.sleep (3)
extension_icon_x = 1420
extension_icon_y = 44
pyautogui.click(extension_icon_x, extension_icon_y)
time.sleep(2)
pyautogui.hotkey('tab')
pyautogui.write('288')
pyautogui.hotkey('tab')
pyautogui.write('@Glgamer1')
pyautogui.hotkey('Enter')


time.sleep (60)


pyautogui.hotkey('win', 'r')
pyautogui.write('shutdown -s -t 00')
pyautogui.hotkey('Enter')


