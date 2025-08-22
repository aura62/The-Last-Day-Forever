init python:

    # 🎬 Transición: Fundido lento (drama, cambio emocional)
    fade_lento = Fade(1.5, 1.0, 1.5, color="#000")

    # 🎬 Transición: Fundido suave (para ritmo natural)
    fundido_suave = Fade(0.5, 0.2, 0.5, color="#000")

    # 🎬 Transición: Desvanecimiento blanco (shock, iluminación)
    white_flash = Fade(0.1, 0.1, 0.3, color="#fff")

    # 🎬 Transición: Desvanecimiento negro rápido (incomodidad, suspenso)
    black_flash = Fade(0.1, 0.1, 0.3, color="#000")

    # 🎬 Transición: Flashback con efecto difuso (requiere imagen PNG)
    flashback_blur = ImageDissolve("transiciones/blur.png", 1.2)

    # 🎬 Transición: Ruido visual tipo memoria fragmentada (requiere PNG o efecto gráfico)
    glitch_dissolve = ImageDissolve("transiciones/glitch_pattern.png", 1.0)

    # 🎬 Transición: Desaturación (efecto emocional gris, con ColorMatrix)
    #desaturar = ColorMatrixTransition("desaturate", 0.8)

    # 🎬 Transición: Enfoque emocional (entrada lenta, apagado suave)
    emocional = ComposeTransition(dissolve, after=fade_lento)

    # 🎬 Transición: Carta apareciendo lentamente
    fade_texto = Dissolve(2.0)

return