#Author : Hossam Ahmed Fouad(DedSec)
#Date   : 12-6-2021

from manim import *


class MyWork(MovingCameraScene):
    def construct(self):
        title = Text("Given: ")
        givenEquation = MathTex(
            r"y^{\frac{1}{r}} - y^{\frac{-1}{r}} = x"
        )
        title2 = Text("Show That: ")
        toShowEquation = MathTex(
            r"(x^2+4)y\prime \prime + xy\prime - r^2y = 0"
        )
        title.shift(2 * LEFT)
        title.shift(2 * UP)
        givenEquation.next_to(title, DOWN + RIGHT)
        title2.next_to(givenEquation, DOWN + LEFT)
        toShowEquation.next_to(title2, DOWN + RIGHT)

        self.play(Write(title), Write(givenEquation))
        self.play(Write(title2), Write(toShowEquation))
        self.wait(3)
        title2.to_corner(UP + RIGHT)
        toShowEquation.scale(0.70)
        title2.scale(0.70)
        self.play(FadeOut(title), FadeOut(givenEquation), title2.animate.to_corner(UP + RIGHT),
                  toShowEquation.animate.next_to(title2, DOWN))
        self.wait()

        start = MathTex(
            r"y^{\frac{1}{r}} - y^{\frac{-1}{r}} = x"
        )
        self.play(FadeIn(start))
        self.wait()
        commstep1 = Text("Multiply By ", font_size=20)
        muliply = MathTex(r"y^{\frac{1}{r}}")
        commstep1.next_to(start, RIGHT)
        commstep1.shift(2 * RIGHT)
        muliply.next_to(commstep1, RIGHT)
        self.play(FadeIn(commstep1), FadeIn(muliply))
        self.wait()

        step1 = MathTex(
            r"y^{\frac{2}{r}} - 1 = xy^{\frac{1}{r}}"
        )
        step1.next_to(start, DOWN)
        self.play(Write(step1))
        self.wait()
        self.play(FadeOut(commstep1), FadeOut(muliply), Transform(start, step1))
        self.play(FadeOut(start), step1.animate.shift(1 * UP))
        self.wait()
        step1B = step1.copy()
        self.add(step1B)
        box = SurroundingRectangle(step1B, buff=.1)
        box.set_color(BLUE_D)
        self.play(Create(box))
        group = VGroup(box, step1B)
        self.play(group.animate.to_corner(UP + LEFT))
        self.wait()
        commstep2 = Text("Differentiate with respect to x on both sides", font_size=15)
        commstep2.next_to(step1, RIGHT)
        commstep2.shift(1 * RIGHT)
        self.play(FadeIn(commstep2))
        self.wait()
        step2 = MathTex(
            r"y\prime \frac{\frac{2}{r}y^{\frac{2}{r}}}{y} = y^{\frac{1}{r}} + y\prime \frac{xy^{\frac{1}{r}}}{y}\frac{1}{r}}"
        )
        step2.next_to(step1, DOWN)
        self.play(Write(step2, run_time=6))
        self.wait(2)
        self.play(Transform(step1, step2), FadeOut(commstep2))
        self.play(FadeOut(step1), step2.animate.shift(1 * UP))
        self.wait()
        step2Simplified = MathTex(
            r"y \prime \frac{ 2y^{ \frac{2}{r} } }{ry} = y^{\frac{1}{r}} + \frac{ xy^{ \frac{1}{r} } y\prime }{y} \frac{1}{r}"
        )
        step2Simplified.next_to(step2, DOWN)
        self.play(Write(step2Simplified))
        self.wait()
        self.play(Transform(step2, step2Simplified))
        self.wait()
        self.play(step2Simplified.animate.shift(2 * UP), FadeOut(step2))
        self.wait()
        commstep3 = Text("Multiply Both Sides By ry", font_size=20)
        commstep3.next_to(step2Simplified, RIGHT)
        commstep3.shift(0 * RIGHT)
        self.play(FadeIn(commstep3))
        self.wait()
        step3 = MathTex(
            r"y \prime 2y^{\frac{2}{r}} = ryy^{\frac{1}{r}} + xy^{\frac{1}{r}}y\prime"
        )
        step3.next_to(step2Simplified, DOWN)
        self.play(Write(step3, run_time=3))
        self.wait()
        self.play(FadeOut(commstep3), Transform(step2Simplified, step3))
        self.play(step3.animate.shift(1 * UP), FadeOut(step2Simplified))
        self.wait()

        commstep4 = Text("Spearate y prime on one side", font_size=20)
        commstep4.next_to(step3, RIGHT)
        self.play(FadeIn(commstep4))
        self.wait()
        step4 = MathTex(
            r"y\prime", r"(2y^{\frac{2}{r}}-xy^{\frac{1}{r}})", "=", r"ryy^{\frac{1}{r}}"
        )
        step4Real = MathTex(
            r"y\prime", r"(1+y^{\frac{2}{r}})", "=", r"ryy^{\frac{1}{r}}"
        )
        step4Real.next_to(step4, DOWN)
        mArrow = CurvedArrow(start_point=[-1,-1,-5], end_point=[-3,3,-8])
        step4Main = MathTex(
            r"y\prime", r"(1+y^{\frac{2}{r}})", "=", r"ryy^{\frac{1}{r}}"
        )
        step4Main.next_to(step3, DOWN)
        step4.next_to(step3, DOWN)
        self.play(Write(step4, run_time=3))
        self.wait()
        self.play(Create(mArrow,run_time=2))
        self.wait()
        self.play(Transform(step4,step4Real),FadeOut(mArrow))
        self.wait()
        self.play(step4[1].animate.next_to(step4[3], DOWN), step4[2].animate.next_to(step4[0], RIGHT))
        step4Simplified = MathTex(
            r"y\prime = \frac{ryy^{\frac{1}{r}}}{1+y^{\frac{2}{r}}}"
        )
        step4Simplified.next_to(step3, DOWN)
        self.play(FadeTransform(step4, step4Simplified))
        self.wait()
        step4SimplifiedB = step4Simplified.copy()
        self.add(step4Simplified)
        box2 = SurroundingRectangle(step4SimplifiedB, buff=.1)
        box2.set_color(BLUE_D)
        self.play(Create(box2))
        group2 = VGroup(step4SimplifiedB, box2)
        self.play(group2.animate.next_to(group, DOWN))
        self.wait()
        self.play(Transform(step4Simplified, step4Main))
        self.play(Transform(step3, step4Main))
        self.play(step4Main.animate.shift(1 * UP), FadeOut(commstep4), FadeOut(step4), FadeOut(step3),
                  FadeOut(step4Simplified))
        self.wait()
        commstep5 = Text("Differentiate with respect to x on both sides", font_size=15)
        commstep5.next_to(step4Main,RIGHT)
        self.play(FadeIn(commstep5))
        self.wait()
        step5 = MathTex(
            r"y\prime \prime (1+y^{\frac{2}{r}}) + y\prime (\frac{2y^{\frac{2}{r}}y\prime }{ry}) = ry\prime y^{\frac{1}{r}}+ry  \frac{y^{\frac{1}{r}}}{ry} y\prime"
        )
        step5.next_to(step4Main,DOWN)
        self.play(Write(step5,run_time=6))
        self.wait()
        self.play(Transform(step4Main,step5))
        self.wait()
        self.play(step5.animate.shift(1*UP),FadeOut(step4Main),FadeOut(commstep5))
        self.wait()
        step5Simplified = MathTex(
            r"y\prime \prime (1+y^{\frac{2}{r}}) + y\prime (\frac{2y^{\frac{2}{r}}y\prime }{ry}) = ry\prime y^{\frac{1}{r}} + ", r"y^{\frac{1}{r}}" + "y\prime"
        )
        self.play(ReplacementTransform(step5,step5Simplified))
        self.play(FadeOut(step5))
        self.wait()
        commstep6 = Text("Multiply Both sides by ry" ,font_size=15)
        commstep6.next_to(step5,RIGHT)
        self.play(FadeIn(commstep6))
        self.wait()
        step6 = MathTex(
            r"y\prime \prime (1+y^{\frac{2}{r}})ry+y\prime (2y^{\frac{2}{r}}y\prime)=r^2yy^{\frac{1}{r}}y\prime+ryy\prime y^{\frac{1}{r}}"

        )
        step6.next_to(step5,DOWN)
        self.play(Write(step6,run_time=6))
        self.wait()
        self.play(Transform(step5Simplified,step6))
        self.wait()
        self.play(step6.animate.shift(1*UP),FadeOut(step5Simplified),FadeOut(commstep6))
        self.wait()
        commstep7 = Text("Take y prime common factor",font_size=15)
        commstep7.next_to(step6,UP)
        self.play(FadeIn(commstep7))
        self.wait()
        step7 = MathTex(
            r"\frac{y\prime \prime (1+y^{\frac{2}{r}})ry}{y\prime} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"
        )
        step7.next_to(step6,DOWN)
        self.play(Write(step7,run_time=6))
        self.wait()
        self.play(Transform(step6,step7))
        self.play(FadeOut(commstep7),FadeOut(step6),step7.animate.shift(1*UP))
        self.wait()
        mArrow2 = CurvedArrow(start_point=[-2, -1, -5], end_point=[-3, 2, -8])
        self.play(Create(mArrow2))
        self.wait()
        self.play(FadeOut(mArrow2))
        step8 = MathTex(
            r"\frac{y\prime \prime (1+y^{\frac{2}{r}})ry}{\frac{ryy^{\frac{1}{r}}}{1+y^{\frac{2}{r}}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step8.next_to(step7,DOWN)
        self.play(Write(step8))
        self.wait()
        step8B = MathTex(
            r"\frac{y\prime \prime (1+y^{\frac{2}{r}})^2}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step8B.next_to(step7,DOWN)
        self.play(Transform(step8,step8B))
        self.wait()
        self.play(Transform(step7,step8B))
        self.play(FadeOut(step7),FadeOut(step8),step8B.animate.shift(1*UP))
        self.wait()
        mArrow3 = CurvedArrow(start_point=[-2, 0, -5], end_point=[-3, 3, -8])
        self.play(Create(mArrow3))
        self.wait()
        self.play(FadeOut(mArrow3))
        self.wait()

        step9 = MathTex(
            r"\frac{y\prime \prime (xy^{\frac{1}{r}}+2)^2}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step9.next_to(step8B,DOWN)
        self.play(Transform(step8B,step9))
        self.wait()
        self.play(FadeOut(step8B),step9.animate.shift(1*UP))
        self.wait()
        step10 = MathTex(
            r"\frac{y\prime \prime (x^2y^{\frac{2}{r}}+4xy^{\frac{1}{r}} + 4)}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step10.next_to(step9,DOWN)
        self.play(Transform(step9,step10))
        self.play(FadeOut(step9),step10.animate.shift(2*UP))
        self.wait()
        mArrow4 = CurvedArrow(start_point=[-3, 0, -5], end_point=[-3, 3, -8])
        self.play(Create(mArrow4))
        self.wait()
        self.play(FadeOut(mArrow4))
        step11 = MathTex(
            r"\frac{y\prime \prime (x^2(xy^{\frac{1}{r}}+1)+4(xy^{\frac{1}{r}} + 1)}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step11.next_to(step10,DOWN)
        self.play(Write(step11))
        self.play(Transform(step10,step11))
        self.wait()
        self.play(FadeOut(step10),step11.animate.shift(2*UP))
        self.wait()
        step12 = MathTex(
            r"\frac{y\prime \prime (x^2+4)(xy^{\frac{1}{r}}+1)}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step12.next_to(step11,DOWN)
        self.play(Write(step12))
        self.wait()
        self.play(Transform(step11,step12))
        self.play(FadeOut(step11),step12.animate.shift(2*UP))
        self.wait()
        step13 = MathTex(
            r"\frac{y\prime \prime (x^2+4)(y^{\frac{2}{r}})}{y^{\frac{1}{r}}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step13.next_to(step12,DOWN)
        self.play(Write(step13))
        self.play(Transform(step12,step13))
        self.play(FadeOut(step12),step13.animate.shift(1*UP))
        self.wait()

        step14 = MathTex(
            r"y\prime \prime (x^2+4)y^{\frac{1}{r}} + y\prime (2y^{\frac{2}{r}}) = r^2yy^{\frac{1}{r}} + ryy^{\frac{1}{r}}"

        )
        step14.next_to(step13,DOWN)
        self.play(Write(step14))
        self.play(Transform(step13,step14))
        self.play(FadeOut(step13),step14.animate.shift(2*UP))
        self.wait()

        step15 = MathTex(
            r"y\prime \prime (x^2+4) + y\prime (2y^{\frac{1}{r}}) = r^2y+ ry"

        )

        step15.next_to(step14,DOWN)
        self.play(Write(step15))
        self.play(Transform(step14,step15))
        self.play(FadeOut(step14),step15.animate.shift(1*UP))
        self.wait()

        step16 = MathTex(
            r"ry = y\prime (1+y^{\frac{2}{r}})y^{\frac{-1}{r}}"
        )
        step16.next_to(step15,DOWN)
        self.play(Write(step16))
        step17 = MathTex(
            r"y\prime \prime (x^2+4) + y\prime (2y^{\frac{1}{r}}) - y\prime (1+y^{\frac{2}{r}})y^{\frac{-1}{r}} = r^2y"

        )
        step17.next_to(step16,DOWN)
        self.play(Write(step17))
        self.play(FadeOut(step16),Transform(step15,step17))
        self.wait()
        self.play(FadeOut(step16),step17.animate.shift(2*UP),FadeOut(step15))
        self.wait()

        step18 = MathTex(
            r"y\prime \prime (x^2+4) + y\prime (2y^{\frac{1}{r}} -y^{\frac{-1}{r}} -y^{\frac{1}{r}}) = r^2y"

        )
        step18.next_to(step17,DOWN)
        self.play(Write(step18))
        self.play(Transform(step17,step18))
        self.play(FadeOut(step17), step18.animate.shift(1*UP))
        self.wait()

        step19 = MathTex(
            r"y\prime \prime (x^2+4) + xy\prime - r^2y = 0 "

        )
        step19.next_to(step18,DOWN)
        self.play(Write(step19))
        self.play(Transform(step18,step19))
        self.wait()
        self.play(FadeOut(step18),step19.animate.shift(2*UP))
        self.wait()

        author = Text("Created By: Hossam Ahmed Fouad")
        self.play(Write(author,run_time=3))
        self.wait()



