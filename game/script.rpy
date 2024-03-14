# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define unknown = Character("???", color="#000000")
# El juego comienza aquí.

label start:
    "Nunca he creido que la vida fuera dura."
    "Claro, algunos pueden nacer en condiciones más dificiles."
    "Pueden tener un ambiente que limite su crecimiento o no les ofrezca muchas oportunidades."
    "pueden haber tenido unos padres molestos, indiferentes, o incluso no tenerlos."
    "Pero si tienen la determinación suficiente, si sobrellevan los problemas aprovechando las oportunidades y, sobretodo, no pierden la esperanza, al final del camino solo les esperará un rotundo exito."
    "Después de todo, no se trata de que tan dura sea la situación, sino de cómo la afrontes."
    "Por eso, nunca he creído que la vida sea dura."
    "..."
    "O almenos, nunca lo habia creido."
    image city_night = "scene_1.png"
    scene city_night
    with fade
    "Oouah*, sabía que la fiesta de hoy también iba a terminar hasta casi la madrugada."
    "Esos desgraciados, no debí confiar en ellos cuando me dijeron que solo sería bailar un rato y tomar un par de copas."
    "Sobre todo considerando que más rato tengo clases en el campus, no tengo tiempo que perder si quiero al menos descansar unas cuantas horas."
    "Oouah*, pero en serio espero llegar rápido al apartamento para poder dormir algo."
    "No le puedo dar el gusto al profesor de tener algo para echarme en cara considerando como lo corregí la última vez en medio de la clase."
    "Bueno, no es mi culpa que no haya verificado bien la información y la intente declarar como la verdad absoluta."
    "¿Y eso que me esforcé para no reírme en medio de su explicación, debería agradecerme por la madurez que mostré, pocas personas tienen la capacidad de controlarse como yo, ¿sabes?."
    "Pero en fin, ya estoy a una calle de mi destino."
    "Ahora solo queda acostarme y tener un pequeño des..."
    # Ruido de camion
    play sound "audio/car_approaching.mp3"
    unknown "¡Aléjense! El carro perdio el control. No puedo pararlo"
    "Mierda, tengo que alejarme rápido de la carretera"
    "Uahh, de todos los momentos este es el peor para tener las secuelas de la fiesta."
    unknown "¡Vete de ahí chico!"
    "¡No hace falta que me lo digas!, estoy tratando de recuperar el sentido, no es como si tuviera ganas de enfrentarme a un camión a gran velocidad o algo así."
    "¡Ah! Eso sonó demasiado tsundere, no recuerdo haber tenido esta faceta en mí"
    "Mi visión empieza a captar las cosas en cámara lenta, la única desventaja de este poder es que solo se activa cuando todo lo que hay en mi campo de visión son las luces de la parte frontal de un camión de más de 8 toneladas."
    "..."
    "Es un poco lamentable que este sea mi último pensamiento."
    play sound "audio/car_crash.mp3"  #Sonido de choque
    image bg_black = "scene_black.png" #Pantalla en negro
    scene bg_black
    "..."
    "La oscuridad lo envuelve todo."
    "Esto debe ser la muerte, ¿verdad?"
    "¿O será que estoy enfrentando mi último suspiro?"
    "Dudo que alguien pudiera haber sobrevivido a ese impacto, al menos sin continuar sintiendo un dolor tan intenso como  el que sentí en el momento del choque."
    "Supongo que significa que esto es la muerte."
    "Nunca contemplé mucho el final de mi vida, no lo consideraba importante todavía, así que ni siquiera tengo una idea de qué hubiera deseado esperar."
    "Pero esta  sensación, este lugar, se siente... desolado."
    "Un vacío infinito, donde la mente sigue funcionando sin cesar, sin compañía, sin saber si habrá fin, o si continuará eternamente; sin duda, sería el mismo infierno."
    "Si no fuera por el frío que atraviesa mi piel, ya estaría enloqueciendo."
    "¡Espera, ¿frío?"
    "Noto cómo mis sentidos se propagan por mis extremidades, las mismas que creí haber perdido para siempre."
    "Con esfuerzo, intento abrir lo que sospecho son mis párpados."
    "Gradualmente comienzo a discernir los contornos que encuentro en mi visión."
    #Efecto de parpadeo
    "¿Donde Estoy?"
    "Me siento un tanto... extraño."
    "Es como si estuviera desconectado de mí mismo."

    #entonces que queria que hiciera! no entiendes nada! de la nada me encuentro en un lugar extraño y oscuro, sin fuerzas y sin tener ni idea de hacer o como continuar despues de aver... de aver...
    image elfa = "elf_3.png" 
    show elfa at right
    "esta bien facha, a que si?"
    hide elfa
    image elfa_2 = "elf_4.png" 
    show elfa_2
    "Esta es mi historia"

    return
