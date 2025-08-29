screen imagemap_route1():
    imagemap:
        idle "images/bg/park_objects.png"
        hover "images/bg/park_objects_hover.png"

        hotspot (440, 590, 89, 102) action Jump("lirios") alt "Lirios"
        hotspot (827, 677, 89, 155) action Jump("arrendajo") alt "Arrendajo"
        hotspot (1415, 628, 96, 108) action Jump("paloma") alt "Paloma"
        hotspot (1736, 581, 83, 88) action Jump("rosa") alt "Rosa"

label preguntas:
    label pr1:
    $ rsp = 1

    show kieran nsmile
    k "¡Veo, veo!"
    p "¿Qué ves?"
    k "Una cosita..."
    p "¿Qué cosita es?"
    k "Blanco con petalos en forma de campana."
    "¿Que podria ser?"
    call imagemap_example

    label pr2:
    $ rsp = 2

    show kieran nsmile
    k "¡Veo, veo!"
    p "¿Qué ves?"
    k "Una cosita..."
    p "¿Qué cosita es?"
    k "Un animal con cresta en la cien, vuela y probablemente tiene un amigo mapache.."
    "¿Que podra ser?"
    call imagemap_example

    label pr3:
    $ rsp = 3

    show kieran nsmile
    k "¡Veo, veo!"
    p "¿Qué ves?"
    k "Una cosita..."
    p "¿Qué cosita es?"
    k "Tiene el pecho blanco, capaz de encontrar su camino de vuelta a casa con un vuelo de paz."
    "¿Que podra ser?"
    call imagemap_example

    label pr4:
    $ rsp = 4

    show kieran nsmile
    k "¡Veo, veo!"
    p "¿Qué ves?"
    k "Una cosita..."
    p "¿Qué cosita es?"
    k "Un secreto teñido de flor, imposible de hallar en un jardin."
    "¿Que podra ser?"
    call imagemap_example

    return

label imagemap_example:

    call screen imagemap_route1
    return

label lirios:
    $ opc = 1
    p "¿Te refieres a los lirios del valle?"
    jump imagemap_done

label arrendajo:
    $ opc = 2
    p "¿Te refieres al arrendajo que está encima de la maceta?"
    jump imagemap_done

label paloma:
    $ opc = 3
    p "¿Te refieres a la paloma que esta en la fuente?"
    jump imagemap_done

label rosa:
    $ opc = 4
    p "¿Hablas sobre esa rosa azul?"
    jump imagemap_done

init python:
    respuestas = {
        1: ["¡Sí!", "Los lirios del valle son realmente bonitos, aunque son considerados una plaga en muchos sitios."],
        2: ["¡Lo has clavado!", "Quiero pensar que lo deje facil."],
        3: ["Tal vez no sean las aves mas amadas.", "Pero admiro su capacidad de adaptación."],
        4: ["Correcto. En realidad me pregunto cómo llegó esa rosa allí..", "Naturalmente no hay pigmento azul en estas...", "De forma natural claro."]
    }

label imagemap_done:
    python:
        if opc == rsp:
            for linea in respuestas[rsp]:
                renpy.show("kieran blush")
                renpy.say(k, linea)
        else:
            renpy.show("kieran surprised")
            renpy.say(k, "Eh.... no, no me refiero a eso.")
            renpy.show("kieran nsmile")
            renpy.say(k, "¡Pero sigamos!")
 