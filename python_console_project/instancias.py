import os
import entidades as ent
import random

def obtener_datos(archivo: str) -> list:
    
    object_list = []

    path = os.path.join("T1", archivo)

    with open(archivo, 'r', encoding='UTF-8') as file:
        file_list = file.readlines()

    for i in range(1, len(file_list)):
        item = file_list[i].rstrip("\n").split(",")
        object_list.append(item)

    # Retorna una sola lista con los valores
    # Para los atributos del objeto

    return object_list


def crear_objeto(item: list, object_type: str) -> object:
    
    if object_type == 'consumibles':

        name = item[0]
        tipo = 'consumible'
        descrip = item[1]
        energia = int(item[2])
        fuerza = int(item[3])
        suerte = int(item[4])
        felicidad = int(item[5])

        return ent.Consumibles(name, tipo, descrip, energia, fuerza, suerte, felicidad)
    
    if object_type == 'excavadores':
       
        name = item[0]
        tipo = item[1]
        edad = item[2]
        energia = int(item[3])
        fuerza = int(item[4])
        suerte = int(item[5])
        felicidad = int(item[6])

        if tipo == 'docencio':
            return ent.ExcavadorDocencio(name, tipo, edad, energia, fuerza, suerte, felicidad)

        if tipo == 'tareo':
            return ent.ExcavadorTareo(name, tipo, edad, energia, fuerza, suerte, felicidad)
        
        if tipo == 'hibrido':
            return ent.ExcavadorHibrido(name, tipo, edad, energia, fuerza, suerte, felicidad)
        
    if object_type == 'arenas':

        name = item[0]
        tipo = item[1]
        rareza = int(item[2])
        humedad = int(item[3])
        dureza = int(item[4])
        estatica = int(item[5])
        list_items = []

        if tipo == 'magnética' or tipo == 'magnetica':
            return ent.ArenaMagnetica(name, tipo, rareza, humedad, dureza, estatica, list_items)

        if tipo == 'normal':
            return ent.ArenaNormal(name, tipo, rareza, humedad, dureza, estatica, list_items)
        
        if tipo == 'mojada':
            return ent.ArenaMojada(name, tipo, rareza, humedad, dureza, estatica, list_items)

        if tipo == 'rocosa':
            return ent.ArenaRocosa(name, tipo, rareza, humedad, dureza, estatica, list_items)
        
    if object_type == 'tesoros':

        name = item[0]
        tipo = 'tesoro'
        descrip = item[1]
        calidad = item[2]
        cambio = item[3]

        return ent.Tesoros(name, tipo, descrip, calidad, cambio)

excavadores = obtener_datos("excavadores.csv")
arenas = obtener_datos("arenas.csv")
tesoros = obtener_datos("tesoros.csv")
consumibles = obtener_datos("consumibles.csv")

instancias_excavadores = []
instancias_arenas = []
instancias_tesoros = []
instancias_consumibles = []

for i in range(len(excavadores)):
    objeto = crear_objeto(excavadores[i], 'excavadores')
    instancias_excavadores.append(objeto)

for i in range(len(arenas)):
    objeto = crear_objeto(arenas[i], 'arenas')
    instancias_arenas.append(objeto)

for i in range(len(tesoros)):
    objeto = crear_objeto(tesoros[i], 'tesoros')
    instancias_tesoros.append(objeto)

for i in range(len(consumibles)):
    objeto = crear_objeto(consumibles[i], 'consumibles')
    instancias_consumibles.append(objeto)

arena_normal = []
arena_rocosa = []
arena_mojada = []
arena_magnetica = []

for arena in instancias_arenas:
    if arena.tipo == 'normal':
        arena_normal.append(arena)
    elif arena.tipo == 'rocosa':
        arena_rocosa.append(arena)
    elif arena.tipo == 'mojada':
        arena_mojada.append(arena)
    else:
        arena_magnetica.append(arena)

excavador_docencio = []
excavador_tareo = []
excavador_hibrido = []

for excavador in instancias_excavadores:
    if type(excavador).__name__ == 'ExcavadorDocencio':
        excavador_docencio.append(excavador)
    elif type(excavador).__name__  == 'ExcavadorTareo':
        excavador_tareo.append(excavador)
    else:
        excavador_hibrido.append(excavador)

items_totales = instancias_consumibles + instancias_tesoros