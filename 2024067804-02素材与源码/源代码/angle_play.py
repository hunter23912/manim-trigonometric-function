from manim import *
class angle_play(Scene):
    def construct(self):
        theta_tracker=ValueTracker(60)
        
        line1=Line(ORIGIN,[3,0,0])
        line2=Line(ORIGIN,[1.5,3*np.sin(PI/3),0])
        
        angle=Arc(radius=0.5,angle=PI/3,arc_center=ORIGIN,color=YELLOW)
        angle_label=MathTex(r"\theta").move_to(Arc(radius=0.8,angle=PI/3,arc_center=ORIGIN).point_from_proportion(0.5))
        
        theta_text=MathTex(r"\theta=").align_on_border(LEFT).shift(RIGHT).scale(1.2)
        theta_value=DecimalNumber(theta_tracker.get_value(),num_decimal_places=0,unit="^{\circ}").next_to(theta_text,RIGHT,buff=0.4).scale(1.2)
        
        
        b1=Brace(line1)
        b1text=b1.get_text("initial side")
        
        b2=Brace(line2,direction=line2.copy().rotate(PI/2).get_unit_vector())
        b2text=b2.get_text("terminal side")
        
        self.play(Create(line1),Create(line2))
        self.play(Write(angle),Write(angle_label))
        self.play(Write(theta_text),Write(theta_value))
        self.play(Write(b1),Write(b1text))
        self.play(Write(b2),Write(b2text))
        self.wait()
        
        self.play(FadeOut(b1),FadeOut(b2),FadeOut(b1text),FadeOut(b2text))
        
        # 保证角度在-180到180之间，使旋转不易错乱
        def correction(x):
            if x > 360:
                return x%360
            elif x < -360:
                return x%(-360)
            else:
                return x
        
        angle.add_updater(
            lambda x: x.become(Arc(radius=0.5,angle=correction(theta_tracker.get_value())*DEGREES,color=YELLOW))
        )           
        line2.add_updater(
            lambda x: x.become(
                Line(ORIGIN,
                     [3*np.cos(theta_tracker.get_value()*DEGREES),3*np.sin(theta_tracker.get_value()*DEGREES),0]))
            )
        angle_label.add_updater(
            lambda x: x.become(
                MathTex(r"\theta").move_to(
                    Arc(radius=0.8,angle=correction(theta_tracker.get_value())*DEGREES,arc_center=ORIGIN).point_from_proportion(0.5))
            )
        )
        theta_value.add_updater(
            lambda x: x.become(
                DecimalNumber(
                    theta_tracker.get_value(),num_decimal_places=0,
                    unit="^{\circ}"
                ).next_to(theta_text,RIGHT,buff=0.4).scale(1.2)
        )
        )
        self.play(theta_tracker.animate.set_value(120),run_time=1.5,rate_func=smooth)
        self.wait()
        self.play(theta_tracker.animate.set_value(-30),run_time=1.5,rate_functions=smooth)
        self.wait()
        self.play(theta_tracker.animate.set_value(420),run_time=4,rate_functions=smooth)
        self.wait()
        self.play(theta_tracker.animate.set_value(60),run_time=4,rate_functions=smooth)
        self.wait()
        
        

        
            
        