from manim import *

class feature(Scene):
    def construct(self):

        # 初始化背景函数
        def backgroud():
            screaen_width = config["frame_width"]
            screen_height = config["frame_height"]
            plane = NumberPlane(
                x_range=[-1.1, 1.1, 1],
                y_range=[-1.1, 1.1, 1],
            ).shift(LEFT * 3)
            plane.set_width(screaen_width - 4)
            plane.set_height(screen_height - 2)
            len = plane.get_x_unit_size()

            label1 = MathTex("1").next_to(plane.c2p(1, 0), DL, buff=0.1).scale(0.8)
            label0 = MathTex("O").next_to(plane.c2p(0, 0), DL, buff=0.1).scale(0.8)
            circle = Circle(radius=len, color=RED).shift(plane.c2p(0, 0))
            self.plane = plane
            self.circle = circle
            self.add(plane, label1, label0, circle)

        backgroud()
        plane = self.plane
        circle = self.circle

        dot = Dot(color=YELLOW).shift(circle.point_from_proportion(1 / 9))

        y2 = np.tan(40 * DEGREES)

        dot2 = Dot(color=YELLOW).shift(plane.c2p(1, y2))

        line1 = Line(plane.c2p(0, 0), dot2.get_center(), color=X11.PALETURQUOISE)

        liney1 = Line(dot.get_center(), [dot.get_center()[0], 0, 0], color=X11.PLUM)

        liney1_b = Brace(liney1, LEFT, buff=0.1)

        liney1_b_label = liney1_b.get_tex(r"sin\theta", buff=0.1).scale(0.8)

        liney2 = Line(dot2.get_center(), plane.c2p(1, 0), color=X11.PLUM)

        liney2_b = Brace(liney2, RIGHT, buff=0.1)

        liney2_b_label = liney2_b.get_tex(r"tan\theta", buff=0.1).scale(0.8)

        linex = Line(
            plane.c2p(0, 0), [dot.get_center()[0], 0, 0], color=X11.PALETURQUOISE
        )

        jiao = Angle(linex, line1, radius=0.5, color=X11.LIGHTGOLDENRODYELLOW)

        jiao_label = (
            MathTex(r"\theta")
            .move_to(
                Angle(linex, line1, radius=0.5 + 3 * SMALL_BUFF).point_from_proportion(
                    0.5
                )
            )
            .set_color(X11.LIGHTGOLDENRODYELLOW)
        )

        jiao_group = VGroup(jiao, jiao_label)

        dash_line = DashedLine(
            plane.c2p(1, 1), plane.c2p(-1, -1), dash_length=0.1, color=YELLOW
        )

        up_group = Polygon(
            self.plane.c2p(1, 1),
            self.plane.c2p(-1, 1),
            self.plane.c2p(-1, -1),
            color=X11.PLUM,
            fill_opacity=0.1,
        )

        down_group = Polygon(
            self.plane.c2p(1, 1),
            self.plane.c2p(1, -1),
            self.plane.c2p(-1, -1),
            color=X11.PLUM,
            fill_opacity=0.1,
        )

        sin_tan_group = VGroup(liney1_b, liney1_b_label, liney2_b, liney2_b_label)

        func = (
            MathTex(r"y=x").next_to(dash_line, UR, buff=0.1).set_color(X11.SPRINGGREEN1)
        )

        func1 = MathTex(r"y>x").shift(plane.c2p(-0.4, 0.4)).set_color(X11.SPRINGGREEN1)

        func2 = MathTex(r"y<x").shift(plane.c2p(0.4, -0.4)).set_color(X11.SPRINGGREEN1)

        t1 = MathTex(r"\left|sin\theta\right|<\left|tan\theta\right|").shift(
            UP + 4 * RIGHT
        )

        t2 = MathTex(r"sin\theta>cos\theta").next_to(t1, DOWN)

        t3 = MathTex(r"sin\theta<cos\theta").next_to(t2, DOWN)

        self.play(Create(dot))
        self.play(Create(line1))
        self.play(Create(jiao_group))
        self.play(Create(linex), Create(liney1), Create(liney2))
        self.play(Write(liney1_b), Write(liney2_b))
        self.play(Write(liney1_b_label), Write(liney2_b_label))
        self.wait(0.5)

        self.play(Indicate(liney1), Indicate(liney2), Indicate(sin_tan_group))
        self.play(ReplacementTransform(sin_tan_group, t1))
        self.wait(0.5)

        self.play(Create(dash_line))
        self.play(Write(func))
        self.play(Create(up_group))
        self.play(Write(func1))
        self.play(ReplacementTransform(up_group, t2))
        self.wait(0.5)

        self.play(Create(down_group))
        self.play(Write(func2))
        self.play(ReplacementTransform(down_group, t3))
        self.wait()
