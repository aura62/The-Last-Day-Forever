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

    show kieran nsmile at center_zoomed with fundido_suave
    show kieran surprised at left_small with moveinleft
    "¿Este chico ha aparecido de repente?"
    k "Hola, [player_name]"
    k "¡Soy Kieran!"
    k "Al fin nos conocemos en persona."

    p "¿[player_name]?"
    k "Sí..ese es tu nombre ¿no?"

    menu confNombre:
            "De hecho..."
            "Sí":
                p "Perdona. Es que me tomo por sorpresa-"
                p "Olvida lo que dije Kieran."
            "No":
                p "De hecho solo es un apodo."
                k "¡Oh! Eso es una sopresa... no recuerdo que me lo hayas dicho pero esta bien."
                k "¿Como deberia de llamarte?"
                $ player_name = renpy.input("Mi nombre es")

    $ player_name = player_name.strip().capitalize()
    if player_name =="":
        $ player_name = "Alex"
    show kieran shy
    k "¡[player_name]! Es bueno verte al fin en persona."
    show kieran nsmile
    k "Por un momento pense que no podria reconocerte.."
    p "O-oh... yo también lo pense. Despues de todo es diferente cuando las personas se ven cara a cara."
    "Honestamente no recuerdo tener un conocido llamado Kieran...¿por que estoy respondiendo como si lo conozco?"
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

label ch_parque:
    show kieran blush
    k "¡Me parece buena idea! de paso podria invitarte a algo."
    jump parque

label ch_cafeteria:
    show kieran blush
    k "Conozco el lugar ideal. ¡Vamos! Quisiera invitarte a comer."
    jump cafeteria

label conversacion:
    
    show kieran nsmile
    k "Pues tienes razón, si que ha servido para matar el tiempo."
    p "¿Kieran?"
    show kieran shy
    k "Dime.."
    p "¿Tu me habias dicho tu nombre antes?"
    k "...."
    show kieran sad with fade_texto
    k "No, en realidad no."
    show kieran pout with fade_texto
    k "Pero no deberias de preocuparte."
    show kieran nsmile
    k "Despues de todo este es tu sueño, es normal que sepas mi nombre."
    p "...Entiendo. Honestamente lo pense por un momento."
    p "Demasiado real para estar conviviendo con alguien medianamente agradable."
    show kieran surprised
    k "...."
    show kieran shy
    k "A mi tambien me agrado pasar el rato contigo."
    k "...."
    show kieran sad with fade_texto
    k "Pero estas por despertar.."
    k "No tengo idea si es la ultima vez que nos veremos pero"
    show kieran blush with fade_texto
    k "Gracias por hablar conmigo."
    p "...."
    pause 0.5
    p "No, gracias a ti. Hacia dias que no tenia un buen descanso."
    p "Tengo fe que nos volveremos a ver así que no dire adios.."
    p "¡Hasta pronto Kieran!"
    show kieran surprised with fade_texto
    pause 1.0
    show kieran shy with fade_texto
    k "Hasta pronto, [player_name]"

    # Finaliza el juego:

    return
