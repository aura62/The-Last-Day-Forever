init python:
    style.carta_nvl_text = Style(style.nvl_text)
    style.carta_nvl_text.size = 30                # Tamaño de fuente
    style.carta_nvl_text.line_spacing = 12        # Espaciado entre líneas
    style.carta_nvl_text.color = "#000000"        # Color de texto (negro suave)
    style.carta_nvl_text.font = "fonts/DancingScript-Medium.ttf"
    style.carta_nvl_text.xmargin = 70             # Márgenes laterales
    style.carta_nvl_text.ymargin = 35             # Márgenes arriba/abajo

    # Espacio entre párrafos NVL
    style.nvl_vbox.box_spacing = 25  

    # Fondo de la ventana NVL
    style.nvl_window.background = Frame("gui/nvl.png", 50, 50)