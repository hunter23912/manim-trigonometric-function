from manim import *

class End(Scene):
    def construct(self):
        title = (
            Text("QUESTION", font="快看世界体")
            .set_color_by_gradient({"#f6d365", "#fda085"})
            .align_on_border(UL, buff=0.3)
            .shift(RIGHT * 0.3 + DOWN * 0.3)
        )
        quesiton1 = MathTex(
            r"&\sin{300^{\circ}}=\ ? \\ &\sin{(\theta+\frac{k\pi}{2})}=\ ?(k\in{Z}) \\ &\tan{\frac{\pi}{2}} \ \ ?"
        ).align_on_border(LEFT, buff=1)

        self.play(Write(quesiton1), SpiralIn(title), run_time=2)
        self.wait()
