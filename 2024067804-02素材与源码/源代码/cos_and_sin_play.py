from manim import *
from os import system

class cos_and_sin_play(Scene):
    def construct(self):
        self.create()
        self.moving_dot()
    
    def create(self):
        screaen_width=config["frame_width"]
        screen_height=config["frame_height"]
        # 设置数平面
        plane=NumberPlane(
            x_range=[-1.1,1.1,1],
            y_range=[-1.1,1.1,1],
        ).shift(3*LEFT)
        plane.set_width(screaen_width-4)
        plane.set_height(screen_height-2)
        # 1刻度
        len=plane.get_x_unit_size()
        unit_label=MathTex("1")
        unit_label.next_to(plane.c2p(1,0),DR,buff=0.1).scale(0.8)
        # 原点刻度
        origin_point=MathTex("O").next_to(plane.c2p(0,0),DL,buff=0.1).scale(0.8)
        self.plane=plane
        # 画圆
        circle=Circle(radius=len,color=RED).shift(plane.c2p(0,0))
        self.circle=circle
        self.add(plane,circle,unit_label,origin_point)
        
    def moving_dot(self):
        theta_tracker=ValueTracker(60)
                
        # 创建一个点
        dot=Dot(color=YELLOW)
        # 将点移动到圆的1/6处
        dot.move_to(self.circle.point_from_proportion(1/6))
        self.dot=dot
        # 创建一条线
        line=Line(self.plane.c2p(0,0),dot.get_center())
        # 创建一条线
        linex=Line(self.plane.c2p(0,0),self.plane.c2p(1,0))
        # 复制线
        line_ref=linex.copy()
        
        # 创建一条线
        a=Arc(angle=theta_tracker.get_value()*DEGREES,arc_center=self.plane.c2p(0,0),radius=0.5,color=YELLOW)
        
        # 创建一个MathTex
        tex=MathTex(r"\theta").move_to(
            Arc(angle=theta_tracker.get_value()*DEGREES,
                arc_center=self.plane.c2p(0,0),
                radius=0.8,color=YELLOW).point_from_proportion(0.5)
        )
        
        # 绘制点A标签
        def get_A_label():
            vector=dot.get_center()-self.plane.c2p(0,0)
            return MathTex(r"A").scale(0.8).move_to(self.plane.c2p(0,0)+1.2*vector)
        A_label=always_redraw(get_A_label)
        
        # 初始化函数
        def initial():
            # 创建点
            self.play(Create(dot))
            self.play(Write(A_label))
            # 创建线
            self.play(Create(line))
            # 添加线
            self.add(a)
            # 写入MathTex
            self.play(Write(tex))
        initial()
        
        # 结束淡出函数
        def end():
            self.play(
                FadeOut(dot),
                Uncreate(A_label),
                Uncreate(line),
                Uncreate(a),
                FadeOut(tex),
            )
                    
        # 更新初始函数
        def update_inital():
            # 添加点更新器
            dot.add_updater(
                lambda x:x.move_to(self.plane.c2p(np.cos(theta_tracker.get_value()*DEGREES),np.sin(theta_tracker.get_value()*DEGREES)))
            )
            # 添加线更新器
            line.add_updater(
                lambda x:x.become(line_ref.copy()).rotate(
                    theta_tracker.get_value()*DEGREES,
                    about_point=self.plane.c2p(0,0)
                ))
            # 添加线更新器
            a.add_updater(
                lambda x: x.become(Arc(angle=theta_tracker.get_value()*DEGREES,arc_center=self.plane.c2p(0,0),radius=0.5,color=YELLOW))
            )

            # 添加MathTex更新器
            tex.add_updater(
                lambda x:x.move_to(
                    Arc(angle=theta_tracker.get_value()*DEGREES,
                        arc_center=self.plane.c2p(0,0),
                        radius=0.8,
                        color=YELLOW).point_from_proportion(0.5)
                )
            )
        update_inital()
            
        # 获取垂直于y轴的线
        def get_line_dot_yzhou():
            # 返回一个线
            return always_redraw(
                lambda :Line(
                    [self.plane.c2p(0,0)[0],dot.get_center()[1],0],
                    dot.get_center(),color=YELLOW)
            ) 
        line_dot_to_y=get_line_dot_yzhou()
        
        # 获取线括号
        def get_b1():
            # 返回一个线
            return always_redraw(
                lambda:Brace(
                    line_dot_to_y,direction=UP,buff=SMALL_BUFF)
                )
        b1=get_b1()
        
        # 获取括号注释
        def get_b1text():
            # 返回一个线
            return always_redraw(
                lambda:b1.get_tex(r"cos\theta").next_to(b1,UP,buff=SMALL_BUFF)
            )
        b1text=get_b1text()
        
        # 获取垂直于x轴的线
        def get_line_dot_xzhou():
            # 返回一个线
            return always_redraw(
                lambda :Line(
                    [dot.get_center()[0],0,0],
                    dot.get_center(),color=YELLOW)
            ) 
        line_dot_to_x=get_line_dot_xzhou()
        
        # 获取线括号
        def get_b2():
            # 返回一个线
            return always_redraw(
                lambda:Brace(
                    line_dot_to_x,direction=RIGHT,buff=SMALL_BUFF)
                )
        b2=get_b2()
        
        # 获取括号注释
        def get_b2text():
            # 返回一个线
            return always_redraw(
                lambda:b2.get_tex(r"sin\theta").next_to(b2,RIGHT,buff=SMALL_BUFF)
            )
        b2text=get_b2text()
        
        def get_theta():
            t0_text=MathTex(r"\theta=").shift(RIGHT*3+UP*2).scale(1.5)
            t0_value=DecimalNumber(theta_tracker.get_value(),num_decimal_places=0,unit="^{\circ}").next_to(t0_text,RIGHT,buff=0.5).scale(1.5)
            
            t0_value.add_updater(lambda x: x.set_value(theta_tracker.get_value()))
            
            t0=VGroup(t0_text,t0_value)
            return t0
        t0=get_theta()
        
        def get_cos():
            t1_text=MathTex(r"cos\theta=").shift(RIGHT*3).scale(1.5)
            t1_value=DecimalNumber(theta_tracker.get_value(),num_decimal_places=2).next_to(t1_text,RIGHT,buff=0.5).scale(1.5)
            
            def update_t1_value(obj):
                obj.set_value(np.cos(theta_tracker.get_value()*DEGREES))
            t1_value.add_updater(update_t1_value)
            t1=VGroup(t1_text,t1_value)
            return t1
        t1=get_cos()
        
        def get_sin():
            t2_text=MathTex(r"sin\theta=").shift(RIGHT*3).scale(1.5)
            t2_value=DecimalNumber(theta_tracker.get_value(),num_decimal_places=2).next_to(t2_text,RIGHT,buff=0.5).scale(1.5)
            
            def update_t2_value(obj):
                obj.set_value(np.sin(theta_tracker.get_value()*DEGREES))
            t2_value.add_updater(update_t2_value)
            t2=VGroup(t2_text,t2_value)
            return t2
        t2=get_sin()
                
        # 开始移动动画函数（先余弦后正弦）
        def start_move_animate():
            # 创建线
            self.play(Create(line_dot_to_y))
            # 创建线
            self.play(Write(b1))
            # 创建线
            self.play(Write(b1text))
            self.play(Write(t0))
            # 创建值
            self.play(FadeIn(t1))
            # 设置值
            self.play(theta_tracker.animate.set_value(-50),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(35),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(120),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(240),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(60),run_time=2)
            self.wait()
            
            #淡出动画
            self.play(
                FadeOut(line_dot_to_y),
                FadeOut(b1),
                FadeOut(b1text),
                FadeOut(t1)
            )
            
            # 正弦动画
            self.play(Create(line_dot_to_x))
            self.play(Write(b2))
            self.play(Write(b2text))
            self.play(FadeIn(t2))
            self.play(theta_tracker.animate.set_value(-50),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(35),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(120),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(240),run_time=2)
            self.wait(0.5)
            self.play(theta_tracker.animate.set_value(60),run_time=2)
            self.wait()
            
            # 淡出动画
            self.play(
                FadeOut(line_dot_to_x),
                FadeOut(b2),
                FadeOut(b2text),
                FadeOut(t2),
                FadeOut(t0)
            )
        start_move_animate()
        end()
        
        

if __name__ == "__main__":
    system("manim {} COS_then_SIN -qp --fps=60 -p".format(__file__))