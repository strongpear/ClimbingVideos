from manim import *

class FirstScene(Scene):
    def construct(self):
        initialText = Text("Mindset")


        # Text
        initialText1 = Text('Previously...')
        # Constants
        gradeScaling = 0.8
        physicalGrades = [5, 10]
        mental = [0.4, 0.98]

        # Text
        textPhysical = Text('Physical', color=RED, font_size=36)
        textMental = Text('Mental', color=BLUE, font_size=36)
        textReal = Text('Real Grade', color=GREEN, font_size=36)
        textGroup = VGroup(textPhysical, textMental, textReal).arrange(direction=RIGHT, aligned_edge=UP, buff=1.5).to_edge(UP)
        textImprove = Text("Improving Mental Game?", color=BLUE, font_size=36)
        t1 = Text("Mindset", color=YELLOW, font_size=24)
        t2 = Text("Intuition", color=YELLOW, font_size=24)
        t3 = Text("Visualization", color=YELLOW, font_size=24)
        t4 = Text("Tactics", color=YELLOW, font_size=24)

        tGroup = VGroup(t1, t2, t3, t4).arrange(RIGHT)
        
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
       
        self.add(initialText)
        self.wait(12)
        self.play(Transform(initialText, initialText1))
        self.wait(2)
        self.play(initialText.animate.to_edge(UP))
        # Animate
        self.play(Write(textGroup.next_to(initialText, DOWN)))
        self.wait(1)
        self.play(Create(rectGroup))
        self.wait(3)
        self.play(Write(labelGroup))
        self.wait(1)
        self.play(rectGroup.animate.stretch(1.6, dim=0, about_edge=LEFT), UpdateFromFunc(physicalLabel, update_phys_label), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(blue_rect.animate.stretch(1.5, dim=0, about_edge=LEFT), UpdateFromFunc(realLabel, update_real_label), UpdateFromFunc(mentalLabel, update_mental_label))
        self.wait(1)
        self.play(FadeOut(textGroup, rectGroup, labelGroup), Transform(initialText, textImprove))
        self.wait(6)
        self.play(GrowFromCenter(tGroup.shift(DOWN)))
        self.wait(4)
        self.play(FadeOut(initialText), FadeOut(tGroup))
        self.wait(2)





class SecondScene(Scene):
    def construct(self):

        firstText = Text("Fixed vs Growth Mindset?")
        crossThrough = Line(start=firstText.get_left(), end=firstText.get_right(), color=RED)
        arrow = Arrow(UP, DOWN)
        firstTextGroup = VGroup(firstText, crossThrough)
        secondText = Text("Learning", color=BLUE).shift(DOWN*2)


        self.play(Write(firstText))
        self.wait(2)
        self.play(Create(crossThrough))
        self.wait(4)
        self.play(firstTextGroup.animate.shift(UP*2), GrowArrow(arrow), GrowFromCenter(secondText))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

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
        whatISay = ["Hi! I'm Mr. Lee.", "You think I don't notice?", "Wow, ya'll are behind. ", "It's not your fault :("]
        whatKidsSay = ["Wow, this guy sucks!", "I'm going to cheat :)", "PhotoMath Time!", "We literally don't care...", "Yeah, It's been hard lately."]
        myTextBox = CreateTextBox(whatISay[0]).next_to(meArrow, RIGHT)
        studentsTextBox = CreateTextBox(whatKidsSay[0]).next_to(studentsArrow, RIGHT)


        self.play(GrowFromCenter(nameTextGroup), Create(arrowGroup))
        self.play(GrowFromCenter(myTextBox))
        self.wait(5)
        self.play(GrowFromCenter(studentsTextBox))
        self.wait(2)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[1]).next_to(studentsArrow, RIGHT)))
        self.wait(1)
        self.play(Transform(myTextBox, CreateTextBox(whatISay[1]).next_to(meArrow, RIGHT)))
        self.wait(4)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[2]).next_to(studentsArrow, RIGHT)))
        self.wait(12)
        self.play(Transform(myTextBox, CreateTextBox(whatISay[2]).next_to(meArrow, RIGHT)))
        self.wait(9)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[3]).next_to(studentsArrow, RIGHT)))
        self.wait(9)
        self.play(Transform(myTextBox, CreateTextBox(whatISay[3]).next_to(meArrow, RIGHT)))
        self.wait(2)
        self.play(Transform(studentsTextBox, CreateTextBox(whatKidsSay[4]).next_to(studentsArrow, RIGHT)))
        self.wait(2)
        self.play(Transform(meText, usText.shift(LEFT)), FadeOut(meArrow), Write(equalsText.shift(LEFT*0.5)), studentsText.animate.center().shift(RIGHT*1.5), FadeOut(myTextBox), FadeOut(studentsTextBox), FadeOut(studentsArrow))
        self.wait(10)
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
        myText = Text("Pattern Recognition \n\n Critical Thinking", color=GREEN)
        intersection = Intersection(leftCircle, rightCircle, color=GREEN, fill_opacity=0)
        myLeftText = Text("Concepts", color=BLUE).shift(DOWN + LEFT*4)
        myRightText = Text("Techniques", color=RED).shift(DOWN + RIGHT*4)
        myLeftArrow = Arrow(start=leftLabel.get_corner(DR), end=myLeftText.get_edge_center(UP))
        myRightArrow = Arrow(start=rightLabel.get_corner(DL), end=myRightText.get_edge_center(UP))
        
        self.play(Create(leftCircleGroup), Create(rightCircleGroup))
        self.wait(1)    
        self.play(leftCircleGroup.animate.shift(RIGHT), rightCircleGroup.animate.shift(LEFT))
        self.wait(1)
        intersection = Intersection(leftCircle, rightCircle, color=GREEN, fill_opacity=0)
        self.add(intersection)
        self.play(Indicate(intersection))
        self.wait(1)
        self.play(Transform(intersection, myText), FadeOut(leftCircle), FadeOut(rightCircle))
        self.wait(2)
        self.play(FadeOut(intersection))
        self.play(GrowArrow(myLeftArrow))
        self.play(GrowFromCenter(myLeftText))
        self.play(GrowArrow(myRightArrow))
        self.play(GrowFromCenter(myRightText))
        self.wait(2)
        textGroup = VGroup(leftLabel, rightLabel)
        problemsText = Text("Problems", color=GREEN)
        self.play(ReplacementTransform(textGroup, problemsText.move_to(textGroup.get_center()).shift(RIGHT*0.5)))
        self.wait(2)
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