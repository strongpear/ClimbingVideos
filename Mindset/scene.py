from manim import *

class FirstScene(Scene):
    def construct(self):
        initialText = Text("Mindset")


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
       
        self.add(initialText)
        self.wait(10)
        # Animate
        self.play(Transform(initialText, textPerformance), remover=False)
        self.wait(10)
        self.play(initialText.animate.shift(UP*3))
        self.play(Write(textGroup))
        self.wait(5)
        self.play(textGroup.animate.shift(UP*1.5))
        self.play(Create(rectGroup1))
        self.wait(1)
        self.play(Transform(rectGroup1, rectGroup))
        self.wait(5)
        self.play(FadeOut(textPhysical, rectGroup1, initialText))
        self.wait(1)
        self.play(textMental.animate.move_to(ORIGIN))
        self.wait(10)
        self.play(FadeOut(textMental))


class SecondScene(Scene):
    def construct(self):
        firstText = Text("Fixed vs Growth Mindset")
        crossThrough = Line(start=firstText.get_left(), end=firstText.get_right(), color=RED)
        arrow = Arrow(UP, DOWN)
        firstTextGroup = VGroup(firstText, crossThrough)
        secondText = Text("Learning", color=BLUE).shift(DOWN*2)
        self.add(firstText)
        self.wait(1)
        self.play(Create(crossThrough))
        self.wait(1)
        self.play(firstTextGroup.animate.shift(UP*2), GrowArrow(arrow), GrowFromCenter(secondText))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
class ThirdScene(Scene):
    def construct(self):
        meText = Text("Me", color=YELLOW).to_corner(DL)
        studentsText = Text("Students").to_corner(DR)
        whatISay = [Text("Hi! I'm Mr. Lee."), Text("You think I can't tell?")]
        whatKidsSay = [Text("Wow, this guy sucks!"), Text("I'm going to cheat on every assignment..."), Text("PhotoMath Time!")]

        self.play(GrowFromCenter(meText), GrowFromCenter(studentsText))
        self.wait(1)
