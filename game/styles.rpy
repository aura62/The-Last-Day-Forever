init python:
    # 🔤 Estilo personalizado para texto entre escenas
    style.carta_nvl_text = Style(style.nvl_text)
    style.carta_nvl_text.size = 30  # Tamaño de fuente
    style.carta_nvl_text.line_spacing = 2  # Espacio entre líneas dentro del bloque
    style.carta_nvl_text.color = "#e8e8e8"  # Color suave para papel
    #style.carta_nvl_text.font = "fonts/DancingScript-Regular.ttf" 

    # 📏 Reduce espacio entre bloques nvl consecutivos
    style.nvl_vbox.box_spacing = 2  # Por defecto suele estar entre 15–20

    # (Opcional) Aplicar un fondo de carta solo al NVL
    # style.nvl_window.background = Frame("gui/carta_fondo.png", 50, 50)