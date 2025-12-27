'''
Author: Laplace
Date: 2024-04-15 16:08:37
LastEditors: Laplace
LastEditTime: 2024-05-08 09:28:33
FilePath: \undefinedd:\pythonexe_c\Trigonometric\manim-design\源代码\begin.py
Description: 

Copyright (c) 2024 by Laplace, All Rights Reserved. 
'''
from manim import *

class Begin(MovingCameraScene):
    def construct(self):
        # self.camera.frame.save_state()

        # ax = Axes(
        #     x_range=[0, 3.2 * PI, PI],
        #     y_range=[-1, 1.5],
        #     y_length=4,
        #     x_length=3.6 * PI,
        #     tips=True,
        #     axis_config={"tip_shape": StealthTip, "include_numbers": False},
        # )
        # graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])
        # pi_math = VGroup(
        #     MathTex("\pi"),
        #     MathTex("2\pi"),
        #     MathTex("3\pi"),
        # )
        # for i in range(3):
        #     pi_math[i].next_to(ax.c2p(PI * (i + 1)), DOWN, buff=0.1)

        # moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        # dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        # dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        # sin_trace = TracedPath(moving_dot.get_center).set_color(BLUE)
        # self.add(sin_trace)
        # self.play(Write(pi_math), Create(ax), FadeIn(moving_dot))
        # self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        # def update_curve(mob):
        #     mob.move_to(moving_dot.get_center())

        # all_group = VGroup(ax, graph, *pi_math, moving_dot)

        # self.camera.frame.add_updater(update_curve)
        # self.play(MoveAlongPath(moving_dot, graph, rate_func=linear), run_time=2)
        # self.add(graph)
        # self.remove(sin_trace)
        # self.camera.frame.remove_updater(update_curve)

        # self.play(Restore(self.camera.frame), all_group.animate.set_opacity(0.9))

        title = (
            Text("深入浅出理解三角函数", font="快看世界体")
            .set_color_by_gradient("#BC95C6", "#7DC4CC")
            .shift(UP)
            .scale(1.5)
        )
        title2 = (
            Text("——几何与函数抽象", font="快看世界体")
            .set_color_by_gradient("#7DC4CC", "#A7BFE8")
            .next_to(title, DOWN * 1.5)
            .scale(1.1)
        )
        # self.play(
        #     all_group.animate.set_opacity(0.2).scale(1.8),
        #     Write(title),
        #     Write(title2),
        # )
        # self.wait()

        self.play(Write(title), Write(title2))

        # content_title = (
        #     Text("CONTENT", font="快看世界体")
        #     .scale(1.3)
        #     .align_on_border(UR)
        #     .shift(LEFT * 0.5)
        #     .set_color_by_gradient({"#f6d365", "#fda085"})
        # )

        # content = (
        #     Text(
        #         "·弧度制\n\n·任意角\n\n·三角函数定义\n\n·简单性质\n\n·函数图像的简单演示\n\n",
        #         font="快看世界体",
        #     )
        #     .scale(0.75)
        #     .shift(LEFT)
        # )

        # self.play(Write(content_title))
        # self.play(Write(content))
        # self.wait()
