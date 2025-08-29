label parque:
    show kieran nsmile
    k "Siguemeeeeee"
    hide kieran nsmile with moveoutright
    p "¡Kieran esperame!"
    
    scene bg park with fade_texto
    pause 1.0
    stop music fadeout 1.0
    pause 0.5
    play music ("audio/BGM/Pawel_Feszczuk_How_Its_Done.mp3",) fadein 0.5
    p "Ni si quiera pude ver hacia donde se fue.."
    "Voy a quedarme aquí un momento y lo esperare."
    "Dijo que me invitaria a comer algo asi que seguro no tarda en venir."
    "......"
    "No me gusta estar en silencio."
    "Tampoco recuerdo haber preguntado su nombre..."
    "¿Como pude pronunciarlo sin saberlo?"
    "...."

    show kieran nsmile at center_zoomed with vpunch
    k "¡[player_name] ya estoy de vuelta!"
    p "!!!!"
    p "{redalert}NO HAGAS ESO DE NUEVO-{redalert}"
    show kieran surprised with fade_texto
    pause 1.0
    k "Perdona no era mi intención.... solo intente darme prisa para regresar."
    k "No queria preocuparte.."
    p "...."
    p "Vale solo no lo hagas de nuevo. Me dio un buen {textshadow}susto.{textshadow}"
    show kieran shy
    k "Lo tendre en cuenta para la proxima."
    k "Nuestra orden tardara unos minutos..."
    show kieran blush
    k "¿Te parece bien si me siento a tu lado a esperar?"
    p "Claro, que hay sitio de sobra en la banca."
    p "¿Quieres jugar a veo veo para matar el tiempo?"
    show kieran nsmile
    k "¡Claro!"
    call preguntas
    jump conversacion

label cafeteria:
    show kieran nsmile
    k "Siguemeeeeee"
    hide kieran nsmile with moveoutright
    p "¡Kieran esperame!"

    scene bg cafeteria with fade_texto
    stop music fadeout 1.0
    pause 0.5
    play music ("audio/BGM/Paweł Feszczuk - How it's done.mp3",) fadein 0.5
    show kieran nsmile at center_zoomed with fade_texto
    k "¡Hemos llegado!"
    p "A penas y pude seguirte el paso..."
    show kieran shy
    k "Disculpa, me emocione tanto que olvide bajar el ritmo."
    p "Bueno..¡no pasa nada!"
    p "Este lugar se ve agradable."
    show kieran blush
    k "¡Desde luego! es uno de mis lugares favoritos."
    k "¡Ahora ire a traer el menú!"
    hide kieran nsmile with moveoutleft
    pause 3.0
    p "...." 
    show kieran nsmile at center_zoomed with moveinleft
    pause 1.0
    k "Aqui tienes."
    k "Cuando termines de mirar el menu, dime que quieres pedir."
    hide kieran shy with moveoutright
    p "¿Que deberia elegir?"
    pause 0.5
    call screen menu_comida


screen menu_comida():
    hbox:
        spacing 19
        xalign 0.5
        yalign 0.5

        # Botón con icono de omelette
        imagebutton:
            idle "images/icn/ome.png"    # imagen normal
            hover "images/icn/ome_hover.png"  # imagen al pasar el ratón
            action Jump("ome_opc")

        # Botón con icono de pancakes
        imagebutton:
            idle "images/icn/pan.png"
            hover "images/icn/pan_hover.png"
            action Jump("pan_opc")

        # Botón con icono de sandwich
        imagebutton:
            idle "images/icn/sand.png"
            hover "images/icn/sand_hover.png"
            action Jump("sand_opc")

label ome_opc:
    pause 0.5
    show kieran shy at right_small with moveinright 
    k "Teniendo en cuenta la hora que es, entiendo por que has elegido el omelette."
    jump conversacion

label pan_opc:
    pause 0.5
    show kieran surprised at right_small with moveinright
    k "¡Algo que tenemos en común!"
    show kieran blush
    k "Me gustan las tortitas, especialmente si estan hechas de avena."
    jump conversacion

label sand_opc:
    pause 0.5
    show kieran nsmile at right_small with moveinright
    k "¡Buena elección!"
    k "Siempre viene bien comer algo ligero antes del plato principal."
    jump conversacion



