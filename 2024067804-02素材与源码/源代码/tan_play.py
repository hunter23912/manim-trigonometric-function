from manim import *

class tan_play(Scene):
    def construct(self):
        self.create()
        self.moving_dot()
        
    # 绘制平面
    def create(self):
        screaen_width=config["frame_width"]
        screen_height=config["frame_height"]
        
        plane=NumberPlane(
            x_range=[-1.1,1.1,1],
            y_range=[-1.1,1.1,1],
        ).shift(3*LEFT)
        plane.set_width(screaen_width-4)
        plane.set_height(screen_height-2)
        len=plane.get_x_unit_size()
        
        unit_label=MathTex("1")
        unit_label.next_to(plane.c2p(1,0),DL,buff=0.1).scale(0.8)
        origin_point=MathTex("O").next_to(plane.c2p(0,0),DL,buff=0.1).scale(0.8)
        self.plane=plane
        circle=Circle(radius=len,color=RED).shift(plane.c2p(0,0))
        self.circle=circle
        self.add(plane,circle,unit_label,origin_point)
     
     
        # 正切动画演示
    def moving_dot(self):
        # 定义moving_dot函数
        theta_tracker=ValueTracker(40)
        # 创建一个ValueTracker对象，并赋值为40
        
        dot=Dot(color=YELLOW)
        dot.move_to(self.circle.point_from_proportion(1/9))
        dot_label=MathTex(r"A(x,y)").next_to(dot,LEFT,buff=0.1).scale(0.8)
        self.dot=dot
        
        dot2_y=np.tan(theta_tracker.get_value()*DEGREES)
        dot2=Dot(color=YELLOW).move_to(self.plane.c2p(1,dot2_y))
        dot3=Dot(color=YELLOW).move_to(self.plane.c2p(1,0))
        linex1=Line(self.plane.c2p(0,0),[dot.get_center()[0],0,0],color=YELLOW)
        linex=Line(self.plane.c2p(0,0),self.plane.c2p(1,0),color=BLUE)
        line=Line(self.plane.c2p(0,0),dot2.get_center(),color=BLUE)
        line_chui=Line(dot2.get_center(),self.plane.c2p(1,0))
        
        a=Arc(angle=theta_tracker.get_value()*DEGREES,arc_center=self.plane.c2p(0,0),radius=0.5)
        tex=MathTex(r"\theta").move_to(
            Angle(linex,line,radius=0.8)
        )
        
        jiao_group=VGroup(a,tex)
        line1=Line(self.plane.c2p(0,0),dot.get_center(),color=YELLOW)
        line2=Line(dot.get_center(),[dot.get_center()[0],0,0],color=YELLOW)
                
        self.play(Create(dot),Write(dot_label))
        self.play(Create(line1),Create(line2),Create(linex1))
        self.play(Write(jiao_group))
        self.wait(0.5)
        
        t1=MathTex(r"tan\theta=").scale(1.5).shift(RIGHT*3)
        def write_text():
            self.play(TransformFromCopy(jiao_group,t1))
            self.wait(0.5)
            tan_group=VGroup(line2,linex1)
            t2=MathTex(r"\frac{y}{x}").next_to(t1,RIGHT,buff=0.3).scale(1.5)
            self.play(TransformFromCopy(tan_group,t2))
            self.wait(0.5)
            
            t3=MathTex("?").next_to(t1,RIGHT,buff=0.3).scale(1.5)
            self.play(ReplacementTransform(t2,t3))
            self.wait()
            self.play(FadeOut(t3),FadeOut(dot_label),FadeOut(line1),FadeOut(line2),FadeOut(linex1))
            self.wait(0.5)
        write_text()
        
        self.play(Create(line))
        self.play(Create(dot2))
        
        def get_dot2_label():
            return always_redraw(lambda: MathTex("P").next_to(dot2,UR,buff=0.1)).scale(0.8)
        dot2_label=get_dot2_label()
        dot3_label=MathTex("Q").next_to(dot3,DR,buff=0.1).scale(0.8)
        self.play(Write(dot2_label))
        
        self.play(Create(line_chui),Create(dot3))
        self.play(Write(dot3_label))
        
        sanjiao_group=VGroup(line,line_chui,linex)
        self.play(Indicate(sanjiao_group))
        self.wait(0.5)
        
        t2_1=MathTex(r"\frac{PQ}{OQ}").next_to(t1,RIGHT,buff=0.1)
        t2_2=MathTex(r"PQ").next_to(t1,RIGHT,buff=0.3).scale(1.3)
        
        self.play(Indicate(sanjiao_group[1:]))
        self.wait(0.5)
        self.play(TransformFromCopy(sanjiao_group[1:],t2_1))
        self.wait(0.5)
        self.play(Indicate(linex,scale_factor=1.5))
        self.wait(0.5)
        self.play(ReplacementTransform(t2_1,t2_2))
        
        theta_text=MathTex(r"\theta=").scale(1.5).shift(RIGHT*3+UP*2)
        theta_value=DecimalNumber(theta_tracker.get_value(),num_decimal_places=0,unit="^{\circ}").scale(1.5).next_to(theta_text,RIGHT,buff=0.3)
        
        t1_value=DecimalNumber(np.tan(theta_tracker.get_value()*DEGREES)).scale(1.5).next_to(t1,RIGHT,buff=0.3)
         
           
        # 为曲线添加更新器
        def update_inital():
            theta_value.add_updater(lambda x: x.set_value(theta_tracker.get_value())
            )
            
            t1_value.add_updater(lambda x: x.set_value(np.tan(theta_tracker.get_value()*DEGREES)))
            
            dot.add_updater(
                lambda x:x.move_to(self.plane.c2p(np.cos(theta_tracker.get_value()*DEGREES),np.sin(theta_tracker.get_value()*DEGREES)))
            )
            dot2.add_updater(
                lambda x:x.move_to(self.plane.c2p(1,np.tan(theta_tracker.get_value()*DEGREES)))
            )
            line_chui.add_updater(
                lambda x:x.become(Line(self.plane.c2p(1,0),dot2.get_center()))
            )
            line.add_updater(
                lambda x:x.become(Line(self.plane.c2p(0,0),dot2.get_center(),color=BLUE))
                )
            a.add_updater(
                lambda x:x.become(Arc(angle=theta_tracker.get_value()*DEGREES,radius=0.5,arc_center=self.plane.c2p(0,0)))
            )
            def should_use_other_angle(linex,line):
                angle=Angle(linex,line)
                return angle.get_value()>PI
            tex.add_updater(
                lambda x:x.move_to(
                    Angle(linex,line,radius=0.8,other_angle=should_use_other_angle(linex,line))
                    )
                )
        update_inital()
        
        # 添加括号及标签
        def get_b1():
            return always_redraw(
                lambda:Brace(
                    line_chui,direction=RIGHT,buff=SMALL_BUFF)
                )
        b1=get_b1()
        def get_b1text():
            return always_redraw(
                lambda:b1.get_tex(r"tan\theta").next_to(b1,RIGHT,buff=SMALL_BUFF)
            )
        b1text=get_b1text()
        

        
        def start_move_animate():
            self.play(Write(b1))
            self.play(Write(b1text))
            self.play(Write(theta_text),Write(theta_value))
            self.play(FadeOut(t2_2),Write(t1_value))
            self.play(theta_tracker.animate.set_value(55),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(-50),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(40),run_time=2)
            self.wait()
        start_move_animate()
        
        def end():
            self.play(
                Uncreate(jiao_group),
                FadeOut(t1),
                FadeOut(t1_value),
                FadeOut(b1),
                FadeOut(b1text),
                FadeOut(dot2_label),
                FadeOut(dot3_label),
                FadeOut(theta_text),
                FadeOut(theta_value),
                Uncreate(dot3),
                Uncreate(dot2),
                Uncreate(dot),
                Uncreate(line_chui),
                Uncreate(linex),
                Uncreate(line)
            )
        end()