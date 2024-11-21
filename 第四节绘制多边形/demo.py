import turtle
def draw(n):
    angle = (n - 2) * 180 / n
    print(angle)
    for i in range(n):
        turtle.forward(100)
        turtle.rt(180 - angle)

#n = input('想要绘制几边形')
n = turtle.numinput('提示', '想要绘制几边形？')

draw(int(n))
turtle.mainloop()
turtle.circle()

'''
这段代码使用了turtle库来绘制多边形。具体解释如下：

导入turtle库。

定义了一个名为draw的函数，该函数接受一个参数n，表示要绘制的多边形的边数。

在函数内部，通过计算(n - 2) * 180 / n得到多边形内角的度数，并将结果赋值给变量angle。


使用for循环，循环n次，每次循环执行以下操作：

使用turtle.forward(10)向前移动10个像素。
使用turtle.rt(180 - angle)右转到下一个顶点的角度。
通过turtle.numinput()函数弹出一个对话框，提示用户输入要绘制的多边形的边数，并将用户输入的值赋值给变量n。

调用draw函数，传入用户输入的多边形边数。

使用turtle.mainloop()进入主循环，保持窗口持续显示。

使用turtle.circle()绘制一个圆形。

注意：代码中的turtle.mainloop()和turtle.circle()是在draw函数调用之后执行的，与绘制多边形无关。
'''