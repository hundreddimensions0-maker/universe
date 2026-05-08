%%manim -v WARNING -r 1080,1920 -pqh hydrogen_atom

from manim import*
import random
class hydrogen_atom(Scene):
    def construct(self):
      title=Text("Atomic Cloud Model")
      title.move_to(UP*5)
      equation = MathTex(
            r"\psi_{1s}(r) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}",
            font_size=42
        )
      equation.move_to(DOWN*5)
      box = SurroundingRectangle(equation, color=YELLOW, buff=0.3)
      eq_group = VGroup(equation, box)
      core = Circle(radius=0.2)
      core.set_fill("#FFF7B0", opacity=1)
      core.set_stroke(width=0)
      glow = VGroup()
      n = 15  # more layers = more smooth merge
      for i in range(n):
            r = 0.2 + i * 0.08
            opacity = 0.25 * (1 - i/n)  # fade outward
            c = Circle(radius=r)
            c.set_fill("#FF8C00", opacity=opacity)
            c.set_stroke(width=0)
            glow.add(c)
      r=2
      dr=0.8
      orbital=VGroup()
      orbit1=ParametricFunction(
              lambda t:np.array([r*np.cos(t),r*np.sin(t),0]),t_range=(0,2*PI))
      orbit2=ParametricFunction(
              lambda t:np.array([(r+dr)*np.cos(t),(r+dr)*np.sin(t),0]),t_range=(0,2*PI))
      orbit1.set_stroke_width(0.2)
      orbit2.set_stroke_width(0.2)
      orbital.add(orbit1, orbit2)

      a=ValueTracker(0)
      dots=VGroup()
      for i in range(1000):
        # Store the random initial angle for each dot
        initial_angle = random.uniform(0,2*PI)
        dot = always_redraw(lambda ia=initial_angle: Dot(
            np.array([
                random.uniform(r-dr,r+dr)*np.cos(ia + a.get_value()),
                random.uniform(r-dr,r+dr)*np.sin(ia + a.get_value()),
                0
            ]),
            radius=0.03,
            color=BLUE
        ))
        dots.add(dot)
      self.add(dots,title,glow, core,eq_group)

      self.play(a.animate.set_value(2*PI), run_time=9, rate_func=linear)
