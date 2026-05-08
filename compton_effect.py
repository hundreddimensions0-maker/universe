%%manim -v WARNING -r 1080,1920 -pqh compton_effect
from manim import*
class compton_effect(Scene):
  def construct(self):
    title=Text("Compton Effect")
    title.scale(1)
    title.move_to(UP*6)
    formula = MathTex(
            r"\Delta \lambda = \lambda' - \lambda = \frac{h}{m_e c} (1 - \cos\theta)",font_size=42
        )
    formula.move_to(6*DOWN)
    box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)  # buff=padding
    electron=Dot(color=YELLOW)
    self.add(electron,box,formula,title)
    base_line=DashedLine(LEFT*6,RIGHT*6)
    self.add(base_line.set_stroke(width=0.3))
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
    g.move_to(LEFT*4)
    self.add(g)
    straight = Line(LEFT*4, LEFT*0)
    trace = TracedPath(g.get_center, stroke_width=4)
    self.add(g)

    self.play(MoveAlongPath(g, straight),run_time=2, rate_func=linear)
    deflect_straight = Line(LEFT*0, UR*4).set_fill(opacity=0.3)

    trace = TracedPath(g.get_center, stroke_width=1)

    electron_path = TracedPath(electron.get_center, stroke_width=4)
    electron_path = Line(LEFT*0, DR*4).set_fill(opacity=0.3)
    trace_E = TracedPath(electron.get_center, stroke_width=1)
    self.add(g.set_fill(BLUE, opacity=opacity*5),trace,trace_E)
    angle = Angle(base_line, deflect_straight, radius=0.5, other_angle=False)
    angle_e=MathTex(
            r"\theta")
    angle_e.next_to(angle,RIGHT)
    self.play(
    MoveAlongPath(g, deflect_straight),
    MoveAlongPath(electron, electron_path),Create(angle),Write(angle_e),
    run_time=3,
    rate_func=linear
      )
    self.wait(1)
