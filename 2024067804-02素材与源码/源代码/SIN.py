from manim import *


class SIN(Scene):
    def construct(self):
        # 显示坐标轴
        self.show_axis()
        self.show_text()
        # 显示圆
        self.show_circle()
        # 移动点并绘制曲线
        self.move_dot_and_draw_curve()
        # 等待
        self.wait(2)

    def show_text(self):
        text1 = Text("正弦函数").scale(0.7).shift(5 * LEFT + 3 * UP)
        self.play(Write(text1))

    # 定义show_axis函数，用于显示坐标轴
    def show_axis(self):
        # 定义x轴的起点和终点
        x_start = np.array([-6.5, 0, 0])
        x_end = np.array([6, 0, 0])

        # 定义y轴的起点和终点
        y_start = np.array([-3, -2, 0])
        y_end = np.array([-3, 2, 0])

        # 定义x轴和y轴
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        x_flag = MathTex(r"\theta").next_to(x_end, RIGHT)
        y_flag = MathTex(r"sin\theta").next_to(y_end, UP)

        # 将x轴和y轴添加到坐标系中
        self.play(
            Create(x_axis),
            Create(y_axis),
            Create(x_flag),
            Create(y_flag),
        )
        # 添加x轴标签
        self.add_x_labels()

        # 定义原点
        self.origin_point = np.array([-5, 0, 0])
        # 定义曲线起点
        self.curve_start = np.array([-3, 0, 0])

    # 定义一个函数，用于添加x轴标签
    def add_x_labels(self):
        # 创建一个列表，用于存储x轴标签
        x_labels = [
            MathTex("\pi"),
            MathTex("2 \pi"),
            MathTex("3 \pi"),
            MathTex("4 \pi"),
        ]

        # 遍历x轴标签列表，将每一个标签放置在x轴的特定位置
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2 * i, 0, 0]), DOWN)
            self.add(x_labels[i])

    # 定义一个函数show_circle，用于显示圆
    def show_circle(self):
        # 创建一个圆，半径为1
        circle = Circle(radius=1)
        # 将圆移动到原点
        circle.move_to(self.origin_point)
        # 将圆添加到self中
        line1 = Line([-5, -1.5, 0], [-5, 1.5, 0])
        self.play(Create(circle), Create(line1))
        # 将圆赋值给self.circle
        self.circle = circle

    def move_dot_and_draw_curve(self):
        # 获取圆的参数
        orbit = self.circle
        # 获取原点的位置
        origin_point = self.origin_point

        # 创建一个点，半径为0.08，颜色为YELLOW
        dot = Dot(radius=0.08, color=YELLOW)
        # 将点移动到圆的点上
        dot.move_to(orbit.point_from_proportion(0))
        # 初始化t_offset
        self.t_offset = 0
        # 设置每帧的移动速度
        rate = 0.25

        # 定义一个函数，用来移动点，并绘制曲线
        def go_around_circle(mobe, dt):
            # 将t_offset增加每帧移动的距离
            self.t_offset += dt * rate
            # 将点移动到圆的点上
            mobe.move_to(orbit.point_from_proportion(self.t_offset % 1))

        # 定义一个函数，用来获取到圆的线段
        def get_line_to_circle():
            # 返回从原点到点的线段，颜色为BLUE
            return Line(origin_point, dot.get_center(), color=BLUE)

        # 定义一个函数，用来获取到曲线上的线段
        def get_line_to_curve():
            # 返回从点到曲线的线段，颜色为YELLOW_A，宽度为2
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(
                dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2
            )

        # 定义一个函数，用于添加曲线，参数为self和dot
        self.curve = VGroup()
        # 添加一条线段，起点为self.curve_start，终点为self.curve_start
        self.curve.add(Line(self.curve_start, [-3, 0, 0]))

        # 定义一个函数，用于获取曲线
        def get_curve():
            # 获取曲线最后一个元素
            last_line = self.curve[-1]
            # 计算x坐标
            x = self.curve_start[0] + self.t_offset * 4
            # 计算y坐标
            y = dot.get_center()[1]
            # 添加一条线段，起点为last_line的终点，终点为[x,y,0]，颜色为YELLOW_D
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            # 将新添加的线段添加到曲线中
            self.curve.add(new_line)
            # 返回曲线
            return self.curve

        # 获取点到x轴垂线
        def get_line_to_x1():
            x = dot.get_center()[0]
            return Line(dot.get_center(), [x, 0, 0], color=GRAY_A)

        line_to_x1 = always_redraw(get_line_to_x1)

        # 获取b1
        def get_b1():
            return always_redraw(lambda: Brace(line_to_x1, RIGHT, buff=0.1))

        b1 = get_b1()

        # 获取b1的文本
        def get_b1_tex():
            return always_redraw(
                lambda: b1.get_tex(r"sin\theta")
                .next_to(b1, RIGHT, buff=SMALL_BUFF)
                .scale(0.75)
            )

        b1_tex = get_b1_tex()

        # 获取曲线到x轴的垂线
        def get_line_to_x2():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(np.array([x, 0, 0]), np.array([x, y, 0]), color=GRAY_B)

        line_to_x2 = always_redraw(get_line_to_x2)

        # 获取b2
        def get_b2():
            return always_redraw(lambda: Brace(line_to_x2, RIGHT, buff=0.1))

        b2 = get_b2()

        # 获取b2的文本
        def get_b2_tex():
            # 返回b2的文本，文本为sintheta，位置为b2的右边，缩放为0.75
            return always_redraw(
                lambda: b2.get_tex(r"sin\theta")
                .next_to(b2, RIGHT, buff=SMALL_BUFF)
                .scale(0.75)
            )

        b2_tex = get_b2_tex()

        # 添加一个从原点到圆心的线段
        origin_to_circle_line = always_redraw(get_line_to_circle)
        # 添加一个从点到曲线的线段
        dot_to_curve_line = always_redraw(get_line_to_curve)
        # 添加一个从曲线到曲线的线段
        sine_curve_line = always_redraw(lambda: get_curve())

        # 将点添加到场景中
        self.add(dot, origin_to_circle_line)
        # 将圆心、原点到圆心的线段、点到曲线的线段、曲线到曲线的线段添加到场景中
        self.add(orbit, sine_curve_line, line_to_x1, line_to_x2, dot_to_curve_line)
        self.add(b1, b1_tex, b2, b2_tex)
        # 添加一个更新器，使点在圆中移动
        dot.add_updater(go_around_circle)
        # 等待8秒
        self.wait(8)
        # 移除更新器，使点不在圆中移动
        dot.remove_updater(go_around_circle)
