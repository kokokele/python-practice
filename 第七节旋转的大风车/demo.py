'''
绘制动态大风车
知识点：
* trace(0) 隐藏屏幕绘制过程， 需要加 turtle.update()手动更新
* circle(xx, 180)：绘制半圆
* ontimer
'''

import turtle as t
# t.speed(1)
t.tracer(0)  # 隐藏屏幕绘制过程，需要手动更新
t.hideturtle()  # 隐藏海龟图标

def drawHead():
    colors = ['red', 'green', 'purple', 'yellow']  # 定义颜色列表
    for i in range(4):
        t.up()  # 抬起画笔
        t.goto(0, 200)  # 移动到指定位置
        t.down()  # 放下画笔
        t.color(colors[i])  # 设置画笔颜色
        t.begin_fill()  # 开始填充
        t.circle(30, 180)  # 绘制半圆
        t.end_fill()  # 结束填充
        t.left(90)  # 左转90度

def update():
    t.clear()  # 清除屏幕
    t.left(1)  # 左转1度
    drawHead()  # 绘制头部
    t.update()  # 手动更新屏幕
    t.ontimer(update, 10)  # 设置定时器，10毫秒后调用update函数

drawHead()  # 初始绘制头部
t.update()  # 手动更新屏幕

update()  # 开始动态更新
t.done()  # 结束绘图

'''
1、导入turtle模块：使用import turtle as t导入turtle模块并简写为t。
2、设置绘图参数：
    t.tracer(0)：隐藏屏幕绘制过程，需要手动更新。
    t.hideturtle()：隐藏海龟图标。
3、定义drawHead函数：
    定义颜色列表colors。
    循环4次，每次绘制一个半圆并填充不同颜色。
4、定义update函数：
    清除屏幕。
    左转1度。
    调用drawHead函数绘制头部。
    手动更新屏幕。
    设置定时器，10毫秒后再次调用update函数，实现动态效果。
5、初始绘制和更新：
    调用drawHead函数初始绘制头部。
    手动更新屏幕。
    调用update函数开始动态更新。
6、结束绘图：调用t.done()结束绘图。
'''