from manim import *
from manim import X11


class Induction_Formula(Scene):
    def construct(self):
        self.backgroud()
        self.draw()
        # 初始化背景函数

    def backgroud(self):
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
        self.circle = Circle(radius=len, color=RED).shift(plane.c2p(0, 0))
        self.origin = plane.c2p(0, 0)
        self.plane = plane
        self.add(plane, label1, label0, self.circle)

    def draw(self):
        dot1 = Dot(color=BLUE_D, radius=0.08).move_to(
            self.circle.point_from_proportion(1 / 18)
        )
        dot1_label = MathTex("A(x,y)").scale(0.8).next_to(dot1, UP, buff=0.1)

        linex = DashedLine(
            self.origin,
            [dot1.get_center()[0], 0, 0],
            color=X11.SPRINGGREEN1,
            dash_length=0.1,
        )
        line_to_dot1 = Line(self.origin, dot1.get_center(), color=YELLOW)

        a = Angle(linex, line_to_dot1, radius=0.5)
        a_label = (
            MathTex(r"\theta")
            .scale(0.8)
            .move_to(Angle(linex, line_to_dot1, radius=0.8))
        )

        liney = DashedLine(
            dot1.get_center(),
            [dot1.get_center()[0], 0, 0],
            color=X11.SPRINGGREEN1,
            dash_length=0.1,
        )

        t = MathTex(r"cos\theta=x, sin\theta=y").move_to(RIGHT * 3 + UP * 2)
        t_before = MathTex(r"sin(\theta+\frac{\pi}{2})=?").move_to(RIGHT * 3 + DOWN)
        self.play(Create(dot1))
        self.play(Create(line_to_dot1), Write(dot1_label))
        self.play(Create(a), Write(a_label))
        self.play(Create(liney), Create(linex))
        self.wait()
        self.play(Write(t))
        self.wait()
        self.play(Write(t_before))
        self.wait()
        self.play(FadeOut(t_before))

        dot2 = dot1.copy().move_to(self.circle.point_from_proportion(1 / 18 + 0.25))
        dot2_label = MathTex("A_1", "(-y,", "x", ")").scale(0.8).next_to(dot2, UP)
        line_to_dot2 = Line(self.origin, dot2.get_center(), color=YELLOW)
        liney2 = DashedLine(
            dot2.get_center(),
            [dot2.get_center()[0], 0, 0],
            color=X11.SPRINGGREEN1,
            dash_length=0.1,
        )
        linex2 = DashedLine(
            self.origin,
            [dot2.get_center()[0], 0, 0],
            color=X11.SPRINGGREEN1,
            dash_length=0.1,
        )

        a_up = Arc(
            angle=PI / 9, start_angle=1.5 * PI, arc_center=dot2.get_center(), radius=0.5
        )
        a_up_label = (
            MathTex(r"\theta_1")
            .move_to(
                Arc(
                    angle=PI / 9,
                    start_angle=1.5 * PI,
                    arc_center=dot2.get_center(),
                    radius=0.8,
                )
            )
            .scale(0.8)
        )

        a_mid = Angle(line_to_dot2, linex2, radius=0.3)
        a_mid_label = (
            MathTex(r"\alpha")
            .move_to(Angle(line_to_dot2, linex2, radius=0.7))
            .scale(0.8)
        )

        triangle2 = VGroup(
            dot2,
            dot2_label[0],
            line_to_dot2,
            liney2,
            linex2,
            a_up,
            a_up_label,
            a_mid,
            a_mid_label,
        )

        t1_angle = MathTex(r"\theta+\alpha=\frac{\pi}{2}").next_to(t, DOWN)
        t2_angle = MathTex(r"\theta_1+\alpha=\frac{\pi}{2}").next_to(t1_angle, DOWN)
        t_12 = VGroup(t1_angle, t2_angle)
        t_12_b = Brace(t_12, buff=0.1, direction=LEFT)
        t3_angle = MathTex(r"\theta=\theta_1").next_to(t2_angle, DOWN)
        a2 = Sector(
            inner_radius=0,
            outer_radius=0.5,
            angle=110 * DEGREES,
            color=PINK,
            fill_opacity=0.6,
        ).shift(self.origin)
        a2_label = (
            MathTex(r"\theta+\frac{\pi}{2}")
            .scale(0.6)
            .move_to(Angle(linex, line_to_dot2, radius=1.4))
        )
        B_label = MathTex("B").scale(0.8).next_to(self.plane.c2p(1, 0), DR, buff=0.2)
        B_1_label = (
            MathTex(r"B_1")
            .scale(0.8)
            .next_to([dot2.get_center()[0], 0, 0], DOWN, buff=0.1)
        )

        self.play(Write(triangle2), run_time=2)
        self.play(Write(B_label), Write(B_1_label))
        self.play(Create(a2))
        self.play(Write(a2_label))
        self.wait()
        self.play(Write(t1_angle), Write(t2_angle))
        self.play(Write(t_12_b))
        self.play(FadeIn(t3_angle))
        self.play(FadeOut(t1_angle), FadeOut(t2_angle), FadeOut(t_12_b))
        self.play(t3_angle.animate.next_to(t, DOWN))

        t4_angle = MathTex("AO=A_1O").next_to(t3_angle, DOWN).scale(0.8)
        t_34 = VGroup(t3_angle, t4_angle)
        t_34_b = Brace(t_34, buff=0.1, direction=LEFT)
        t5_angle = (
            MathTex(r"\bigtriangleup AOB\cong\bigtriangleup A_1B_1O")
            .next_to(t4_angle, DOWN)
            .scale(0.8)
        )

        self.play(Write(t4_angle))
        self.play(Write(t_34_b))
        self.play(Write(t5_angle))
        self.wait()
        self.play(Indicate(dot2_label[0], scale_factor=1.5))
        self.play(Write(dot2_label[1:]))
        self.wait()
        t2_sin = MathTex(r"sin(\theta+\frac{\pi}{2})=", "x").next_to(t5_angle, DOWN)
        t2_sin_end = MathTex(r"cos\theta").next_to(t2_sin[0], RIGHT, buff=0.2)

        self.play(Write(t2_sin[0]))
        self.play(Indicate(dot2_label[-2], scale_factor=1.5))
        self.play(TransformFromCopy(dot2_label[-2], t2_sin[-1]))
        self.wait()
        self.play(ReplacementTransform(t2_sin[-1], t2_sin_end))
        self.wait()
        t2_cos = MathTex(r"cos(\theta+\frac{\pi}{2})=-sin\theta").next_to(t2_sin, DOWN)
        t2_group = VGroup(t2_sin, t2_cos)
        self.play(Write(t2_cos))
        self.wait()
        self.play(Circumscribe(t2_group))
        self.wait()
