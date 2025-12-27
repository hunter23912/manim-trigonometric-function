from manim import *
class UnitCircle(Scene):
    def construct(self):
        self.show_plane()
        self.add_triangle()
        self.wait()
    
    # 画出坐标系、圆
    def show_plane(self):
        screen_width=config["frame_width"]
        screen_height=config["frame_height"]
        plane=NumberPlane(
            x_range=[-1.1,1.1,1],
            y_range=[-1.1,1.1,1],
        ).shift(3*LEFT)
        plane.set_width(screen_width-4)
        plane.set_height(screen_height-2)
        self.origin=plane.c2p(0,0)
        len=plane.get_x_unit_size()
        origin_point=MathTex("O").next_to(self.origin,DL,buff=0.1).scale(0.8)
        unit_label=MathTex("1")
        unit_label.next_to(plane.c2p(1,-0.1),buff=0.1).scale(0.8)
        circle=Circle(radius=len,color=RED).move_to(self.origin)       
        self.play(Create(plane))
        self.play(Create(circle),Write(unit_label),Write(origin_point))
        self.circle=circle
        self.plane=plane
        
    # 添加三角形
    def add_triangle(self):
        dot1=Dot(color=BLUE).move_to(self.circle.point_from_proportion(1/7))
        dot1_label=MathTex("A(x,y)").next_to(dot1,UR,buff=0.1).scale(0.8)      
        line1=Line(self.origin,dot1.get_center(),color=YELLOW)
        x=dot1.get_center()[0]
        line_to_x=Line(dot1.get_center(),[x,0,0],color=YELLOW)
        B_label=MathTex("B").next_to([x,0,0],DOWN,buff=0.2).scale(0.8)
        linex=Line(self.origin,[x,0,0],color=YELLOW)
        
        self.play(Create(dot1))
        self.play(Write(dot1_label))
        self.play(Create(line1),Create(line_to_x),Create(linex))
        self.play(Write(B_label))
        
        # 角度标签
        arc=Angle(linex,line1,radius=0.5)
        arc_tex=MathTex(r"\theta").move_to(
            Angle(linex,line1,radius=0.5+3*0.1).point_from_proportion(0.5)
        )
        
        # 直角标签
        rt=RightAngle(line_to_x,linex,length=0.2)
        rt.rotate(PI,about_point=[x,0,0])
        
        self.play(Write(arc),Write(rt))
        self.play(Write(arc_tex))
        
        triangle_group=VGroup(line1,line_to_x,linex)
        self.play(Indicate(triangle_group))
        
        # 画边的标记
        b1=Brace(line1,direction=line1.copy().rotate(PI/2).get_unit_vector(),buff=0.1)
        b1_tex=b1.get_tex(r"1",buff=0.1).scale(0.8)
        
        b2=Brace(line_to_x,RIGHT,buff=0.1)
        b2_tex=b2.get_tex(r"y",buff=0.1).scale(0.8)
        
        b3=Brace(linex,DOWN,buff=0.1)
        b3_tex=b3.get_tex(r"x",buff=0.1).scale(0.8)
        
        self.play(Write(b1),Write(b1_tex))
        self.wait(0.5)
        self.play(Write(b2),Write(b2_tex))
        self.wait(0.5)
        self.play(Write(b3),Write(b3_tex))
        self.wait()
        
        # 角度标记组合
        theta_group=VGroup(arc,arc_tex)
        
        # 添加表达式
        def get_text():
            
            # sinθ=
            t1_1=MathTex(r"sin\theta","=").arrange(RIGHT,buff=0.1).move_to(RIGHT*3+UP*2).scale(1.5)
            self.play(Indicate(arc_tex,scale_factor=1.6))
            self.wait(0.5)
            self.play(TransformFromCopy(theta_group,t1_1))
            self.wait(0.5)
            
            # AB/AO
            t1_2=MathTex(r"\frac{AB}{AO}").next_to(t1_1,RIGHT,buff=0.1)
            
            # 强调AB,AO
            sin_group=VGroup(line1,line_to_x)
            self.play(Indicate(sin_group,scale_factor=1.5,color=YELLOW_C),run_time=1.5)
            self.play(TransformFromCopy(sin_group,t1_2))
            self.wait(0.5)
            
            # cosθ=
            t2_1=MathTex(r"cos\theta","=").arrange(RIGHT,buff=0.1).next_to(t1_1,DOWN*4).scale(1.5)
            self.play(TransformFromCopy(theta_group,t2_1))
            self.wait(0.5)
            
            # OB/AO
            t2_2=MathTex(r"\frac{OB}{AO}").next_to(t2_1,RIGHT,buff=0.1)
            
            # 强调OB,AO
            cos_group=VGroup(linex,line1)
            self.play(Indicate(cos_group,scale_factor=1.5,color=YELLOW_C),run_time=1.5)
            self.play(TransformFromCopy(cos_group,t2_2))
            self.wait(0.5)            
            
            # tan=sinθ/cosθ
            t3_1=MathTex(r"tan\theta=").scale(1.5).next_to(t2_1,DOWN*4)
            
            t3_2=MathTex(r"\frac{sin\theta}{cos\theta}").next_to(t3_1,RIGHT,buff=0.3).scale(1.2)
            
            # 将sinθ、cosθ组合
            sc_group1=VGroup(t1_1[0],t2_1[0])
            
            self.play(TransformFromCopy(theta_group,t3_1))
            self.wait(0.5)
            self.play(Indicate(sc_group1))
            self.play(TransformFromCopy(sc_group1,t3_2))
            self.wait()        
            
            # 第二部分，将线段转化成值
            # y/1->y
            sin_group2=VGroup(t1_1,t1_2)
            
            t1_3=MathTex(r"\frac{y}{1}").next_to(t1_1,RIGHT,buff=0.3).scale(1.5)
            t1_4=MathTex(r"y").next_to(t1_1,RIGHT,buff=0.3).scale(1.5)
            self.play(Indicate(sin_group2))
            self.wait(0.5)
            self.play(ReplacementTransform(t1_2,t1_3))
            self.wait(0.5)
            self.play(ReplacementTransform(t1_3,t1_4))
            self.wait()
            
            # x/1->x
            cos_group2=VGroup(t2_1,t2_2)
            t2_3=MathTex(r"\frac{x}{1}").next_to(t2_1,RIGHT,buff=0.3).scale(1.5)
            t2_4=MathTex(r"x").next_to(t2_1,RIGHT,buff=0.3).scale(1.5)
            
            self.play(Indicate(cos_group2))
            self.wait(0.5)
            self.play(ReplacementTransform(t2_2,t2_3))
            self.wait(0.5)
            self.play(ReplacementTransform(t2_3,t2_4))
            self.wait()
            
            # sinθ/cosθ->y/x
            tan_group2=VGroup(t3_1,t3_2)
            t3_3=MathTex(r" \frac{y}{x}").next_to(t3_1,RIGHT,buff=0.3).scale(1.5)    
            sc_group2=VGroup(t1_4,t2_4)
            
            self.play(Indicate(tan_group2))
            self.play(FadeOut(t3_2))
            self.play(Indicate(sc_group2))
            self.play(TransformFromCopy(sc_group2,t3_3))
            self.wait(2)
            
            def end_text():
                self.play(
                    FadeOut(t1_1),
                    FadeOut(t2_1),
                    FadeOut(t3_1),
                    FadeOut(t1_4),
                    FadeOut(t2_4),
                    FadeOut(t3_3),
                )
            end_text()
        get_text()
        def end_triangle():
            self.play(
                FadeOut(b1),
                FadeOut(b1_tex),
                FadeOut(b2),
                FadeOut(b2_tex),
                FadeOut(b3),
                FadeOut(b3_tex),
                FadeOut(dot1),
                FadeOut(dot1_label),
                FadeOut(B_label),
                FadeOut(arc),
                FadeOut(arc_tex),
                FadeOut(rt),
                Uncreate(line1),
                Uncreate(line_to_x),
                Uncreate(linex),
            )
        end_triangle()
            
        
        
        
            
            
            
        
        