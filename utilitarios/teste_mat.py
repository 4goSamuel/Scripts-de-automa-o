import  pygetwindow as  gw
import  pyautogui   as  pa
import  time

# pega as janelas do chrome
janelas = [w for w in gw.getAllWindows() if "Chrome" in w.title]

num_jan = len(janelas)

print(f"encontradas {num_jan} janelas")


