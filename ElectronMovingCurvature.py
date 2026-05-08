%%manim -v WARNING -r 1080,1920 -pqh ElectronMovingCurvatureTitle
import numpy as np

class ElectronMovingCurvatureTitle(ThreeDScene):
    def construct(self):

        # camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)

        # electron tracker (x-position)
        t = ValueTracker(-3.5)

        # surface function (dynamic, bend follows electron)
        def surface_func(u, v):
            x_e = t.get_value()
            y_e = 0
            r = np.sqrt((u - x_e)**2 + (v - y_e)**2)
            z = -1.2 * np.exp(-0.8 * r)
            return np.array([u, v, z])

        # surface always redraw
        surface = always_redraw(lambda: Surface(
            surface_func,
            u_range=[-4, 4],
            v_range=[-4, 4],
            resolution=(35, 35)
        ).set_fill(BLUE_E, opacity=0.7)
         .set_stroke(width=0.3, opacity=0.15))

        # electron always redraw
        electron = always_redraw(lambda: Sphere(radius=0.25)
                                 .set_fill(YELLOW, opacity=1)
                                 .set_stroke(YELLOW, width=0.5)
                                 .move_to([t.get_value(), 0, surface_func(t.get_value(), 0)[2] + 0.1]))

        self.add(surface, electron)

        # 🎯 Fixed title (camera independent)
        title = Text("Electron Motion", font_size=48, color=WHITE)
        self.add_fixed_in_frame_mobjects(title)  # fixed in screen coordinates
        title.to_edge(UP)  # top of the screen

        # animate electron left → right → back
        self.play(t.animate.set_value(3.5), run_time=6, rate_func=there_and_back)

        # camera rotation
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
