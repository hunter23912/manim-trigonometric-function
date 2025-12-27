from manim import *


class TAN(Scene):
    def construct(self):
        # 显示坐标轴
        self.show_axis()
        self.show_text()
        # 显示圆
        self.show_circle()
        # 移动点并绘制曲线
        self.move_dot_and_draw_curve()
        # 等待
        self.wait()

    def show_text(self):
        text1 = Text("正切函数").scale(0.7).shift(5 * LEFT + 3 * UP)
        self.play(Write(text1))

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

        # 定义x轴和y轴的标签
        x_flag = MathTex(r"\theta").next_to(x_end, RIGHT)
        y_flag = MathTex(r"tan\theta").next_to(y_end, UP)

        # 创建x轴和y轴以及x轴和y轴的标签
        self.play(
            Create(x_axis),
            Create(y_axis),
            Create(x_flag),
            Create(y_flag),
        )
        # 添加x轴的标签
        self.add_x_labels()

        # 定义原点以及曲线起始点
        self.origin_point = np.array([-5, 0, 0])
        self.curve_start = np.array([-3, 0, 0])

    def add_x_labels(self):
        # 定义x轴的标签
        x_labels = [
            MathTex(r"\frac{\pi}{2}"),
            MathTex(r"\pi"),
            MathTex(r"\frac{3}{2}\pi"),
            MathTex(r"2 \pi"),
            MathTex(r"\frac{5}{2}\pi"),
            MathTex(r"3 \pi"),
            MathTex(r"\frac{7}{2}\pi"),
            MathTex(r"4 \pi"),
        ]

        # 将x轴的标签添加到坐标轴上
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-2 + i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        # 创建圆
        circle = Circle(radius=1)
        # 将圆移动到原点
        circle.move_to(self.origin_point)
        # 创建线段
        line1 = Line([-4, -100, 0], [-4, 100, 0])
        # 创建圆和线段
        self.play(Create(circle), Write(line1))
        # 将圆赋值给self.circle
        self.circle = circle

        dash_line1 = DashedLine(
            [-2, 5, 0], [-2, -5, 0], color=X11.PLUM, dash_length=0.2
        )
        dash_line2 = DashedLine([0, 5, 0], [0, -5, 0], color=X11.PLUM, dash_length=0.2)
        dash_line3 = DashedLine([2, 5, 0], [2, -5, 0], color=X11.PLUM, dash_length=0.2)
        dash_line4 = DashedLine([4, 5, 0], [4, -5, 0], color=X11.PLUM, dash_length=0.2)
        self.play(
            Create(dash_line1),
            Create(dash_line2),
            Create(dash_line3),
            Create(dash_line4),
        )
        self.wait()

    def move_dot_and_draw_curve(self):
        # 获取圆和原点
        orbit = self.circle
        origin_point = self.origin_point

        # 创建点
        dot = Dot(radius=0.08, color=YELLOW_E)
        # 将点移动到圆上
        dot.move_to(orbit.point_from_proportion(0))

        # 创建另一个点
        dot2 = Dot(radius=0.08, color=YELLOW)
        # 将点移动到原点
        dot2.move_to([-4, 0, 0])

        # 定义偏移量
        self.t_offset = 0
        # 定义移动速度
        rate = 0.2

        # 定义移动圆的函数
        def go_around_circle(mobe, dt):
            # 更新偏移量
            self.t_offset += dt * rate
            # 将点移动到圆上
            mobe.move_to(orbit.point_from_proportion(self.t_offset % 1))

        # 定义获取移动点的函数
        def get_moving_dot2():
            # 获取点的斜率
            jiaodu = np.arctan2(dot.get_center()[1], dot.get_center()[0] + 5)
            # 计算移动点的y坐标
            dot2_y = np.tan(jiaodu)
            # 返回移动点
            return Dot(np.array([-4, dot2_y, 0]), radius=0.1, color=YELLOW)

        def get_b1():
            return always_redraw(
                lambda: Brace(Line(dot2.get_center(), [-4, 0, 0]), RIGHT, buff=0.1)
            )

        b1 = get_b1()

        def get_b1_tex():
            return always_redraw(
                lambda: b1.get_tex(r"tan\theta")
                .scale(0.75)
                .next_to(b1, RIGHT, buff=SMALL_BUFF)
            )

        b1_tex = get_b1_tex()

        # 定义获取原点与点的斜线的函数
        def get_line_origin_tan():
            # 获取原点与点的向量
            vector = dot.get_center() - origin_point
            # 返回斜线
            return Line(origin_point, dot.get_center() + vector * 15, color=BLUE)

        # 定义获取原点与点的斜线的函数
        def get_line_fan_origin_tan():
            # 获取原点与点的向量
            vector = origin_point - dot.get_center()
            # 返回斜线
            return Line(origin_point, origin_point + 15 * vector, color=BLUE)

        # 定义获取点与曲线之间的斜线的函数
        def get_line_to_curve():
            # 获取曲线起始点的x坐标
            x = self.curve_start[0] + self.t_offset * 4
            # 获取移动点的y坐标
            y = dot2.get_center()[1]
            # 返回斜线
            return Line(
                dot2.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2
            )

        # 定义获取曲线与x轴之间的斜线的函数
        def get_line_curve_to_x():
            # 获取曲线起始点的x坐标
            x = self.curve_start[0] + self.t_offset * 4
            # 获取移动点的y坐标
            y = dot2.get_center()[1]
            # 返回斜线
            return Line(
                np.array([x, y, 0]), np.array([x, 0, 0]), color=YELLOW_B, stroke_width=2
            )

        curve_to_x_line = always_redraw(get_line_curve_to_x)

        def get_b2():
            return always_redraw(lambda: Brace(curve_to_x_line, RIGHT, buff=0.1))

        b2 = get_b2()

        def get_b2_tex():
            return always_redraw(
                lambda: b2.get_tex(r"tan\theta")
                .next_to(b2, RIGHT, buff=SMALL_BUFF)
                .scale(0.75)
            )

        b2_tex = get_b2_tex()

        # 创建曲线
        self.curve = VGroup()
        # 添加曲线上的线段
        self.curve.add(Line(self.curve_start, self.curve_start))

        # 定义获取曲线的函数
        def get_curve():
            # 获取曲线上的最后一条线段
            last_line = self.curve[-1]
            # 获取曲线起始点的x坐标
            x = self.curve_start[0] + self.t_offset * 4
            # 获取移动点的y坐标
            y = dot2.get_center()[1]
            # 返回斜线
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            # 将斜线添加到曲线中
            self.curve.add(new_line)
            # 返回曲线
            return self.curve

        # 添加原点与点的斜线
        origin_tan_line = always_redraw(get_line_origin_tan)
        # 添加原点与点的斜线
        origin_tan_line_fan = always_redraw(get_line_fan_origin_tan)
        # 添加点与曲线之间的斜线
        dot_to_curve_line = always_redraw(get_line_to_curve)
        # 添加曲线
        tan_curve_line = always_redraw(lambda: get_curve())

        # 添加曲线与x轴之间的斜线

        # 添加圆和点
        self.add(orbit, dot, dot2)
        # 添加原点与点的斜线
        self.add(origin_tan_line, origin_tan_line_fan)
        # 添加曲线
        self.add(tan_curve_line)
        # 添加曲线与x轴之间的斜线
        self.add(curve_to_x_line, dot_to_curve_line)
        self.add(b1, b1_tex, b2, b2_tex)

        dot.add_updater(go_around_circle)
        dot2.add_updater(lambda b: b.become(get_moving_dot2()))
        # 等待10.5秒
        self.wait(10.5)

        # 移除点与曲线的更新器
        dot.remove_updater(go_around_circle)
        dot2.remove_updater(get_moving_dot2)
