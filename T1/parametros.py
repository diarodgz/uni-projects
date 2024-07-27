import random

choice_list_inicial = ['1', '2', '3']
options_inicial = ["Nueva partida", "Cargar partida", "Salir"]

choice_list_princip = ['1', '2', '3', '4', '5', '6']
options_princip = [
    "Simular día torneo", "Ver estado torneo", "Ver items", 
    "Guardar partida", "Volver", 
    "Salir del programa"]


dia_totales_torneo = 20

tipos_arena = ["normal", "magnética", "rocosa", "mojada"]

arena_inicial = random.choice(tipos_arena)

cantidad_excavadores_iniciales = random.randint(1, 9)

metros_meta = 20

dias_torneo = 5

prob_encontrar_item = 0.5

prob_encontrar_consumible = 0.7

prob_encontrar_tesoro = 0.3

prob_iniciar_evento = 0.6

prob_lluvia = 0.1

prob_terremoto = 0.6

prob_derrumbe = 0.3

metros_perdidos_derrumbe = 3

felicidad_perdida = 3

pond_arena_normal = 3

felicidad_adicional_docencio = 2

energia_perdida_docencio = 6

fuerza_adicional_docencio = 3

felicidad_adicional_tareo = 4

energia_perdida_tareo = 5

edad_adicional_tareo = 3

energia_adicional_tareo = 1

suerte_adicional_tareo = 2

felicidad_perdida_tareo = 3
