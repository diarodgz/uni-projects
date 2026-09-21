import parametros as p
import os
import sys
from torneo import Torneo
import instancias as inst
import random
from guardar_partida import guardar
from cargar_partida import cargar

# MENÚ DE INICIO

def menu_inicio():
    print("***MENÚ DE INICIO***")
    print("--------------------")
    for i in range(len(p.options_inicial)):
        print(f"[{i+1}] {p.options_inicial[i]}")
    print("Seleccione una opción: 1, 2, 3")

    choice = input()

    while choice not in p.choice_list_inicial:
            print("Por favor elige un número del 1 al 3.")
            choice = input()

    while choice in p.choice_list_inicial:

        if choice == '1': # Nueva partida

            equipo_inicial = []

            for i in range(p.cantidad_excavadores_iniciales):
                miembro = random.choice(inst.instancias_excavadores)
                equipo_inicial.append(miembro)

                if p.arena_inicial == 'normal':
                    arena_inicial = random.choice(inst.arena_normal)
                elif p.arena_inicial == 'rocosa':
                    arena_inicial = random.choice(inst.arena_rocosa)
                elif p.arena_inicial == 'mojada':
                    arena_inicial = random.choice(inst.arena_mojada)
                else:
                    arena_inicial = random.choice(inst.arena_magnetica)

            arena_inicial.items = inst.items_totales

            nuevo_torneo = Torneo(arena_inicial, equipo_inicial, \
p.metros_meta, p.dia_totales_torneo)

            destino = os.path.join('DCCavaCava.txt')

            archivo_nuevo = open(destino, "w")
            archivo_nuevo.writelines("")
            archivo_nuevo.close()

            menu_principal(nuevo_torneo)
            
        if choice == '2': # Cargar partida

            menu_carga()
                
            
        if choice == '3': # Salir
            sys.exit("Salir del programa.")

        print("***MENÚ DE INICIO***")
        print("--------------------")
        for i in range(len(p.options_inicial)):
            print(f"[{i+1}] {p.options_inicial[i]}")
        print("Seleccione una opción: 1, 2, 3")

        choice = input()
        while choice not in p.choice_list_inicial:
            print("Por favor elige un número del 1 al 3.")
            choice = input()

# MENÚ PRINCIPAL

def menu_principal(torneo):

    print("***MENÚ PRINCIPAL***")
    print("--------------------")
    for i in range(len(p.options_princip)):
        print(f"[{i+1}] {p.options_princip[i]}")
    print("Seleccione una opción: 1, 2, 3, 4, 5, 6")

    choice = input()

    while choice not in p.choice_list_princip:
            print("Por favor elige un número del 1 al 6.")
            choice = input()

    while choice in p.choice_list_princip:

        if choice == '1': # Simular día
            torneo.simular_dia()

            if torneo.dias_transcurridos == torneo.dias_totales:    
                print(f"""Se han acabado los días del torneo.
                \nTu estado final: {torneo.metros_cavados} / {torneo.meta}""")
                if torneo.metros_cavados >= torneo.meta:
                    print("¡Felicitaciones! Lo lograste. :D")
                    menu_inicio()
                else:
                    print("No alcanzaste la meta. ): Intenta de nuevo!")
                    menu_inicio()
            
        if choice == '2': # Mostrar estado
            torneo.mostrar_estado()
            
        if choice == '3': # Ver items
            
            menu_items(torneo)
        
        if choice == '4': # Guardar partida

            print("¿Con qué nombre desee guardar el partido?")
            nombre_partida = input()
            guardar(torneo, nombre_partida)
            print("La partida ha sido guardada exitósamente.")

        if choice == '5': # Volver
            menu_inicio()
        
        if choice == '6':
            sys.exit("Salir del programa.")

        print("***MENÚ DE PRINCIPAL***")
        print("--------------------")
        for i in range(len(p.options_princip)):
            print(f"[{i+1}] {p.options_princip[i]}")
        print("Seleccione una opción: 1, 2, 3, 4, 5, 6")

        choice = input()
        while choice not in p.choice_list_princip:
            print("Por favor elige un número del 1 al 6.")
            choice = input()

def menu_items(torneo):
    
    choice = None
    while choice != f"{len(torneo.mochila) + 2}":
        torneo.mostrar_mochila()

        print(f"[{len(torneo.mochila) + 1}] Usar consumible")
        print(f"[{len(torneo.mochila) + 2}] Volver")
        print(f"Elige la opción [{len(torneo.mochila) + 1}] o [{len(torneo.mochila) + 2}]")

        choices = []

        for i in range(1, len(torneo.mochila) + 3):
            choices.append(f'{i}')

        choice = input()

        while choice not in choices:
            print("Por favor elige un número válido.")
            choice = input()

        if choice == f'{len(torneo.mochila) + 1}':
            torneo.usar_consumible()
    
    
    menu_principal(torneo)

def menu_carga():
    choice = None
    folders = os.listdir('Partidas')

    while choice != f"{len(folders)}":
        print("***MENÚ DE CARGA***")
        print("-------------------")

        for i in range(len(folders)):
            print(f"[{i}] {folders[i]}")

        print(f"[{len(folders)}] Volver")
        print("Escoge su partida.")

        choices = []
        for i in range(len(folders)):
            choices.append(f'{i}')

        choice = input()

        if choice in choices:
            torneo_antiguo = cargar(folders[int(choice)])
            menu_principal(torneo_antiguo)           
        elif choice == f"{len(folders)}":
            pass
        else:
            print("Este archivo no existe. Intente iniciar una partida.")

menu_inicio()