import pyautogui
from time import sleep

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

while True:
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    sleep(0.1)
    pyautogui.moveTo(828, 490)
    pyautogui.click()
    sleep(0.2)
    pyautogui.press('enter')
    sleep(0.1)





#pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
#pyautogui.doubleClick()
#pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
#pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
#pyautogui.keyDown('shift')
#pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
#pyautogui.keyUp('shift')
#pyautogui.hotkey('ctrl', 'c')