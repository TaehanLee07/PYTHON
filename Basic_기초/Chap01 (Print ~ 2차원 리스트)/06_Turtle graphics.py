# Turtle graphics 란?
# 터틀은 어린이 및 초보자가 파이썬을 쉽게 배울 수 있도록 만든 모듈인데, 거북이가 기어가는 모양대로 그림을 그린다고 해서 터틀이라고 합니다.
# 사용해보기
import turtle as t # 이름을 t로 turtle 클래스름 불러옴
t.shape('turtle') # t의 모양 설정 기본값은 화살표 모양이다
t.forward(100) # 거북이를 100픽셀 만큼 앞으로 이동시킴
t.right(90) # 거북이를 90도 회전시킴

# 사각형 그려보기
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# 다른 기능들
# 앞으로 이동: forward, fd # 줄여 적을수 있다
# 뒤로 이동: backward, bk, back
# 왼쪽으로 회전: left, lt
# 오른쪽으로 회전: right, rt

import turtle as t
 
t.shape('turtle')
 
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

# mainloop
# 만약 그림을 다 그리자 마자 꺼지면 mainloop를 써보자 그러면 사용자가 창을 닫을때 까지 창이 유지된다
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.mainloop()

# speed
# speed는 거북이의 속도를 지정합니다 0에서 10 사이의 수로 나타내며 기본값은 6입니다 0은 가장빠른 1은 가장느림 이후 숫자가 오를수록 빨라집니다.

t.speed(0) # 0 이외의 다른수를 넣어보세요
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.mainloop()

# color
# 그냥 color 는 거북이의 색을 바꿔주고 bg.color 는 배경의 색을 바꿔준다
t.color('red')
t.bgcolor('blue')
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.mainloop()

# 반복문을 사용해서 그리보기
# 반복문을 활용해서 단순한 도형이 아닌 더 복잡한 그림도 그릴수 있다.
for i in range(300):    # 600번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)
t.mainloop()
# 사각형으로 이루어진 소용돌이 그림이 만들어진다

# write
# 터틀 클래스에서 제공하는 write로 글씨를 쓸수도 있다
t.write("거북이", align="center", font=("궁서", 34, "bold"))
# 천천히 알아보면 왼쪽부터 '적을 글씨', '글씨 정렬', '폰트' , '글씨 크기', '굵게' 이다
