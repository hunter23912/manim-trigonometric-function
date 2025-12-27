# -*- coding: utf-8 -*-
from manim import *
from manim import X11, AS2700, BS381, XKCD

"""--------------
    NOTE:Radian
    弧度制相关介绍
--------------"""


class Radian(Scene):
    def construct(self):
        self.create()
        self.desciption()
        self.wait()

    def create(self):
        # 用于演示的中心圆
        self.center_circle = Circle(radius=2, color=BLUE).shift(LEFT * 3)

        # 值更新器
        self.angle_value_tracker = ValueTracker(0.2)

        # 用于圆上移动的点,比例
        self.dotB_move_in_circle = Dot(
            self.center_circle.point_from_proportion(0), color=YELLOW
        )
        self.dotA_move_in_circle = always_redraw(
            lambda: Dot(
                self.center_circle.point_from_proportion(
                    self.angle_value_tracker.get_value()
                ),
                color=YELLOW,
            )
        )

        # 用于演示的边
        self.line1_radius = Line(
            start=self.center_circle.get_center(),
            end=self.dotB_move_in_circle.get_center(),
            color=WHITE,
        )

        self.line2_radius = always_redraw(
            lambda: Line(
                start=self.center_circle.get_center(),
                end=self.dotA_move_in_circle.get_center(),
                color=WHITE,
            )
        )

        # 用于演示的角度
        self.angle = always_redraw(
            lambda: Angle(
                self.line1_radius,
                self.line2_radius,
                radius=0.5,
                color=WHITE,
            )
        )

        # 角度值
        self.angle_value = DecimalNumber(self.angle.get_value())
        self.angle_value.add_updater(
            lambda mob: mob.become(DecimalNumber(self.angle.get_value()))
        )

        # 用于演示的theta标签和点(用于让theta标签对齐到角度上)
        self.dot_theta = always_redraw(
            lambda: Dot(
                self.center_circle.copy()
                .scale(0.5)
                .point_from_proportion(self.angle_value_tracker.get_value() / 2),
                fill_opacity=0,
            )
        )

        self.theta_label = always_redraw(
            lambda: MathTex(r"\theta").move_to(self.dot_theta)
        )

        # 定义两点间的弧
        self.arc_between_dot = always_redraw(
            lambda: Arc(
                radius=2,
                start_angle=0,
                angle=Angle(self.line1_radius, self.line2_radius).get_value(),
                arc_center=self.center_circle.get_center(),
                color=X11.DEEPPINK1,
            )
        )

        # 定义两点的标签
        self.label1_dot_B = always_redraw(
            lambda: MathTex("B").next_to(self.dotB_move_in_circle, RIGHT)
        )
        self.label2_dot_A = always_redraw(
            lambda: MathTex("A", color=X11.SPRINGGREEN1).next_to(
                self.dotA_move_in_circle, UR
            )
        )

        # 定义原点标签
        self.label_origin = (
            MathTex("O").next_to(self.center_circle.get_center(), DL).scale(0.7)
        )

        self.add(self.dotA_move_in_circle, self.dot_theta)
        # 创建场景
        self.play(
            Create(self.center_circle),
            FadeIn(self.label1_dot_B),
            Create(self.line1_radius),
            FadeIn(self.label2_dot_A),
            Create(self.line2_radius),
            Create(self.dot_theta),
        )
        self.play(
            Write(self.label_origin),
            Write(self.theta_label),
            FadeIn(self.angle),
            Create(self.arc_between_dot),
            run_time=2,
        )

    def desciption(self):
        # 文字和数学公式分开渲染(只能这样了)
        tex_radin_math = Tex(
            r"$\overset{\LARGE{\frown}}{AB}=$",
            r"  $l$",
            tex_template=TexTemplateLibrary.ctex,
        ).next_to(self.center_circle, UR * 2 + RIGHT * 8)

        l_label = always_redraw(
            lambda: MathTex("l")
            .next_to(
                Dot(
                    self.center_circle.copy().point_from_proportion(
                        self.angle_value_tracker.get_value() / 2
                    ),
                    fill_opacity=0,
                ),
                UR,
                buff=0.2,
            )
            .set_color(X11.PLUM1)
        )
        # OB=r
        tex_r_label = MathTex(r"OB=", r"r").next_to(tex_radin_math, DOWN)
        # 定义半径标签
        radius_brace = Brace(self.line1_radius, direction=DOWN, color=X11.GOLD1)

        label_radius = MathTex("r", color=X11.PLUM1).next_to(radius_brace, DOWN)
        self.play(Write(tex_radin_math), Write(tex_r_label))
        self.play(
            Indicate(tex_radin_math[-1], color=X11.PLUM1, scale_factor=2),
            Indicate(tex_r_label[-1], color=X11.PLUM1, scale_factor=2),
        )
        self.play(
            TransformFromCopy(tex_radin_math[-1], l_label),
            DrawBorderThenFill(radius_brace),
            TransformFromCopy(tex_r_label[-1], label_radius),
            run_time=1,
        )
        self.wait()

        # theta = AB/OB
        tex_theta = MathTex(
            r"\theta=", r"\frac{\overset{\LARGE{\frown}}{AB}}{OB}"
        ).next_to(tex_r_label, DOWN)
        self.play(TransformFromCopy(VGroup(tex_r_label, tex_radin_math), tex_theta))
        self.wait()
        # 公式表示
        tex_theta_formula = (
            MathTex(r"\theta=", r"\frac{l}{r}", tex_template=TexTemplateLibrary.ctex)
            .next_to(tex_r_label, DOWN)
            .shift(LEFT * 0.25)
        )

        # 2 PI标签
        tex_2pi = (
            MathTex(r"\theta=", r"2\pi", color=XKCD.TANGERINE)
            .move_to(self.center_circle)
            .shift(UP * 3)
        )
        # 圆周长公式
        tex_circle_length = MathTex(r"{C}", r"=", r"{2\pi}", r"{r}").next_to(
            tex_theta_formula, DOWN
        )
        self.play(Transform(tex_theta, tex_theta_formula))
        self.wait()
        self.moving(1)
        self.play(Write(tex_circle_length), FadeIn(tex_2pi))
        self.wait()
        self.play(Circumscribe(tex_2pi), Circumscribe(tex_circle_length))

        # 得到另一个周长表示公式
        tex_circle_length_change = MathTex(r"{2\pi}", r"=", r"\frac{C}{r}").next_to(
            tex_theta_formula, DOWN
        )
        self.play(TransformMatchingTex(tex_circle_length, tex_circle_length_change))
        self.wait()
        all_obj = VGroup(
            tex_theta, tex_radin_math, tex_r_label, tex_circle_length_change
        )
        # 写出转换公式
        tex_change_formula = (
            MathTex(
                r"\theta",
                r"=",
                r"\frac{2\pi}{360}",
                r"\times",
                r"\alpha",
                color=XKCD.VERYLIGHTBLUE,
            )
            .next_to(self.center_circle, RIGHT)
            .shift(RIGHT * 2.5 + UP * 1.5)
        )
        tex_change_formula[0].set_color(XKCD.UGLYYELLOW)
        tex_change_formula[-1].set_color(XKCD.UGLYYELLOW)

        text_explain = VGroup(
            Text("radian", slant=ITALIC, font="Times New Roman", color=XKCD.UGLYYELLOW),
            Text("angle", slant=ITALIC, font="Times New Roman", color=XKCD.UGLYYELLOW),
        ).scale(0.8)
        text_explain[0].next_to(tex_change_formula[0], DOWN)
        text_explain[-1].next_to(tex_change_formula[-1], DOWN)
        self.play(FadeTransform(all_obj, tex_change_formula))
        self.play(
            Indicate(tex_change_formula[0], color=XKCD.UGLYYELLOW, scale_factor=2),
            Indicate(tex_change_formula[-1], color=XKCD.UGLYYELLOW, scale_factor=2),
            SpiralIn(text_explain),
        )
        self.wait()
        # 添加 alpha 标签
        alpha_label = (
            MathTex(r"\alpha=", color=XKCD.ROBINSEGG)
            .next_to(text_explain[0], DOWN)
            .shift(DOWN * 0.5)
        )
        # 添加 alpha 值标签
        alpha_value_label = always_redraw(
            lambda: DecimalNumber(unit="^{\circ}", color=XKCD.ROBINSEGG)
            .set_value(self.angle_value_tracker.get_value() * 360)
            .next_to(alpha_label, RIGHT)
        )
        self.play(TransformFromCopy(tex_change_formula[-1], alpha_label))
        self.play(Write(alpha_value_label))

        # 改变角度标签,旋转动画
        def change_2pi_label(angle_value: float):

            self.play(
                Transform(
                    tex_2pi,
                    MathTex(
                        r"\theta=", f"{angle_value/180:.2f}\\pi", color=XKCD.TANGERINE
                    )
                    .move_to(self.center_circle)
                    .shift(UP * 3.25),
                )
            )
            self.moving(angle_value / 360)

        change_2pi_label(90)
        change_2pi_label(180)
        change_2pi_label(0.000001)
        self.wait()

    def moving(self, move_angle: float):

        # 移动点
        self.play(self.angle_value_tracker.animate.set_value(move_angle))
