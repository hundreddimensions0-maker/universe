%%manim -v WARNING -r 1080,1920 -pqh amperes_law
from manim import *

class amperes_law(ThreeDScene):
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

        title = Text("Magnetic Field Lines", font_size=40, color=WHITE)
        title.move_to(UP*4)

        equation = MathTex(r"B = \frac{\mu_0 I}{2\pi r}", font_size=40)
        box = SurroundingRectangle(equation, color=YELLOW, buff=0.3)
        eq_group = VGroup(equation, box)
        eq_group.move_to(DOWN*5)


        self.add_fixed_in_frame_mobjects(title, eq_group)
        self.add(title, eq_group)

        # Wire
        wire = Cylinder(radius=0.3, height=5, resolution=(32, 32))
        wire.set_fill(GREY, opacity=0.8)
        wire.set_stroke(width=0)
        self.add(wire)

        # Electrons
        num_electrons = 8
        electrons = VGroup()
        for i in range(num_electrons):
            dot = Dot3D(color=YELLOW, radius=0.08)
            electrons.add(dot)
        self.add(electrons)

        def update_electrons(mob):
            for i, dot in enumerate(mob):
                phase = (t.get_value() + i / num_electrons) % 1.0
                z_pos = -2.5 + phase * 5.0
                angle = i * (TAU / num_electrons)
                x_pos = 0.15 * np.cos(angle)
                y_pos = 0.15 * np.sin(angle)
                dot.move_to([x_pos, y_pos, z_pos])

        electrons.add_updater(update_electrons)
        self.add(electrons)

        #  Fixed radii wali rings jo sirf rotate karengi
        m_lines = always_redraw(lambda: self.get_magnetic_rings(t.get_value()))
        self.add(m_lines)

        self.play(
            t.animate.set_value(2),
            run_time=5,
            rate_func=linear
        )
        self.wait()

    def get_magnetic_rings(self, offset):
        rings = VGroup()

        # Fixed radii — expand nahi hongi, sirf rotate hongi
        radii = [0.8, 1.4, 2.0, 2.6, 3.2]

        for r in radii:
            # Opacity door jaane par kam hogi
            opacity = clip(1 - (r / 4.0), 0.1, 1)

            #  Arc banao — puri ring nahi, taake rotation visible ho
            arc = Arc(
                radius=r,
                start_angle=offset * TAU,       #  Rotation: angular movement
                angle=TAU * 0.92,               # Almost full circle, gap se direction pata chale
                color=BLUE,
                stroke_width=3,
                stroke_opacity=opacity
            )

            #  Arrow tip add karo — angular direction dikhane ke liye
            tip_angle = offset * TAU + TAU * 0.92
            tip_pos = np.array([r * np.cos(tip_angle), r * np.sin(tip_angle), 0])
            tang = np.array([-np.sin(tip_angle), np.cos(tip_angle), 0])  # Tangent direction
            arrow = Arrow(
                start=tip_pos - tang * 0.01,
                end=tip_pos + tang * 0.3,
                color=BLUE,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.8,
                stroke_opacity=opacity,
                fill_opacity=opacity
            )

            rings.add(arc, arrow)

        return rings
