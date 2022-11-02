import pyautogui
import time
import pyperclip

날씨 = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨"]

addr_x = 580 #url의 x,y 좌표
addr_y = 62
start_x = 333 #start x,y 캡처할 시작점 좌표
start_y = 368
end_x = 1062  #end_x,y 캡처할 끝점 좌표
end_y = 990

for 지역날씨 in 날씨:
    pyautogui.moveTo(addr_x, addr_y,1) #마우스 이동 및 커서 이동속도 설정
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1) #타자속도 설정
    pyautogui.write(["enter"])  #엔터 입력
    time.sleep(1)
    
    
    pyperclip.copy(지역날씨)    #클립보드에 저장
    pyautogui.hotkey("ctrl", "v")  #hotkey를 이용하여 두 개의 키를 동시 입력 가능
    time.sleep(0.5)
    pyautogui.write(["enter"])   #엔터키입력 "[enter]"은 enter출력
    time.sleep(1)
    저장경로 = 지역날씨 + '.png'  #작업공간에 png로 날씨들 저장
    pyautogui.screenshot(저장경로, region=(start_x, start_y, end_x, end_y))

