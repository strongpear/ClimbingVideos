from manim import *

class FirstScene(Scene):
    def construct(self):

        # Text
        textPerformance = Text('Climbing Performance')
        textPhysical = Text('Physical', color=RED).shift(LEFT*3)
        textMental = Text('Mental', color=BLUE).shift(RIGHT*3)
        textGroup = VGroup(textPhysical, textMental)

        # Rectangles
        red_rect = Rectangle(width=3.5, height=3, color=RED, fill_color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width=1.5, height=3, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        red_rect.shift(LEFT * 1.5)
        blue_rect.shift(RIGHT * 1.5)
        rectGroup = VGroup(red_rect, blue_rect).shift(DOWN)

        # Second Set of Rectangles
        red_rect1 = Rectangle(width=2.5, height=3, color=RED, fill_color=RED, fill_opacity=0.8).shift(LEFT*1.5)
        blue_rect1 = Rectangle(width=2.5, height=3, color=BLUE, fill_color=BLUE, fill_opacity=0.8).shift(RIGHT*1.5)
        rectGroup1 = VGroup(red_rect1, blue_rect1).shift(DOWN)
       
        
        # Animate
        self.play(Write(textPerformance), remover=False)
        self.wait(10)
        self.play(textPerformance.animate.shift(UP*3))
        self.play(Write(textGroup))
        self.wait(5)
        self.play(textGroup.animate.shift(UP*1.5))
        self.play(Create(rectGroup1))
        self.wait(1)
        self.play(Transform(rectGroup1, rectGroup))
        self.wait(5)
        self.play(FadeOut(textPerformance, textGroup, rectGroup1))
        self.wait(1)

class SecondScene(Scene):
    def construct(self):
        
        # Constants
        gradeScaling = 0.8
        physicalGrades = [5, 10]
        mental = [0.4, 0.98]

        # Text
        textPhysical = Text('Physical', color=RED, font_size=36)
        textMental = Text('Mental', color=BLUE, font_size=36)
        textReal = Text('Real Grade', color=GREEN, font_size=36)
        textGroup = VGroup(textPhysical, textMental, textReal).arrange(direction=RIGHT, aligned_edge=UP, buff=1.5).to_edge(UP)
        
        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)

        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))

        # Animate
        self.play(Write(textGroup))
        self.wait(1)
        self.play(Create(rectGroup))
        self.wait(3)
        self.play(Write(labelGroup))
        self.wait(1)
        self.play(rectGroup.animate.stretch(1.6, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(blue_rect.animate.stretch(1.5, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(FadeOut(textGroup, rectGroup, labelGroup))
        self.wait(1)

class ThirdScene(Scene):
    def construct(self):
        
        # Constants
        gradeScaling = 0.8
        physicalGrades = [5, 10]
        mental = [0.2, 0.98]
        
        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)


        # Names
        firstName = Text("Alex").to_edge(UP)
        secondName = Text("Carson").shift(DOWN*0.25)
        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)
        nameGroup = VGroup(firstName, secondName)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))


        self.play(Write(nameGroup))
        self.wait(3)
        self.play(Create(rectGroup.shift(UP*1.5+LEFT*0.5)))
        self.play(Write(labelGroup.shift(UP*1.5+LEFT*0.5)))
         
        self.play(rectGroup.animate.stretch(1.2, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(blue_rect.animate.stretch(2.5, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(5)


        # Carson code

        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)


        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)
        nameGroup = VGroup(firstName, secondName)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))


        self.play(Create(rectGroup.shift(DOWN*2+LEFT*0.5)))
        self.play(Write(labelGroup.shift(DOWN*2+LEFT*0.5)))
        self.wait(8)
        self.play(rectGroup.animate.stretch(1.6, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(3)
        self.play(blue_rect.animate.stretch(1.25, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(8)
        self.play(*[FadeOut(mob) for mob in self.mobjects])




class FourthScene(Scene):
    def construct(self):
        
        # Drew

        # Constants
        gradeScaling = 0.8
        physicalGrades = [10]
        mental = [0.95]
        
        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(DOWN + RIGHT) + 0.5 * red_rect.get_height() * DOWN)


        # Names
        firstName = Text("Drew").to_edge(UP)
        secondName = Text("Taylor").shift(DOWN*0.25)
        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)
        nameGroup = VGroup(firstName, secondName)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(DOWN + RIGHT) + 0.5 * red_rect.get_height() * DOWN))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))


        self.play(Write(nameGroup))
        self.wait(3)
        self.play(Create(rectGroup.shift(UP*1.5+LEFT*0.5)))
        self.play(Write(labelGroup.shift(UP*1.5+LEFT*0.5)))
        self.wait(8)
        self.play(rectGroup.animate.stretch(1.2, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(3)
        self.play(blue_rect.animate.stretch(1.01, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(3)


        # Taylor

        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(DOWN + RIGHT) + 0.5 * red_rect.get_height() * DOWN)


        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)
        nameGroup = VGroup(firstName, secondName)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(DOWN + RIGHT) + 0.5 * red_rect.get_height() * DOWN))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))


        self.play(Create(rectGroup.shift(DOWN*2+LEFT*0.5)))
        self.play(Write(labelGroup.shift(DOWN*2+LEFT*0.5)))
        self.wait(6)
        self.play(rectGroup.animate.stretch(1.02, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(2)
        self.play(blue_rect.animate.stretch(1.03, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(10)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class FifthScene(ThreeDScene):
    def construct(self):
        title = Text("What About Us?")

        # Define all of the Mobjects
        circle = Circle(radius = 1, color = BLUE)
        circle.set_fill(BLUE, opacity = 0.8)
        sphere = Sphere(radius = 1) # Sphere "top-down perspective"

        # Animate
        self.play(Write(title))
        self.wait()
        self.play(ApplyMethod(title.to_edge, UP)) # Move text to upper left corner
        self.add_fixed_in_frame_mobjects(title) # Fix text so it doesnt transform
        self.set_camera_orientation(phi = 0, theta = 0)
        self.play(Create(circle))
        self.wait(2)
        self.play(ReplacementTransform(circle, sphere)) # Transform circle to sphere
        self.move_camera(phi = PI / 3)
        self.begin_ambient_camera_rotation(rate = 0.1) # Rotate around object
        self.wait(12)
        self.play(FadeOut(title), Uncreate(sphere))
        self.wait()

class SixthScene(Scene):
    def construct(self):
        
        # Constants
        gradeScaling = 0.8
        physicalGrades = [5, 10]
        mental = [0.4, 0.98]

        # Rectangles
        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        # Labels
        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)

        # Groups
        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)

        # Update Functions
        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))

        # Animate

        self.play(Create(rectGroup))
        self.play(Write(labelGroup))
        self.wait(1)
        self.play(rectGroup.animate.stretch(1.25, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(2)
        self.play(rectGroup.animate.stretch(0.8, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.play(blue_rect.animate.stretch(1.25, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(2)
        self.play(blue_rect.animate.stretch(0.8, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(10)
        self.play(FadeOut(rectGroup, labelGroup))
        self.wait(1)
class SeventhScene(Scene):

    def construct(self):
        howText = Text("Mental Training?", color=RED)
        thankYou = Text("Thanks for Watching!", color=BLUE)
        dot = Dot()
        circle = Circle(radius=0.8, color=RED)

        self.play(Write(howText))
        self.wait(13)
        self.play(Transform(howText, thankYou))
        self.play(howText.animate.shift(UP*1.5))
        self.play(Create(dot))
        self.play(GrowFromCenter(circle))
        self.play(dot.animate.shift(RIGHT*0.8))
        for i in range(5):
            self.play(MoveAlongPath(dot, circle), run_time=3, rate_func=linear)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)
        