%%manim -v WARNING -r 1080,1920 -pqh flux

from manim import*
class flux(ThreeDScene):
  def construct(self):
     self.set_camera_orientation(phi=65*DEGREES, theta=-30*DEGREES)
     axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-4, 4, 1],
            x_length=10,
            y_length=10,
            z_length=8,
            axis_config={
                "tip_shape": None,
                "include_ticks": False,
                "include_numbers": False,
            }
        )
     axes.z_axis.set_opacity(0)
     self.add(axes)

     title = Text("Magnetic Force", font_size=40, color=WHITE)
     title.move_to(UP*4)
     equation = MathTex(r"F = B I L \sin\theta", font_size=40)
     box = SurroundingRectangle(equation, color=YELLOW, buff=0.3)
     eq_group = VGroup(equation, box)
     eq_group.move_to(DOWN*5)
     self.add_fixed_in_frame_mobjects(title, eq_group)
     self.add(title, eq_group)
     surface=Square(stroke_width=0)
     surface.set_fill(color=YELLOW,opacity=1)
     self.add(surface)
     # Prism create (dimensions: length, width, height)
     prism = Prism(dimensions=[0.3, 4, 1])
     prism.set_color(BLUE)
     prism.move_to([3,0,0])
     prism1=prism.copy()
     prism1.move_to([-3,0,0])
     prism1.set_color(RED)
     self.add(prism,prism1)
     self.play(Rotate(surface, angle=6*PI, axis=UP), run_time=6)
     self.begin_ambient_camera_rotation(rate=0.1)
     self.wait(3)
