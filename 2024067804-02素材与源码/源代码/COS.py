from manim import *

class COS(Scene):
    def construct(self):
        # 显示坐标轴
        self.show_axis()
        # 显示文本
        self.show_text()
        # 显示圆
        self.show_circle()
        
        # 移动点并绘制曲线
        self.move_dot_and_draw_curve()
        # 等待
        self.wait()

    

    def show_text(self):
        # 创建文本
        text1=Text("余弦函数").scale(0.7).shift(5*LEFT+3*UP)
        # 播放文本
        self.play(Write(text1))
        
    def show_axis(self):
        # 设置x轴的起点和终点
        x_start = np.array([-6.5,0,0])
        x_end = np.array([6,0,0])

        # 设置y轴的起点和终点
        y_start = np.array([-3,-2,0])
        y_end = np.array([-3,2,0])

        # 创建x轴和y轴
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)
        
        # 创建x轴的标签
        x_flag=MathTex(r"\theta").next_to(x_end,RIGHT)
        y_flag=MathTex(r"cos\theta").next_to(y_end,UP)
                
        # 播放x轴和y轴以及x轴的标签和y轴的标签
        self.play(
            Create(x_axis),
            Create(y_axis),
            Create(x_flag),
            Create(y_flag),
            )
        # 添加x轴的标签
        self.add_x_labels()

        # 设置原点
        self.origin_point = np.array([-5,0,0])
        # 设置曲线起点
        self.curve_start = np.array([-3,1,0])

    def add_x_labels(self):
        # 创建x轴的标签
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        # 将x轴的标签移动到指定位置
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        # 创建圆
        circle = Circle(radius=1)
        # 将圆移动到原点
        circle.move_to(self.origin_point)
        # 创建从原点到圆的线
        line1=Line([-5,-1.5,0],[-5,1.5,0])
        # 播放创建圆和从原点到圆的线
        self.play(Create(circle),Create(line1))
        # 将圆赋值给self.circle
        self.circle = circle

    def move_dot_and_draw_curve(self):
        # 获取圆和原点
        orbit = self.circle
        origin_point = self.origin_point

        # 创建点
        dot = Dot(radius=0.08, color=YELLOW)
        # 将点移动到圆上
        dot.move_to(orbit.point_from_proportion(0))
        # 初始化偏移量
        self.t_offset = 0
        # 设置偏移量的变化率
        rate = 0.25

        # 创建一个函数，用于更新点的移动
        def go_around_circle(mobe, dt):
            # 更新偏移量
            self.t_offset += (dt * rate)
            # 更新点的移动
            mobe.move_to(orbit.point_from_proportion(self.t_offset % 1))

        # 创建一个函数，用于获取从原点到点的线
        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        # 创建一个函数，用于获取从点到曲线的线
        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )
        
        # 创建一个函数，用于获取从点到y轴的线
        def get_line_to_y():
            y=dot.get_center()[1]
            return Line(dot.get_center(), np.array([-5,y,0]), color=YELLOW_B, stroke_width=2 )
        
        # 创建一个函数，用于获取从点到y轴的标签
        def get_b1():
            return always_redraw(lambda: Brace(get_line_to_y(),UP, buff=0.1))
        b1=get_b1()
        
        # 创建一个函数，用于获取y轴的标签
        def get_b1_tex():
            return always_redraw(lambda: b1.get_tex(r"cos\theta").next_to(b1,UP,buff=SMALL_BUFF).scale(0.75))
        b1_tex=get_b1_tex()
            
        
        # 创建一个函数，用于获取从曲线的线到x轴的线
        def get_line_curve_to_x():
            x=self.curve_start[0] + self.t_offset * 4
            y=dot.get_center()[0]+5
            return Line(np.array([x,y,0]), np.array([x,0,0]), color=YELLOW_B, stroke_width=2 )
        
        def get_b2():
            return always_redraw(lambda: Brace(get_line_curve_to_x(),RIGHT,buff=SMALL_BUFF))
        b2=get_b2()
        
        def get_b2_tex():
            return always_redraw(lambda: b2.get_tex(r"cos\theta").next_to(b2,RIGHT,buff=SMALL_BUFF).scale(0.75))
        b2_tex=get_b2_tex()


        # 创建一个VGroup，用于存放曲线
        self.curve = VGroup()
        # 将曲线添加到VGroup中
        self.curve.add(Line(self.curve_start,self.curve_start))
        # 创建一个函数，用于更新曲线
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[0]+5
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            # 将新线添加到曲线中
            self.curve.add(new_line)

            # 返回曲线
            return self.curve

        # 创建一个函数，用于获取从原点到圆的线
        origin_to_circle_line = always_redraw(get_line_to_circle)
        # 创建一个函数，用于获取从点到曲线的线
        dot_to_curve_line = always_redraw(get_line_to_curve)
        # 创建一个函数，用于获取曲线
        cosine_curve_line = always_redraw(get_curve)

        # 创建一个函数，用于获取从点到y轴的线
        dot_to_y_line = always_redraw(get_line_to_y)
        
        # 创建一个函数，用于获取从曲线的线到x轴的线
        curve_to_x_line = always_redraw(get_line_curve_to_x)
        
        # 添加圆、从原点到圆的线、从点到曲线的线、从曲线的线到x轴的线、从点到y轴的线、从点到y轴的标签
        self.add(orbit,dot,origin_to_circle_line)
        self.add(cosine_curve_line,dot_to_y_line,curve_to_x_line)
        self.play(Write(b1),Write(b2))
        self.play(Write(b1_tex),Write(b2_tex))
        
        # 添加点的更新器
        dot.add_updater(go_around_circle)
        # 等待8秒
        self.wait(8)
        # 移除点的更新器
        dot.remove_updater(go_around_circle)