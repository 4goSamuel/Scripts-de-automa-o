import pyautogui
import time

pyautogui.keyDown('alt')

pyautogui.press('tab', presses=10)

time.sleep(0.5)

pyautogui.keyUp('alt')
