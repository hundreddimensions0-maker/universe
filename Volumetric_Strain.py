%%manim -v WARNING -r 1080,1920 -pqh swimming_jump_board
from manim import*
class swimming_jump_board(ThreeDScene):
   def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-30*DEGREES)
        t = ValueTracker(0)

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

        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)
        title = Text("Volumetric Strain", font_size=40, color=WHITE)
        title.move_to(UP*4)

        equation = MathTex(r"\epsilon_v = \frac{\Delta V}{V}", font_size=40)
        box = SurroundingRectangle(equation, color=YELLOW, buff=0.3)
        eq_group = VGroup(equation, box)
        eq_group.move_to(DOWN*6)

        self.add_fixed_in_frame_mobjects(title, eq_group)
        self.add(title, eq_group)
        wall = Prism(dimensions=[6, 1.5, 0.2])  # width, thickness, height
        wall.set_fill(BLUE, opacity=0.8)
        self.add(wall)
        
        #  Deformation function (diving board style)
        def deform(p):
            x, y, z = p
            # Cantilever type bending (fixed at left, free at right)
            L = 3
            F = 0.8 * np.sin(t.get_value())  # oscillating force
            z_new = z - F * (x + L)**2 / (L**2)  # bending shape
            return np.array([x, y, z_new])
        #  Dynamic update
        wall.add_updater(lambda m: m.become(
            Prism(dimensions=[6, 1.5, 0.2])
            .set_fill(BLUE, opacity=0.8)
            .apply_function(deform)
        ))
        self.add(wall)
        #  Force arrow
        arrow = Arrow3D(start=[3, 0, 2], end=[3, 0, 0], color=RED)
        self.add(arrow)
        #  Animation (force oscillation)
        self.play(t.animate.set_value(PI/2), run_time=4, rate_func=linear)
        self.wait()
        
