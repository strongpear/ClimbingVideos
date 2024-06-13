from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class FirstScene(Scene):
    def construct(self):

        # Objects   
        textPerformance = Text('Climbing Performance')
        textPhysical = Text('Physical', color=RED).shift(LEFT*3)
        textMental = Text('Mental', color=BLUE).shift(RIGHT*3)
        textGroup = VGroup(textPhysical, textMental)

        red_rect = Rectangle(width=1.5, height=3, color=RED, fill_color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width=3.5, height=3, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        red_rect.shift(LEFT * 1.5)
        blue_rect.shift(RIGHT * 1.5)
        rectGroup = VGroup(red_rect, blue_rect).shift(DOWN)


        red_rect1 = Rectangle(width=2.5, height=3, color=RED, fill_color=RED, fill_opacity=0.8).shift(LEFT*1.5)
        blue_rect1 = Rectangle(width=2.5, height=3, color=BLUE, fill_color=BLUE, fill_opacity=0.8).shift(RIGHT*1.5)
        rectGroup1 = VGroup(red_rect1, blue_rect1).shift(DOWN)
        # Add the rectangles to the scene
        
        # Animation
        self.play(Write(textPerformance), remover=False)
        self.play(textPerformance.animate.shift(UP*3))
        self.play(Write(textGroup))
        self.play(textGroup.animate.shift(UP*1.5))
        self.play(Create(rectGroup))
        self.play(Transform(rectGroup, rectGroup1))
        self.wait(1)
        self.play(FadeOut(textPerformance, textGroup, rectGroup1))
        self.wait(1)

class SecondScene(Scene):
    def construct(self):

        gradeScaling = 0.8
        physicalGrades = [5, 10]
        mental = [0.2, 0.98]

        
        textPhysical = Text('Physical', color=RED, font_size=36)
        textMental = Text('Mental', color=BLUE, font_size=36)
        textReal = Text('Real Grade', color=GREEN, font_size=36)
        textGroup = VGroup(textPhysical, textMental, textReal).arrange(direction=RIGHT, aligned_edge=UP, buff=1.5).to_edge(UP)
        

        red_rect = Rectangle(width = physicalGrades[0] * gradeScaling, height=1, color=RED, fill_opacity=0.8)
        blue_rect = Rectangle(width = physicalGrades[0] * gradeScaling * mental[0], height=1, color=BLUE, fill_opacity=0.8).align_to(red_rect, LEFT)

        physicalLabel = Tex(red_rect.width/gradeScaling, color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)
        mentalLabel = Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center())
        realLabel = Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP)

        rectGroup = VGroup(red_rect, blue_rect)
        labelGroup = VGroup(physicalLabel,mentalLabel,realLabel)

        def update_phys_label(label):
            label.become(Tex(round(red_rect.width/gradeScaling, 2), color=RED).move_to(red_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_real_label(label):
            label.become(Tex(round(blue_rect.width/gradeScaling, 2), color=GREEN).move_to(blue_rect.get_corner(UP + RIGHT) + 0.5 * red_rect.get_height() * UP))
        def update_mental_label(label):
            label.become(Tex(round(blue_rect.width/red_rect.width, 2), color=WHITE).move_to(blue_rect.get_center()))

        self.play(Write(textGroup))
        self.play(Create(rectGroup))
        self.play(Write(labelGroup))
        self.wait(1)
        self.play(rectGroup.animate.stretch(1.6, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(blue_rect.animate.stretch(2.5, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)