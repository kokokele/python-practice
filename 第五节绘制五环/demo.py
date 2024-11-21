import turtle

def draw_circle(color, position):
    turtle.penup()
    turtle.pensize(5)
    turtle.color(color)
    turtle.goto(position)
    turtle.pendown()
    turtle.circle(50)

turtle.speed(0)  # 设置绘制速度
draw_circle("blue", (-120, 0))  # 绘制第一个环
draw_circle("black", (0, 0))  # 绘制第二个环
draw_circle("red", (120, 0))  # 绘制第三个环
draw_circle("yellow", (-60, -50))  # 绘制第四个环
draw_circle("green", (60, -50))  # 绘制第五个环
turtle.done()  # 结束绘制


'''
此程序主要使用了 turtle的circle方法实现的，文档地址 https://www.geeksforgeeks.org/turtle-circle-method-in-python/
代码比较简单，代码中有注释。
关键点：如果想改变circle的笔画大小，需要使用turtle.size方法。