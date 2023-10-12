from manim import*
class Pith(scene):
    def construct(self):
        sq=Square(side_lenght=5,stroke_color=GREEN,fill_color=BLUE,fill_opacity=0.75)
        self.play(Create(sq),run_time=3)
        self.wait()
