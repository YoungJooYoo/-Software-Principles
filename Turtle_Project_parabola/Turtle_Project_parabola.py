import turtle as t
import math  # sin, cos,radians 함수를 사용하기 위해 사용함

tm = 0.3 # 시간 간격 변수
ux = 0 # x 속도 변수
uy = 0 # y 속도 변수
dx = 0 # x 이동거리
dy = 0 # y 이동거리
g = 9.8 # 중력가속도
velo = 0 # 앞으로 나아가는 속도 변수, 던질 속도는?
ang = 0 # 높이 던지는 각도 변수 던질, 각은?


def draw_pos(x,y):
    velo = t.numinput("입력,","속도: ",50,10,100) # 입력값 50 기본 설정 범위는 10~100
    ang = math.radians(t.numinput("입력","각도 : ",45,0,360))
    # 기본 입력값 45 범위 0~360, sin, cos함수는 인수가 라디안 값이므로 일반적
    # 각도 값을 라디안 값으로 변환해서 대입

    t.clearstamps() # stamp를 전부 clear 즉 초기화
    t.hideturtle() # 거북이를 화면에 숨긴다.
    t.setpos(x,y) # 좌표 x,y로 이
    t.showturtle() # 거북이를 화면에 표시한
    t.stamp() # 스탬프찍기

    hl = -(t.window_height() /2) # 스크린 하단에 해당하는 y축 위치를 계산하여 hl에 대입

    ux = velo * math.cos(ang) # x의 속도를 계산
    uy = velo * math.sin(ang) # y의 속도를 계산

    while True:
        uy = uy + (-1 * g) * tm # 중력가속도가 반영된 y속도를 계산하여 uy에 대입
        dy = t.ycor() + (uy*tm) - (g*tm**2) / 2 # dy,dx 이동 거리를 계산하여 대입
        dx = t.xcor() + (ux*tm)
        if dy > hl:
            t.goto(dx,dy)
            t.stamp()
        else:
            break



t.setup(600,600) # 메인윈도우 크기 설정
t.shape("circle") # 아이콘을 원모양으
t.shapesize(0.3, 0.3, 0) # shapesize
t.penup() # 펜을 든다는 명령, 이동하면서 선을 그리지 않는다.
s = t.Screen()
s.onscreenclick(draw_pos) # 클릭하면 값을 입력하는 창이 끈다. 즉 클릭하면 함수를 실
s.listen() # 이 명령어를 실행하야 입력모드가 실행이 되고, 입력된 키에 반응한다.
t.mainloop() # 편집기에 따라 코드가 끝난 후에 창이 바로 종료 될 수 있는데, 종료를 방지하는 명령


# http://blog.naver.com/PostView.nhn?blogId=talkativehacker&logNo=221294708689 코드출처


