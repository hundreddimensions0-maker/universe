%%manim -v WARNING -r 1080,1920 -pqh kcl
from manim import*
class kcl(Scene):
  def construct(self):
    title=Text(" Kirchhoff's Current Law")
    title.scale(1)
    title.move_to(UP*6)
    formula = MathTex(
            r"\sum I_{in} = \sum I_{out}",font_size=42
        )
    formula.move_to(6*DOWN)
    box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)
    self.add(box,formula,title)
    circle=Circle(radius=5)
    line=Line(start=[-5,0,0],end=[0,0,0])
    line1=Line(start=[0,0,0],end=[3.5355,3.5355,0])
    line2=Line(start=[0,0,0],end=[3.5355,-3.5355,0])
    dot=Dot(point=[0,0,0],color=YELLOW)
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
    g.move_to(line.get_start())
    self.add(line,line1,dot,line2,g)
    trace = TracedPath(g.get_center, stroke_width=4)
    electron_path = TracedPath(dot.get_center, stroke_width=4)
    G=g.copy()
    G.move_to(line2.get_start())
    G1=g.copy()
    G1.move_to(line2.get_start()) 
    self.play(MoveAlongPath(g, line),run_time=2, rate_func=linear)
    self.remove(g)
    self.play(MoveAlongPath(G, line1),MoveAlongPath(G1, line2),run_time=4, rate_func=linear)


