%%manim -v WARNING -r 1080,1920 -pqh BlackBodyRayLoop
from manim import *
import numpy as np
class BlackBodyRayLoop(Scene):
    def construct(self):
        config.background_color = BLACK
        # ------------------------
        # Cavity walls
        # ------------------------
        title=Text("Blackbody Radiation")
        title.move_to(UP*5)
        equation = MathTex(
            r"B(\nu,T) = \frac{2h\nu^3}{c^2} \cdot \frac{1}{e^{h\nu/kT}-1}",
            font_size=42
         )
        equation.move_to(DOWN*5)
        box = SurroundingRectangle(equation, color=YELLOW, buff=0.3)
        eq_group = VGroup(equation, box)
        self.add(title,eq_group)
        circle_1 = ParametricFunction(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[PI/9, 2*PI],
            color=WHITE
        )
        circle_2 = ParametricFunction(
            lambda t: np.array([1.2*np.cos(t), 1.2*np.sin(t), 0]),
            t_range=[PI/9, 2*PI],
            color=WHITE
        )
        points1 = [circle_1.point_from_proportion(i) for i in np.linspace(0, 1, 100)]
        points2 = [circle_2.point_from_proportion(i) for i in np.linspace(0, 1, 100)]
        cavity_area = Polygon(*points1, *reversed(points2), color=GREY, fill_opacity=0.4)
        self.add(circle_1, circle_2, cavity_area)
        # ------------------------
        # Ray using loop
        # ------------------------
        intial_ray=Line(start=[5*np.cos(PI/30), np.sin(5*PI/30), 0],end=[np.cos(PI/30), np.sin(PI/30), 0],color=RED)
        intial_ray.set_stroke(width=2)
        ray_path = VMobject(color=RED)
        ray_points = []
        # Angles in radians (like your original points)
        n = 10  # number of angle steps
        angles = np.linspace(PI/30, PI, n)
        for angle in angles:
            # Ray goes in positive direction
            ray_points.append([np.cos(angle), np.sin(angle), 0])
            # Ray goes in negative direction (reflect)
            ray_points.append([-np.cos(angle), -np.sin(angle), 0])
        ray_path.set_points_as_corners(ray_points)
        ray_path.set_stroke(width=2)
        # Animate ray
        self.play(Create(intial_ray))
        self.play(Create(ray_path), run_time=3)
        self.wait()
