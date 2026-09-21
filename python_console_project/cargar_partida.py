from instancias import crear_objeto, items_totales
from torneo import Torneo
import os

def cargar(nombre_archivo):

    destino = os.path.join('Partidas', nombre_archivo)
    with open(destino, 'r', encoding='UTF-8') as file:
        lineas = file.readlines()

    # Datos Torneo:

    eventos = lineas[2].rstrip(',\n').split(',')
    equipo = []
    mochila = []
    arena_items = []

    # DATOS TORNEO
    metros_cavados, meta, dias_transcurridos, dias_total = lineas[3].rstrip(',\n').split(',')

    # Puntos de inicio y fin de iteración
    start_mochila = '--MOCHILA START--\n'
    end_mochila = '--MOCHILA FINISH--\n'
    start_ex = "--ITEMS FINISH\n"
    end_ex = "--EXCAVADOR END--\n"
    start_item = '--ITEMS START--\n'

    # DATOS MOCHILA

    for i in range(lineas.index(start_mochila) + 1, lineas.index(end_mochila)):
        
        item = lineas[i].rstrip("\n").split(",")
        if item[1] == 'consumible':
            item.pop(1)
            new_object = crear_objeto(item, 'consumibles')
            mochila.append(new_object)
        if item[1] == 'tesoro':
            item.pop(1)
            new_object = crear_objeto(item, 'tesoros')
            mochila.append(new_object)

    # DATOS ITEMS

    for i in range(lineas.index(start_item) + 1, lineas.index(start_ex)):
        
        item = lineas[i].rstrip("\n").split(",")
        if item[1] == 'consumibles':
            item.pop(1)
            new_object = crear_objeto(item, 'consumibles')
            arena_items.append(new_object)
        elif item[1] == 'tesoros':
            item.pop(1)
            new_object = crear_objeto(item, 'tesoros')
            arena_items.append(new_object)   

    # DATOS EXCAVADORES

    for i in range(lineas.index(start_ex) + 1, lineas.index(end_ex)):

        item = lineas[i].rstrip("\n").split(",")
        if len(item) > 2:
            new_object = crear_objeto(item, 'excavadores')
            new_object.descansando = item[-1]
            equipo.append(new_object)
            
        # DATOS ARENA

    for i in range(lineas.index(end_mochila) + 1, lineas.index(start_item)):
        item = lineas[i].rstrip("\n").split(",")
        if len(item) > 2:
            item[1].lstrip(" ")
            arena = crear_objeto(item, 'arenas')

    arena.items += items_totales

    partida = Torneo(arena, equipo, int(meta), int(dias_total))

    partida.metros_cavados = float(metros_cavados)
    partida.eventos = eventos
    partida.dias_transcurridos = int(dias_transcurridos)
    partida.mochila = mochila

    return partida
