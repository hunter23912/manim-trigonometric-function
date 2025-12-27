from manim import *

# 引入部分
class introduction(Scene):
    def construct(self):
        # 定义三角形的三个顶点
        dian = [[-4, -1, 0], [-2, -1, 0], [-4, 2, 0]]

        # 创建三角形
        sanjiao = Polygon(*dian, color=BLUE)
        line_ca = Line([-4, -1, 0], [-4, 2, 0], color=BLUE)
        line_ab = Line([-4, -1, 0], [-2, -1, 0], color=BLUE)
        line_cb = Line([-4, 2, 0], [-2, -1, 0], color=BLUE)
        # 显示三角形
        self.play(Create(sanjiao))

        # 计算标记位置
        label_positions = [
            dian[0] + 0.5 * LEFT + 0.5 * DOWN,
            dian[1] + 0.5 * RIGHT + 0.5 * DOWN,
            dian[2] + 0.5 * UP,
        ]

        # 创建弧，从左侧开始顺时针画
        arc = Arc(
            angle=-np.arctan(1.5), radius=0.5, arc_center=dian[1], start_angle=PI
        ).set_color(X11.YELLOW1)

        # 创建角标记
        t1 = Text("A", color=X11.PLUM).move_to(label_positions[0])
        t2 = Text("B", color=X11.PLUM).move_to(label_positions[1])
        t3 = Text("C", color=X11.PLUM).move_to(label_positions[2])
        labels = VGroup(t1, t2, t3)
        # 显示角标记和弧
        self.play(Write(labels), Create(arc))
        self.wait()

        text1a = MathTex(r"\sin B", r"=\frac{AC}{BC} ").shift(RIGHT + 2 * UP)
        text1b = (
            Text("(对边比斜边)")
            .next_to(text1a, RIGHT)
            .scale(0.7)
            .set_color(X11.SPRINGGREEN1)
        )
        text1 = VGroup(text1a, text1b)

        text2a = MathTex(r"\cos B", r"=\frac{AB}{BC} ").next_to(text1a, DOWN)
        text2b = (
            Text("(邻边比斜边)")
            .next_to(text2a, RIGHT)
            .scale(0.7)
            .set_color(X11.SPRINGGREEN1)
        )
        text2 = VGroup(text2a, text2b)

        text3a = MathTex(r"\tan B", r"=\frac{AC}{AB} ").next_to(text2a, DOWN)
        text3b = (
            Text("(对边比邻边)")
            .next_to(text3a, RIGHT)
            .scale(0.7)
            .set_color(X11.SPRINGGREEN1)
        )
        text3 = VGroup(text3a, text3b)

        self.play(Indicate(arc), Indicate(t2))
        self.play(Write(text1a[0]))
        self.play(Indicate(line_ca))
        self.play(Indicate(line_cb))
        self.play(Write(text1a[1]))
        self.play(Write(text1b))
        self.wait(0.5)
        self.play(Write(text2a[0]))
        self.play(Indicate(line_ab))
        self.play(Indicate(line_cb))
        self.play(Write(text2a[1]))
        self.play(Write(text2b))
        self.wait(0.5)
        self.play(Write(text3a[0]))
        self.play(Indicate(line_ca))
        self.play(Indicate(line_ab))
        self.play(Write(text3a[1]))
        self.play(Write(text3b))
        self.wait()
