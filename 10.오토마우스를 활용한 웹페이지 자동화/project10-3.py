import pyautogui
import time
import pyperclip

pyautogui.moveTo(796,257,0.2) #x, y의 좌표로 이동합니다.서울 날씨
pyautogui.click()              #마우스를 클릭
time.sleep(0.5)                #0.5초 딜레이

pyperclip.copy("서울 날씨")    #클립보드에 저장
pyautogui.hotkey("ctrl", "v")  #hotkey를 이용하여 두 개의 키를 동시 입력 가능
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 333 #start x,y 캡처할 시작점 좌표
start_y = 368
end_x = 1062  #end_x,y 캡처할 끝점 좌표
end_y = 990

#screenshot함수를 이용해 캡처
pyautogui.screenshot('서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
#region 사용 시 캡처 영역 지정 가능
