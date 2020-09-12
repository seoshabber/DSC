from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

t=time.localtime()
ms=0

while True:
    sec_pre=t[5]
    canvas.delete("all")#모두 삭제\
    t=time.localtime()#시간
    sr = 220
    mr = 180
    hr = 130#침 길이
    #초
    #sec=t[5]#초, 1초에 6도
    #s_radian = 6*sec*2*3.14/360
    #sx = sr * math.sin(s_radian)
    #sy = sr * math.cos(s_radian)
    #canvas.create_line(250,250, 250+sx, 250-sy)#중간이 250
    #초/ 더 부드럽게, 초를 더 나눠야할 것 같음
    
    sec=t[5]
    if sec_pre != sec:
        ms=0
    sec_degree = t[5]*6 + ms*6/10
    ms += 1
    if ms > 9:
        ms=0
    s_radian = sec_degree*2*3.14/360
    sx = sr*math.sin(s_radian)
    sy = sr*math.cos(s_radian)
    canvas.create_line(250, 250, 250+sx, 250-sy, fill='red', width='1')
    #sec=t[5]#초, 1초에 6도
    #s_radian = 6*sec*2*3.14/360
    #sx = sr * math.sin(s_radian)
    #sy = sr * math.cos(s_radian)
    #canvas.create_line(250,250, 250+sx, 250-sy)
    #분
    min=t[4]
    m_radian = ((6*min)+(sec*1/10))*2*3.14/360 #1분에 6도, 1초에 1/10도
    mx = mr * math.sin(m_radian)
    my = mr * math.cos(m_radian)
    canvas.create_line(250,250, 250+mx, 250-my, width='2')
    #시
    hour=t[3]
    h_radian = (hour*30+min/2)*2*3.14/360 #1시간에 30도, 1분에 1/2도
    hx = hr * math.sin(h_radian)
    hy = hr * math.cos(h_radian)
    canvas.create_line(250,250, 250+hx, 250-hy, width='3')
    #원
    canvas.create_arc(10,10,490, 490, style=CHORD, width=2, extent=359)
    canvas.create_arc(245,245,255,255, style=CHORD, extent=359, fill="blue")
    #프로그래밍 실습1 5분 단위로 눈금 추가
    #30도에 눈금 한개, 길이는 10정도
    r = 10#눈금 길이
    for i in range(12):
        r_degree = i*30#눈금 번호, 각도
        r_radian = r_degree*2*3.14/360
        rx_s = 250+240*math.sin(r_radian)#눈금 시작
        ry_s = 250-240*math.cos(r_radian)
        rx_e = 250+230*math.sin(r_radian)#눈금 끝
        ry_e = 250-230*math.cos(r_radian)
        canvas.create_line(rx_s, ry_s, rx_e, ry_e)
        


    #갱신, sleep
    tk.update()
    time.sleep(0.1)
    
    
    


#while True :
    #canvas.delete("all")
    #t = time.localtime()
    #hour = t[3]
    #min = t[4]
    #sec = t[5]
    #my_clock=str(hour)+":"+str(min)+":"+str(sec)
    #canvas.create_text(250, 250, text = str(hour)+":"+str(min)+":"+str(sec), font = ('Arial', 25))
    #tk.update()
    #time.sleep(1)
