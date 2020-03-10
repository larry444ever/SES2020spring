import numpy as np
import math
import matplotlib.pyplot as plt

class circle:
    #定义圆类，包括圆心坐标（x，y）与半径r
    x=0
    y=0
    r=0

    def __init__(self,x,y,r):  #定义构造函数
        self.x = x
        self.y = y
        self.r = abs(r)


def search(list):              #定义函数search，在list里面寻找符合条件的最大圆
    max_x = 0
    max_y = 0
    max_r = 0

    state = 1
    for x in range(-100,100,1):   #步长无法为0.01，因此先设为1
        x = x/100
        for  y in range(-100,100,1):
            y = y/100
            for c in list:
                if (x-c.x)**2 + (y-c.y)**2 < c.r**2:
                    state = 0

            if state==0:
                state = 1
                continue

            r = min(abs(x+1),abs(1-x),abs(y+1),abs(y-1))    #将新圆的半径先初始化为其到边界的最近距离

            for c in list:
                if (x-c.x)**2 + (y-c.y)**2 < (c.r+r)**2:    #当r太大时，改变r为相切时的半径
                    r = ((x-c.x)**2 + (y-c.y)**2)**0.5 - c.r

            if r > max_r:
                max_r = r
                max_x = x
                max_y = y       #储存最大的半径的圆

    new = circle(max_x,max_y,max_r)
    list.append(new)

def plot(list):
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1,1])
    plt.ylim([-1,1])           #画出如题的矩形范围
    theta = np.linspace(0, 2*np.pi, 90)
    for c in list:
        plt.plot(c.x + c.r*np.cos(theta), c.y + c.r*np.sin(theta), 'b')
                              #画出list里面所有的圆
    plt.show()


n = 18

if n>0:
    clist = []
    while(n):
        search(clist)   #利用贪心算法，第n次调用search函数是在第n-1次调用search函数的基础之上得到的最优解
        n-=1

    plot(clist)







