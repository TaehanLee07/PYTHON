# 간단한 오토마우스 만들어 보기
일단 시작하기전 'tkinter'과 'pyautogui' 라이브러리를 사용해서 만들어 볼거다 
tkinter는 파이썬에서 GUI 프로그램을 만들때 사용되는 라이브러리로 간단하게 Hello World를 창을 띄워서 출력하고 싶을때 사용한다고 가정하면
# tkinter의 자세한  설명듣기
from tkinter import * # `tkinter` 모듈의 모든 요소를 가져오기 위한 코드

root = Tk() # `Tk` 객체를 생성하여 기본 윈도우 창을 만듦
label = Label(root, text='Hello World') # `Label` 위젯을 생성하여 텍스트를 표시함 `root`는 라벨이 위치할 윈도우를 지정하며, `text` 인자는 라벨에 표시할 문자열을 지정함

label.pack() # `pack` 메서드를 사용하여 `label` 위젯을 창에 배치함, 위젯의 크기와 위치를 자동으로 조정함

root.mainloop() # 사용자의 입력 이벤트(예: 버튼 클릭, 키보드 입력 등)를 처리함 <br><br> 
# 실행화면 <br><br> ![실행 화면](https://github.com/TaehanLee07/PYTHON/assets/121335699/beb233d5-8e17-4f7d-9a07-18cb8c45ecba)

# pyautogui 이란?
파이썬에서 마우스와 키보드 제어를 도와주는 라이브러리 이다.
사용하려면  pip install pyautogui을 통해 설치를 해줘야한다.
pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다
이렇게 사용할 수 있다.
# pyautogui 자세한 설명 들으러 가기
 
