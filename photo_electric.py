%%manim -v WARNING -r 1080,1920 -pqh photo_electric
from manim import*
class photo_electric(Scene):
  def construct(self):
    title=Text("Photoelectric Effect")
    title.scale(1)
    title.move_to(UP*6)
    formula = MathTex(
            r"K_{\text{max}} = h \frac{c}{\lambda} - \phi",font_size=42
        )
    formula.move_to(6*DOWN)
    box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)  # buff=padding
    self.add(title,formula,box)

    metal=Line(LEFT*3,RIGHT*3,stroke_width=5,color=WHITE)
    self.add(metal)
    core = Ellipse(width=0.2, height=0.1)
    core.set_fill("#FFF7B0", opacity=1)
    core.set_stroke(width=0)
    # smooth gradient layers
    glow = VGroup()
    n = 25  # more layers = more smooth merge
    for i in range(n):
        w =0.2 + i * 0.016     # width grow karegi
        h = 0.1 + i * 0.011   # height grow karegi
        opacity = 0.25 * (1 - i/n)  # fade outward
        c = Ellipse(width=w, height=h)
        c.set_fill("#FF8C00", opacity=opacity)
        c.set_stroke(width=0)
        glow.add(c)
    g=VGroup(glow, core)
    g.rotate(PI/4)
    refrence_line=Line(LEFT*4,RIGHT*3,color=WHITE)
    refrence_line.rotate(-PI/4)
    refrence_line1=Line(LEFT*0,UR*3,color=WHITE)

    triangle = Polygon(
            [-1,-0,0],
            refrence_line.get_start(),
            [1,0,0],stroke_width=0
        )                                                                 # refrence_line.get_start()
    triangle.set_fill(color=YELLOW,opacity=0.2)
    self.play(Create(triangle),run_time=3,rate_func=linear)
    self.add(g)
    straight = Line(LEFT*4, LEFT*0)
    trace = TracedPath(g.get_center, stroke_width=4)
    self.add(g)
    self.play(MoveAlongPath(g, refrence_line1),run_time=2, rate_func=linear)
    self.wait(2)
