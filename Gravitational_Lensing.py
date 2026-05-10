%%manim -v WARNING -r 1920,1080 -pqh  Gravitational_Lensing

from manim import *
class Gravitational_Lensing(Scene):
    def construct(self):
        title=Text("Gravitational Lensing")
        title.move_to(UP*5)
        title.scale(1)
        self.camera.background_color = BLACK
        # core
        core = Circle(radius=1)
        core.set_fill("#FFF7B0", opacity=1)
        core.set_stroke(width=0)
        # smooth gradient layers
        glow = VGroup()
        n = 15  # more layers = more smooth merge
        for i in range(n):
            r = 1 + i * 0.08
            opacity = 0.25 * (1 - i/n)  # fade outward
            c = Circle(radius=r)
            c.set_fill("#FF8C00", opacity=opacity)
            c.set_stroke(width=0)
            glow.add(c)
        self.add(glow, core)
        straight = Line([-5,3,0], [-3,3,0])
        base_line=DashedLine([-3,3,0],[8,3,0])
        photon = Dot(color=YELLOW).move_to(straight.get_start())
        photon_path=ParametricFunction(lambda m : np.array([m,0.04*-(m+3)**2+3,0]),t_range=(-3,8))
        trace = TracedPath(photon.get_center, stroke_width=4)
        # motion
        self.add(base_line,photon,title)
        self.add(photon, trace)
        formula = MathTex(r"\alpha = \frac{4GM}{c^2 b}")
        formula .move_to(5*DOWN)
        box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)  # buff=padding
        self.play(MoveAlongPath(photon, straight),run_time=2, rate_func=linear)
        self.play(MoveAlongPath(photon, photon_path), run_time=3, rate_func=linear)
        self.play(Write(formula))
        self.play(Create(box))
        self.wait()
