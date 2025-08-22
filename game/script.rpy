# Coloca el código de tu juego en este archivo.

# El juego comienza aquí.
label start:
    $ player_name = pc_username
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg pantalla_negra with dissolve
    pause 0.5

    call intro_1
    pause 0.3
    jump intro

label intro:

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    scene bg street with fundido_suave
    #show kieran nsmile at left_small with dissolve

    # Presenta las líneas del diálogo.

    "....."
    "No recuerdo como he llegado a este sitio.."
    "Pero es familiar de alguna forma."
    #efectos de paso

    show kieran nsmile at left_small with fundido_suave
    show kieran surprised at left_small with fundido_suave
    "¿Este chico ha aparecido de repente?"
    k "Hola, [player_name] al fin nos conocemos en persona."

    p "¿[player_name]?"
    k "Sí..ese es tu nombre ¿no?"

    menu confNombre:
            "De hecho..."
            "Sí":
                p "Perdona. Es que me tomo por sorpresa- olvida la pregunta tonta."
            "No":
                p "De hecho solo es un apodo."
                k "¡Oh! Eso es una sopresa... no recuerdo que me lo hayas dicho pero esta bien."
                k "¿Como deberia de llamarte?"
                $ player_name = renpy.input("Mi nombre es")

    $ player_name = player_name.strip().capitalize()
    if player_name =="":
        $ player_name = "Sam"
    show kieran shy
    k "¡[player_name]! Es bueno verte al fin en persona."
    show kieran nsmile
    k "Por un momento pense que no podria reconocerte.."
    p "O-oh... quiero decir- Yo también lo pense. Despues de todo es diferente cuando las personas se ven cara a cara."
    "Honestamente no tengo idea de quien es este chico...¿por que estoy respondiendo como si lo conozco?"
    show kieran sad
    k "La verdad estaba algo nervioso... no pense que aceptarias mi invitación..."
    show kieran blush
    k "Pero estas aquí-"
    show kieran nsmile
    k "Perdón, no me hagas mucho caso. Ya tengo planeado los lugares que vamos a visitar."
    k "¿Donde te gustaria ir primero?"

    menu sitios:
        "Deberiamos de ir..."
        "Al pequeño parque":
            jump ch_parque
        "A una cafeteria":
            jump ch_cafeteria
        "A un arcade":
            jump ch_arcade

label ch_parque:
    show kieran blush
    k "¡Me parece buena idea! de paso podria invitarte a algo."
    jump parque

label ch_cafeteria:
    show kieran blush
    k "Conozco el lugar ideal. ¡Vamos! Quisiera invitarte a comer."
    jump cafeteria

label ch_arcade:
    show kieran nnsmile
    k "¿Conoces alguno que este cerca? por mi parte no tengo idea si hay alguno."    
    p "¡No te preocupes! De hecho si conozco un lugar que esta cerca."
    p "De paso puedo usar mi membresia para que podamos probar todos los juegos."
    jump arcade

label conversacion:
    "...."

    # Finaliza el juego:

    return
