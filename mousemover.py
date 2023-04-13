import pyautogui
import turtle
import colorsys
import time
import datetime as dte
from datetime import date
try:
    while True:
        t = turtle.Turtle(shape="turtle")
        t1 = turtle.Turtle()
        s = turtle.Screen().bgcolor('black')
        sec = dte.datetime.now().second
        mins = dte.datetime.now().minute
        hr = dte.datetime.now().hour
        date= date.today()
        t.speed(0)
        n = 70
        h = 0
        for i in range (360):
            c = colorsys.hsv_to_rgb(h, 1, 0.8)
            t1.goto(100,450)
            t1.color(c)
            t1.hideturtle()
            t1.clear()
            t1.write("Date: "+str(date).zfill(2)+" Time: "+str(hr).zfill(2)
                        + ":"+str(mins).zfill(2)+":"
                        + str(sec).zfill(2),
                        font=("Arial", 40, "bold"))
            time.sleep(1)
            sec += 1
            if sec == 60:
                sec = 0
                mins += 1
            if mins == 60:
                mins = 0
                hr += 1
            if hr == 13:
                hr = 1
            pyautogui.mouseDown()
            pyautogui.move(0, 300, duration=1)
            pyautogui.mouseUp()
            pyautogui.move(0, -300, duration=1)
            pyautogui.FAILSAFE =True
            c = colorsys.hsv_to_rgb(h, 1, 0.8)
            h+= 1/n
            t.color(c)
            t.left(1)
            t.fd(1)
            for j in range (2):
                t.left(2)
                t.circle(150)
except:
    print("Stopped")


