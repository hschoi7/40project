import pyautogui
import time
import pyperclip

pyautogui.moveTo(796,257,0.2) #x, y의 좌표로 이동합니다.서울 날씨
pyautogui.click()              #마우스를 클릭
time.sleep(0.5)                #0.5초 딜레이

pyperclip.copy("서울 날씨")    #클립보드에 저장
pyautogui.hotkey("ctrl", "v")  #hotkey를 이용하여 두 개의 키를 동시 입력 가능
time.sleep(0.5)

pyautogui.write(["enter"])   #엔터키입력 "[enter]"은 enter출력
time.sleep(1)

