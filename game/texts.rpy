label intro_1:

    window hide
    stop music fadeout 1.0
    play music ("audio/BGM/malictusmusic - Dark Awakening.mp3") fadein 2.0
    $ preferences.text_cps = 15  # Restaura texto instantáneo

    
    nvl clear
    window auto

    #nvl_narrator "{burningforbigtext}Un fuego rojo grande consume estas letras.{/burningforbigtext}"
    #nvl_narrator "{burningforsmalltext}Fuego para letras más pequeñas.{/burningforsmalltext}"
    #nvl_narrator "{blueburnbig}Fuego azul grande.{/blueburnbig}"
    #nvl_narrator "{blueburnsmall}Fuego azul pequeño.{/blueburnsmall}"
    #nvl_narrator "{demo}Este es un shader de demostración.{/demo}"
    #nvl_narrator "{hollowglow}Un resplandor hueco alrededor del texto.{/hollowglow}"
    #nvl_narrator "{gradientglow}Un gradiente brillante.{/gradientglow}"
    #nvl_narrator "{glow}Un texto con un brillo simple.{/glow}"
    #nvl_narrator "{redalert}¡ALERTA ROJA!{/redalert}"
    #nvl_narrator "{prey}Un barrido rojo pasa sobre este texto.{/prey}"
    #nvl_narrator "{goldsweep}Texto con un destello dorado.{/goldsweep}"
    #nvl_narrator "{colorsweep}Un barrido de color atraviesa las letras.{/colorsweep}"
    #nvl_narrator "{textshadow}Texto con sombra.{/textshadow}"
    #nvl_narrator "{gradient}Un degradado entre colores.{/gradient}"
    #nvl_narrator "{hl}Texto resaltado simple.{/hl}"
    #nvl_narrator "{hlrc}Texto resaltado con recoloración.{/hlrc}"
    #nvl_narrator "{reversed}Este texto está al revés (invertido).{/reversed}"
    #nvl_narrator "{flipped}Texto volteado verticalmente.{/flipped}"
    #nvl_narrator "{cthonic}Texto oscuro y distorsionado.{/cthonic}"
    #nvl_narrator "{cthonicjitter}Texto con sacudidas caóticas.{/cthonicjitter}"
    #nvl_narrator "{redactedglitch}Texto glitcheado como si estuviera roto.{/redactedglitch}"
    #nvl_narrator "{cthonicglitch}Glitch oscuro estilo cthonic.{/cthonicglitch}"
    #nvl_narrator "{cthonicglitchcolor}Glitch a color.{/cthonicglitchcolor}"
    #nvl_narrator "{blackout}Texto censurado en negro.{/blackout}"
    #nvl_narrator "{purple}Texto con fuego púrpura.{/purple}"

    nvl_narrator "{=carta_nvl_text}\nAhora solo somos tu y yo en este lugar ¿eh?...No necesitas responder por ahora."
    nvl_narrator "{=carta_nvl_text}\nSé que no te gusta el silencio...ya que significa quedarte a solas conmigo."
    nvl_narrator "{=carta_nvl_text}\nEntiendo.. por ahora intenta descansar. Hare lo mejor que pueda ¿vale?"
    nvl_narrator "{=carta_nvl_text}{redactedglitch}\nPero no siempre sere capaz de esconder tus miedos."
    nvl_narrator "{=carta_nvl_text}{=carta_nvl_text}"
    
window hide
return