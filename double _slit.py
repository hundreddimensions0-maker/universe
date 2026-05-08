%%manim -v WARNING -r 1080,1920 -pqh double _slit


from manim import *
import numpy as np

class double _slit(Scene):
    def construct(self):
        # 1. Configuration
        wave_color = BLUE_B
        wave_stroke = 3
        spacing = 0.8
        max_dist = 6.0

        title = Text("Double Slit Interference Pattern", font_size=32).move_to(UP*8)

        # Wall and Screen
        wall = Line(UP*4, DOWN*4, color=WHITE, stroke_width=8).move_to(LEFT*1.5)
        screen = Line(UP*3.5, DOWN*3.5, color=DARK_GRAY, stroke_width=6).move_to(RIGHT*5.5)
        screen_label = Text("Screen", font_size=20).next_to(screen, UP)

        # Slit positions
        s1_pos = LEFT*1.5 + UP*0.7
        s2_pos = LEFT*1.5 + DOWN*0.7

        t = ValueTracker(0)

        # 2. LINEAR WAVES (Incoming Light)
        linear_waves = VGroup()
        for i in range(8):
            initial_offset = i * spacing
            l_wave = always_redraw(lambda o=initial_offset: Line(
                UP*2.5, DOWN*2.5,
                stroke_width=wave_stroke,
                color=wave_color,
                stroke_opacity=0.5
            ).move_to(LEFT*5 + RIGHT * ((o + t.get_value()) % 3.5)))
            linear_waves.add(l_wave)

        # 3. SEMI-CIRCULAR WAVES (Diffracted)
        def create_synced_waves(source_pos):
            waves = VGroup()
            for i in range(12):
                initial_offset = i * spacing
                wave = always_redraw(lambda o=initial_offset: Arc(
                    radius=((o + t.get_value()) % max_dist),
                    start_angle=-PI/2,
                    angle=PI,
                    arc_center=source_pos,
                    stroke_width=wave_stroke,
                    color=wave_color,
                    stroke_opacity=max(0, 0.8 - (((o + t.get_value()) % max_dist) / max_dist))
                ))
                waves.add(wave)
            return waves

        waves_top = create_synced_waves(s1_pos)
        waves_bottom = create_synced_waves(s2_pos)

        # 4. INTERFERENCE PATTERN & CURVE (SWAPPED)
        def intensity_func(y):
            d = 0.7
            wavelength = spacing
            interference = np.cos(PI * d * y / (wavelength * 0.5))**2
            envelope = np.exp(-0.15 * (y**2))
            return interference * envelope

        # Fringes ab Screen ke Left par hain (Waves aur Screen ke darmiyan)
        fringes = VGroup()
        for y in np.arange(-3.5, 3.5, 0.015):
            opacity = intensity_func(y)
            # Lines 4.8 se start ho kar screen (5.47) tak ja rahi hain
            line = Line(RIGHT*4.8 + UP*y, RIGHT*5.47 + UP*y,
                        color=YELLOW,
                        stroke_width=2,
                        stroke_opacity=opacity)
            fringes.add(line)

        # Intensity Curve ab Screen ke Right par hai (Bahar ki taraf)
        intensity_curve = ParametricFunction(
            # X coordinate ab 5.53 se right ki taraf grow karega
            lambda y: np.array([5.53 + intensity_func(y) * 1.2, y, 0]),
            t_range=[-3.5, 3.5],
            color=YELLOW,
            stroke_width=2
        )

        # 5. Slit Gaps (Visual holes)
        gap_s1 = Line(s1_pos + UP*0.15, s1_pos + DOWN*0.15, color=BLACK, stroke_width=10)
        gap_s2 = Line(s2_pos + UP*0.15, s2_pos + DOWN*0.15, color=BLACK, stroke_width=10)

        # Rendering
        self.add(title, wall, screen, screen_label, linear_waves,
                 waves_top, waves_bottom, gap_s1, gap_s2,
                 fringes, intensity_curve) # Order can be anything here
        equation = MathTex(
            "I(y) = I_0 ",
            "\\left[ \\text{sinc}\\left( \\frac{\pi a y}{\\lambda L} \\right) \\right]^2", # Diffraction
            "\\cos^2\\left( \\frac{\pi d y}{\\lambda L} \\right)", # Interference
            font_size=28
        ).move_to(DOWN*7)

        # Box around equation
        eq_box = SurroundingRectangle(equation, color=YELLOW, buff=0.2, stroke_width=2)

        equation_group = VGroup(eq_box, equation)
        self.add(equation_group)

        self.play(t.animate.set_value(10), run_time=10, rate_func=linear)
        self.wait()
