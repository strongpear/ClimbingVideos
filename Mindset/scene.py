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

        meText = Text("Me", color=YELLOW)
        usText = Text("Us", color=YELLOW).shift(LEFT)
        equalsText = Tex("=")
        studentsText = Text("Students", color=BLUE)
        meArrow = Arrow(LEFT, RIGHT, color=RED)
        studentsArrow = Arrow(LEFT, RIGHT, color=RED)
        
        nameTextGroup = VGroup(meText, studentsText).arrange(DOWN, buff=1.5).shift(LEFT*2)
        arrowGroup = VGroup(meArrow, studentsArrow).arrange(DOWN, buff=1.5).next_to(nameTextGroup, RIGHT)
        whatISay = ["Hi! I'm Mr. Lee.", "You think I don't notice?", "Wow, ya'll are behind. "]
        whatKidsSay = ["Wow, this guy sucks!", "I'm going to cheat :)", "PhotoMath Time!", "Dude, just get me \n through this class."]
        myTextBox = CreateTextBox(whatISay[0]).next_to(meArrow, RIGHT)
        studentsTextBox = CreateTextBox(whatKidsSay[0]).next_to(studentsArrow, RIGHT)


        self.play(GrowFromCenter(nameTextGroup), Create(arrowGroup))
        self.wait(1)
        self.play(GrowFromCenter(myTextBox))
        self.wait(1)
        self.play(GrowFromCenter(studentsTextBox))
        self.wait(1)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[1]).next_to(studentsArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(myTextBox, CreateTextBox(whatISay[1]).next_to(meArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[2]).next_to(studentsArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(myTextBox, CreateTextBox(whatISay[2]).next_to(meArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[3]).next_to(studentsArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(meText, usText.shift(LEFT)), FadeOut(meArrow), Write(equalsText.shift(LEFT*0.5)), studentsText.animate.center().shift(RIGHT*1.5), FadeOut(myTextBox), FadeOut(studentsTextBox), FadeOut(studentsArrow))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

class FourthScene(Scene):
    def construct(self):

        leftCircle = Circle(radius=2,color=BLUE).shift(LEFT*2.5)
        rightCircle = Circle(radius=2).shift(RIGHT*2.5)
        leftLabel = Text("Climbing", color=BLUE).next_to(leftCircle, UP)
        rightLabel = Text("Math", color=RED).next_to(rightCircle, UP)
        leftCircleGroup = VGroup(leftCircle, leftLabel)
        rightCircleGroup = VGroup(rightCircle, rightLabel)


        self.play(Create(leftCircleGroup), Create(rightCircleGroup))
        self.wait(1)    
        self.play(leftCircleGroup.animate.shift(RIGHT), rightCircleGroup.animate.shift(LEFT))
        self.wait(1)

class FifthScene(Scene):
    def construct(self):

        numSteps = 8
        cruxStep = numSteps-3
        titleText = Text("Math", color=RED).to_edge(UP)
        titleText1 = Text("Climbing", color=BLUE).to_edge(UP)
        movementText = Text("Movement Idea", color=GREEN, font_size=24)
        problemText = Text("Single Problem", color=GREEN, font_size=24)
        ellipse = Ellipse(width=3, height=4, color=GREEN)
        ellipseText = Text("Group of Problems", color=GREEN, font_size=24).next_to(ellipse, UP)
        ellipseGroup = VGroup(ellipse, ellipseText)
        mathStepGroup = VGroup()
        climbingStepGroup = VGroup()
        for i in range(numSteps):
            mathStepGroup += Text(f"Step {i+1}", font_size=24)
        
        for i in range(numSteps):
            climbingStepGroup += Text(f"Move {i+1}", font_size=24)

        arrow = Arrow(LEFT, RIGHT)
        self.play(Write(titleText))
        self.play(GrowFromEdge(mathStepGroup.arrange(DOWN), UP))
        self.wait(1)
        self.play(Indicate(mathStepGroup[cruxStep], color=GREEN))
        self.play(Transform(mathStepGroup[cruxStep], Text("Key Step", font_size=24, color=GREEN).move_to(mathStepGroup[cruxStep].get_center())))
        self.wait(1)
        self.play(ReplacementTransform(mathStepGroup, climbingStepGroup.arrange(DOWN)), Transform(titleText, titleText1))
        self.wait(1)
        self.play(Indicate(climbingStepGroup[cruxStep], color=GREEN))
        self.play(Transform(climbingStepGroup[cruxStep], Text("Crux Move", font_size=24, color=GREEN).move_to(climbingStepGroup[cruxStep].get_center())))
        self.wait(1)
        self.play(*[FadeOut(climbingStepGroup[i]) for i in range(numSteps) if i !=cruxStep], climbingStepGroup[cruxStep].animate.center().shift(LEFT*2), GrowArrow(arrow))
        self.wait(1)
        self.play(Write(movementText.next_to(arrow, RIGHT)))
        self.wait(1)

        myGroup = VGroup(climbingStepGroup[cruxStep], movementText)
        self.play(Swap(*myGroup))
        self.play(ReplacementTransform(climbingStepGroup[cruxStep], problemText.next_to(arrow, RIGHT)))
        self.wait(1)
        self.play(ReplacementTransform(problemText, ellipseGroup.next_to(arrow, RIGHT)))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)
class SixthScene(ThreeDScene):
    def construct(self):

        # Define all of the Mobjects
        circle = Circle(radius = 1.5, color = BLUE)
        circle.set_fill(BLUE, opacity = 0.8)
        sphere = Sphere(radius = 1.5) # Sphere "top-down perspective"


        self.set_camera_orientation(phi = 0, theta = 0)
        self.play(Create(circle))
        self.wait(2)
        self.play(ReplacementTransform(circle, sphere)) # Transform circle to sphere
        self.move_camera(phi = PI / 3)
        self.begin_ambient_camera_rotation(rate = 0.1) # Rotate around object
        self.wait(12)
        self.play(Uncreate(sphere))
        self.wait()

class SeventhScene(Scene):
    def construct(self):
        text = Text("Beta")
        text1 = Text("= PhotoMath")

        self.play(Write(text))
        self.play(text.animate.shift(LEFT))
        self.play(Write(text1.next_to(text, RIGHT)))
        self.wait(1)

class EighthScene(Scene):

    def construct(self):
        thankYou = Text("Thanks for Watching!", color=BLUE)
        dot = Dot()
        circle = Circle(radius=0.8, color=RED)

        self.play(Write(thankYou))
        self.play(thankYou.animate.shift(UP*1.5))
        self.play(Create(dot))
        self.play(GrowFromCenter(circle))
        self.play(dot.animate.shift(RIGHT*0.8))
        for i in range(5):
            self.play(MoveAlongPath(dot, circle), run_time=3, rate_func=linear)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)
def CreateTextBox(text):
    boxText = Text(text, font_size=24)
    textBox = SurroundingRectangle(boxText)
    textGroup = VGroup(boxText, textBox)
    return textGroup