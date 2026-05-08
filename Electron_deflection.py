from manim import*
class Electron_deflection(Scene):
  def construct(self):
    title=Text("Electron deflection")
    title.scale(1)
    title.move_to(UP*5)
    positive_plate=Rectangle(width=6,height=0.5,color=BLUE)
    positive_plate.move_to(UP*3)
    positive_plate.set_fill(BLUE, opacity=0.2) # Corrected line
    negative_plate=Rectangle(width=6,height=0.5,color=BLUE)
    negative_plate.move_to(DOWN*3)
    negative_plate.set_fill(BLUE, opacity=0.2) # Corrected line
    num=6
    for k in range(num):
      minus_sing=MathTex(r"\boldsymbol{-}",color=RED)
      minus_sing.move_to(positive_plate.get_center()+(k - (num-1)/2)*LEFT)
      plus_sing=MathTex(r"\boldsymbol{+}",color=RED)
      plus_sing.move_to(negative_plate.get_center()+(k - (num-1)/2)*LEFT)
      plus_sing.scale(0.8)
      self.add(plus_sing,minus_sing)
    foil=Line(LEFT*3,RIGHT*3)
    foil.rotate(PI/2)
    foil.move_to(RIGHT*3.5)
    t=ValueTracker(3)
    straight = Line(LEFT*5, LEFT*3)
    base_line=DashedLine(LEFT*3,RIGHT*3)
    electron = Dot(color=YELLOW).move_to(straight.get_start())
    electron_path=ParametricFunction(lambda m : np.array([m,0.04*-(m+3)**2,0]),t_range=(-3,3.5))
    self.add(base_line,electron,positive_plate, negative_plate,foil,title)
    trace = TracedPath(electron.get_center, stroke_width=4)
    self.add(electron, trace)
    # motion
    self.play(MoveAlongPath(electron, straight),run_time=2, rate_func=linear)
    self.play(MoveAlongPath(electron, electron_path), run_time=3, rate_func=linear)
    formula = MathTex(r"y = \frac{2 m v_0^2}{e E} x^2")
    formula.move_to(5*DOWN)
    box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)  # buff=padding

    self.play(Write(formula))
    self.play(Create(box))
    self.wait(2)
