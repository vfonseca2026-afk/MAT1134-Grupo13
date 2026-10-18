from manim import *


class VideoExplicativoGrupo13(Scene):

  def construct(self):
    # ==========================================
    # BLOQUE 0: PORTADA / IDENTIFICACIÓN (Grupo 13)
    # ==========================================
    curso = Text(
        "Universidad Católica de Temuco — MAT1134", font_size=18, color=GRAY
    )
    curso.to_edge(UP, buff=0.3)

    main_title = Text(
        "Proyecto Grupal: El Infinito en la Definición de Integral",
        font_size=24,
        color=YELLOW,
    )
    main_title.next_to(curso, DOWN, buff=0.15)

    integrantes = Text(
        "Integrantes: Carlos Meléndez | Danna Ramirez | Vicente Fonseca",
        font_size=16,
        color=BLUE_A,
    )
    integrantes.next_to(main_title, DOWN, buff=0.15)

    self.play(
        Write(curso),
        Write(main_title),
        FadeIn(integrantes, shift=DOWN),
        run_time=2,
    )
    self.wait(5)

    self.play(
        FadeOut(curso),
        FadeOut(integrantes),
        Transform(
            main_title,
            Text(
                "Grupo 13: El infinito en la definición de integral", font_size=26
            ).to_edge(UP, buff=0.2),
        ),
        run_time=1.5,
    )
    title = main_title

    # ==========================================
    # BLOQUE 1: GANCHO PRÁCTICO — El problema del vehículo (Velocidad Variable)
    # ==========================================
    sub_pregunta = Text(
        "Un vehículo viaja a velocidad variable v(t).\n"
        "¿Cómo calculamos la distancia exacta recorrida?",
        font_size=18,
        color=GRAY,
    )
    sub_pregunta.next_to(title, DOWN, buff=0.15)
    self.play(FadeIn(sub_pregunta, shift=DOWN), run_time=1.5)

    # Ejes de velocidad vs tiempo
    axes_v = Axes(
        x_range=[0, 6, 1],
        y_range=[0, 6, 1],
        x_length=5.0,
        y_length=2.5,
        axis_config={"include_numbers": False},
    )
    axes_v.to_edge(DOWN, buff=0.8)

    label_vt = MathTex("v(t)").scale(0.6).next_to(axes_v.y_axis, UP, buff=0.1)
    label_t = MathTex("t").scale(0.6).next_to(axes_v.x_axis, RIGHT, buff=0.1)

    # Curva de velocidad oscilatoria (senoidal desplazada)
    v_func = axes_v.plot(
        lambda t: 3 + 1.2 * np.sin(1.8 * t), x_range=[0, 5], color=TEAL
    )
    v_label = (
        MathTex("v(t) = 3 + 1.2\\sin(1.8t)")
        .scale(0.45)
        .next_to(v_func, UP, buff=0.1)
        .set_color(TEAL)
    )

    self.play(
        Create(axes_v),
        Write(label_vt),
        Write(label_t),
        Create(v_func),
        Write(v_label),
        run_time=2,
    )
    self.wait(15)

    # Destacar que la distancia es el área bajo v(t)
    area_v = axes_v.get_area(v_func, x_range=[0, 5], color=TEAL, opacity=0.3)
    dist_text = Text(
        "Distancia = Área bajo la curva de velocidad",
        font_size=16,
        color=TEAL_B,
    ).to_corner(UL).shift(DOWN * 1.0)

    self.play(FadeIn(area_v), Write(dist_text), run_time=1.5)
    self.wait(15)

    # Limpieza para pasar al modelo formal de trabajo
    self.play(
        FadeOut(sub_pregunta),
        FadeOut(axes_v),
        FadeOut(label_vt),
        FadeOut(label_t),
        FadeOut(v_func),
        FadeOut(v_label),
        FadeOut(area_v),
        FadeOut(dist_text),
        run_time=1.5,
    )

    # Modelo matemático del proyecto
    sub_teoria1 = Text(
        "Modelo de estudio: f(x) = x² + 1 en el intervalo cerrado [0, 4]",
        font_size=20,
        color=YELLOW,
    )
    sub_teoria1.next_to(title, DOWN, buff=0.2)
    self.play(Write(sub_teoria1), run_time=1.5)
    self.wait(12)
    self.play(FadeOut(sub_teoria1))

    # ==========================================
    # BLOQUE 2: EJEMPLO Y VISUALIZACIÓN DE SUMAS DE RIEMANN
    # ==========================================
    axes = Axes(
        x_range=[0, 4.5, 1],
        y_range=[0, 20, 4],
        x_length=5.5,
        y_length=2.8,
        axis_config={"include_numbers": True, "font_size": 14},
    )
    axes.to_edge(DOWN, buff=0.6).to_edge(RIGHT, buff=0.5)

    func = axes.plot(lambda x: x**2 + 1, x_range=[0, 4], color=BLUE)
    func_label = (
        MathTex("y = f(x) = x^2 + 1")
        .scale(0.5)
        .next_to(func, UP, buff=0.1)
        .set_color(BLUE)
    )

    self.play(Create(axes), Create(func), Write(func_label), run_time=2)

    sub_explicacion = Text(
        "Paso 1: Pocos rectángulos\nn = 4, Δx = 1.0\nGran error de aproximación",
        font_size=18,
    )
    sub_explicacion.to_corner(UL).shift(DOWN * 0.8)
    self.play(Write(sub_explicacion), run_time=1)

    n1 = 4
    dx1 = 4 / n1
    rects1 = axes.get_riemann_rectangles(
        func, x_range=[0, 4], dx=dx1, color=YELLOW, fill_opacity=0.4
    )
    self.play(Create(rects1), run_time=1.5)
    self.wait(20)

    sub_explicacion2 = Text(
        (
            "Paso 2: Aumentamos subintervalos\nn = 12, Δx ≈ 0.33\nLa región se"
            " ajusta mejor"
        ),
        font_size=18,
    )
    sub_explicacion2.to_corner(UL).shift(DOWN * 0.8)

    n2 = 12
    dx2 = 4 / n2
    rects2 = axes.get_riemann_rectangles(
        func, x_range=[0, 4], dx=dx2, color=YELLOW, fill_opacity=0.4
    )
    self.play(
        Transform(rects1, rects2),
        Transform(sub_explicacion, sub_explicacion2),
        run_time=2,
    )
    self.wait(20)

    # ==========================================
    # BLOQUE 3: RELACIÓN ALGEBRAICA DE Δx
    # ==========================================
    sub_algebra = Text(
        (
            "Relación Algebraica:\nΔx = (b - a) / n = (4 - 0) / n = 4 / n\nAl"
            " crecer n, el denominador aumenta y Δx decrece."
        ),
        font_size=17,
        color=BLUE_C,
    )
    sub_algebra.to_corner(UL).shift(DOWN * 0.8)

    algebra_box = MathTex(
        "\\Delta x = \\frac{4}{n} \\implies \\text{Inversamente proporcionales}"
    ).scale(0.5)
    algebra_box.to_corner(UL).shift(DOWN * 2.0)

    self.play(
        Transform(sub_explicacion, sub_algebra),
        Write(algebra_box),
        run_time=2,
    )
    self.wait(25)

    self.play(FadeOut(algebra_box), run_time=1)

    # ==========================================
    # BLOQUE 4: PROCESO AL INFINITO Y PARADOJA N ≠ ∞
    # ==========================================
    sub_explicacion3 = Text(
        (
            "Paso 3: Proceso al límite\nn → ∞ implica Δx → 0\nEl ancho se vuelve"
            " infinitesimal"
        ),
        font_size=18,
        color=RED,
    )
    sub_explicacion3.to_corner(UL).shift(DOWN * 0.8)

    rects_inf = axes.get_riemann_rectangles(
        func,
        x_range=[0, 4],
        dx=4 / 40,
        color=YELLOW,
        fill_opacity=0.4,
    )

    self.play(
        Transform(rects1, rects_inf),
        Transform(sub_explicacion, sub_explicacion3),
        run_time=2.5,
    )
    self.wait(20)

    sub_paradaja = Text(
        (
            "¿Por qué n ≠ ∞?\nSi n fuera 'infinito', Δx sería 0 exacto:\n"
            "¡Tendríamos una suma de infinitos rectángulos de ancho cero!"
        ),
        font_size=17,
        color=ORANGE,
    )
    sub_paradaja.to_corner(UL).shift(DOWN * 0.8)

    warning_box = Rectangle(
        width=4.5, height=1.2, color=ORANGE, stroke_width=2
    )
    warning_box.to_corner(UL).shift(DOWN * 1.8)
    warning_text = Text(
        "El infinito es una tendencia,\nno un número sustituible.",
        font_size=15,
        color=ORANGE,
    ).move_to(warning_box.get_center())

    self.play(
        Transform(sub_explicacion, sub_paradaja),
        Create(warning_box),
        Write(warning_text),
        run_time=2,
    )
    self.wait(30)

    self.play(
        FadeOut(sub_explicacion),
        FadeOut(warning_box),
        FadeOut(warning_text),
        FadeOut(axes),
        FadeOut(func),
        FadeOut(func_label),
        FadeOut(rects1),
        run_time=1.5,
    )

    # ==========================================
    # BLOQUE 5: CIERRE Y FORMULACIÓN
    # ==========================================
    limit_eq = MathTex(
        "\\int_{0}^{4} (x^2 + 1)\\,dx = \\lim_{n \\to \\infty} \\sum_{i=1}^{n}"
        " f(x_i^*)\\,\\Delta x"
    ).scale(0.8)
    limit_eq.to_edge(UP, buff=1.0)

    sub_cierre = Text(
        "Conclusión: La integral definida transforma una suma infinita\n"
        "de áreas infinitesimales en un valor exacto de acumulación.",
        font_size=20,
    )
    sub_cierre.next_to(limit_eq, DOWN, buff=0.8)

    self.play(Write(limit_eq), Write(sub_cierre), run_time=2)
    self.wait(30)

    self.play(FadeOut(limit_eq), FadeOut(sub_cierre), FadeOut(title), run_time=1)