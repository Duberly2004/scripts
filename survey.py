import pyautogui
import time
import pyperclip

pyautogui.press('tab')
time.sleep(5)
#pyautogui.hotkey('ctrl', 'v')

count = 0
limit = 23

while count <limit:
        for i in range(9):
                pyautogui.press('tab')
                print('start=> ',i)

        pyautogui.press('enter')
        pyautogui.press('tab')  
        print(f'{count} completed!')
        count +=1

pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('enter')

print('Saved successfully')
