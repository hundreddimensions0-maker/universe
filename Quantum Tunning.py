%%manim -v WARNING -r 1080,1920 -pqh Quantum_tunning

from manim import *
import numpy as np

class Quantum_tunning(Scene):
  def construct(self):
    title = Text("Quantum Tunneling")
    title.scale(1)
    title.move_to(UP*6)

    formula = MathTex(
        r"T = \left[ 1 + \frac{V_0^2 \sinh^2(\kappa L)}{4E(V_0 - E)} \right]^{-1}",
        font_size=42
    )
    formula.move_to(6*DOWN)
    box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)
    self.add(title, formula, box)

    barrier = Rectangle(height=6, width=0.5, stroke_width=0)
    barrier.set_fill(color=GREY, opacity=0.7)

    refrence_line = Line(LEFT*4, RIGHT*4, color=WHITE)

    # --- Particle ---
    core = Ellipse(width=0.2, height=0.1)
    core.set_fill("#FFF7B0", opacity=1)
    core.set_stroke(width=0)

    n = 25
    glow = VGroup()
    for i in range(n):
        w = 0.2 + i * 0.016
        h = 0.1 + i * 0.011
        opacity = 0.25 * (1 - i/n)
        c = Ellipse(width=w, height=h)
        c.set_fill("#FF8C00", opacity=opacity)
        c.set_stroke(width=0)
        glow.add(c)

    g = VGroup(glow, core)
    g.move_to(LEFT*3 + UP*0.5)
    self.add(barrier, g)

    # --- Barrier edges (barrier width=0.5, centered at x=0) ---
    barrier_left  = -0.25
    barrier_right =  0.25
    kappa = 5  # decay steepness — bada = zyada fade

    def update_opacity(mob):
        x = mob.get_center()[0]

        if x < barrier_left:
            # Barrier se pehle: full brightness
            alpha = 1.0

        elif x <= barrier_right:
            # Barrier ke andar: exponential decay
            t = (x - barrier_left) / (barrier_right - barrier_left)
            alpha = np.exp(-kappa * t)

        else:
            # Barrier ke baad: dim raho (tunneled particle)
            alpha = 0.25

        # Core opacity update
        core.set_fill(opacity=alpha)

        # Glow layers — har layer ki base opacity scale karo
        for i, layer in enumerate(glow):
            base = 0.25 * (1 - i/n)
            layer.set_fill(opacity=base * alpha)

    g.add_updater(update_opacity)

    self.add(g)
    self.play(MoveAlongPath(g, refrence_line), run_time=5, rate_func=smooth)
    g.remove_updater(update_opacity)
    self.wait(2)
