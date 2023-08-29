import pyautogui
import time
import webbrowser




extension_icon_x = 40
extension_icon_y = 128



#codigo para limpeza de disco 

#pyautogui.hotkey('win', 'r')
#pyautogui.write ('temp')
#pyautogui.hotkey('enter')
#time.sleep(3)
#pyautogui.hotkey('ctrl', 'a')
#time.sleep(3)
#pyautogui.hotkey('win', 'd')
#pyautogui.write ('%temp%')
#pyautogui.hotkey('enter')
#time.sleep(2)
#pyautogui.hotkey('ctrl', 'a')
#pyautogui.hotkey('del')
#time.sleep(3)
#pyautogui.hotkey('win')
#time.sleep (1)
#pyautogui.write ('Lixeira')
#pyautogui.hotkey('enter')
#time.sleep(5)
#pyautogui.hotkey('ctrl', 'a')
#pyautogui.hotkey('del')
##pyautogui.hotkey('enter')
#pyautogui.hotkey('enter')
#time.sleep(10)

webbrowser.open('http://localhost:8040/Login')
pyautogui.hotkey('Enter')
