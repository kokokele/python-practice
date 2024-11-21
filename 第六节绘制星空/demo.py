import turtle
import random
turtle.title('绘制五角星')
turtle.setup(500, 300, 299, 199)
turtle.screensize(600, 100, '#FF0f0f')
turtle.shape('turtle')
# drawStars()


def star(x, y, left_angle, edge_len, color='white'):
    """
    画一个五角星
    :param x: 起始x坐标
    :param y: 起始y坐标
    :param left_angle: 画笔方向逆时针转动度数
    :param edge_len: 五角星边的长度
    :param color: 五角星颜色
    :return:
    """
    # 五角星边的颜色
    turtle.pencolor(color)
    # 五角星内部填充色
    turtle.fillcolor(color)
    # 绘制速度，0代表最快，1-10：数字越大越快
    turtle.speed(0)

    turtle.pu()  # 抬起画笔
    turtle.goto(x, y)  # 移动到初始位置
    turtle.pd()  # 放下画笔

    turtle.begin_fill()  # 开始填充图形
    # 画笔方向以水平方向为基准
    # 逆时针转动 left_angle 度
    turtle.left(left_angle)
    # 循环绘制五角星的 5 条边
    for _ in range(5):
        # 向画笔方向移动edge_len像素长度
        # 即：绘制五角星的一条边
        turtle.forward(edge_len)
        # 画笔方向顺时针旋转144度
        # 由于五角星内角是36度，因此旋转180-36=144度
        turtle.right(144)
    turtle.end_fill()  # 填充完成
    # 将画笔方向恢复为水平方向，以免影响后续画图
    turtle.left(-left_angle)

def drawStars():
    for _ in range(200):
        # 随机生成起始坐标、画笔方向和五角星边长
        rand_x = random.randint(-400, 400)
        rand_y = random.randint(0, 400)
        edge_len = random.randint(3, 8)
        left_angle = random.randint(0, 180)
        # star(rand_x, rand_y, left_angle, edge_len, '#B7C5D2')
        star(rand_x, rand_y, left_angle, edge_len, 'white')

        

# turtle.delay(0)
#turtle.tracer(False)

star(-100, -100, 30, 100)

print(turtle.screensize())

turtle.done()

'''
这段代码使用turtle库绘制了一个五角星，并且调用了drawStars函数绘制了200个随机位置和大小的五角星。

具体的绘制过程如下：
1. 导入turtle和random库。
2. 设置窗口标题为"绘制五角星"，窗口大小为500x300，窗口位置为299,199。
3. 设置画布大小为600x100，背景色为"#FF0f0f"。
4. 设置画笔形状为"turtle"。
5. 定义一个star函数，用于绘制一个五角星。函数参数包括起始坐标(x, y)，画笔方向逆时针转动度数left_angle，五角星边的长度edge_len和颜色color。
6. 在star函数中，设置画笔颜色为color，填充颜色也为color，绘制速度为最快。
7. 抬起画笔，移动到起始坐标(x, y)，放下画笔，开始填充图形。
8. 将画笔方向逆时针转动left_angle度。
9. 循环绘制五角星的5条边，每条边向画笔方向移动edge_len像素长度，然后画笔方向顺时针旋转144度。
10. 填充完成后，将画笔方向恢复为水平方向。
11. 定义一个drawStars函数，用于绘制200个随机位置和大小的五角星。
12. 在drawStars函数中，使用for循环执行200次，每次循环中随机生成起始坐标、画笔方向和五角星边长，然后调用star函数绘制五角星。
13. 调用star函数绘制一个起始坐标为(-100, -100)，画笔方向逆时针转动30度，五角星边长为100的五角星。
14. 打印画布大小。
15. 结束绘制。

注意：代码中有一些被注释掉的部分，包括turtle.delay(0)和turtle.tracer(False)，这些是用于控制绘制速度和显示的，可以根据需要进行调整。 
'''