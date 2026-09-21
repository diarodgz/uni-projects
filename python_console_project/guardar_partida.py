import os

def guardar(torneo, nombre_archivo):

    # Información de código guardada
    # Para después cargar

    # String largo que contiene la información convertida
    # a formato .csv

    informacion_guardada = ""

    # Dato de eventos
    torneo_eventos = "\n"

    for evento in torneo.eventos:
        torneo_eventos += f"{evento},"

    torneo_guardado = f"""\n{torneo.metros_cavados},{torneo.meta},\
{torneo.dias_transcurridos},{torneo.dias_totales}"""

    # Dato de mochila
    torneo_mochila = ""
    
    for item in torneo.mochila:
        nombre = item.nombre
        tipo = item.tipo
        descripcion = item.descripcion

        if item.tipo == 'consumible':
            energia = item.energia
            fuerza = item.fuerza
            suerte = item.suerte
            felicidad = item.felicidad
            info = f"""\n{nombre},{tipo},{descripcion},{energia}, \
{fuerza}, {suerte}, {felicidad}"""
            torneo_mochila += info
        elif item.tipo == 'tesoro':
            calidad = item.calidad
            cambio = item.cambio
            info = f"""\n{nombre},{tipo},{descripcion},{calidad},{cambio}"""
            torneo_mochila += info

        

    torneo_guardado_arena = f"""\n{torneo.arena.nombre},{torneo.arena.tipo},\
{torneo.arena.rareza},{torneo.arena.humedad},{torneo.arena.dureza},\
{torneo.arena.estatica}
                """
    # Items en la arena
    arena_items = ""

    for item in torneo.arena.items:

        nombre = item.nombre
        tipo = item.tipo
        descripcion = item.descripcion

        if item.tipo == 'consumible':
            energia = item.energia
            fuerza = item.fuerza
            suerte = item.suerte
            felicidad = item.felicidad
            info = f"""\n{nombre},{tipo},{descripcion},{energia},{fuerza},{suerte},{felicidad}"""
            arena_items += info
        elif item.tipo == 'tesoro':
            calidad = item.calidad
            cambio = item.cambio
            info = f"""\n{nombre},{tipo},{descripcion},{calidad},{cambio}"""
            arena_items += info

    # Equipo
    torneo_guardado_equipo = f"""
    """

    for excavador in torneo.equipo:
        nombre = excavador.nombre
        tipo = excavador.tipo
        edad = excavador.edad
        energia = excavador.energia
        fuerza = excavador.fuerza
        suerte = excavador.suerte
        felicidad = excavador.felicidad
        descansando = excavador.descansando

        info = f"""\n{nombre},{tipo},{edad},{energia},{fuerza},{suerte},{felicidad},{descansando}"""

        torneo_guardado_equipo += info
    
    informacion_guardada += torneo_eventos
    informacion_guardada += torneo_guardado
    informacion_guardada += '\n--MOCHILA START--'
    informacion_guardada += torneo_mochila
    informacion_guardada += '\n--MOCHILA FINISH--'
    informacion_guardada += torneo_guardado_arena
    informacion_guardada += '\n--ITEMS START--'
    informacion_guardada += arena_items
    informacion_guardada += '\n--ITEMS FINISH'
    informacion_guardada += torneo_guardado_equipo
    informacion_guardada += '\n--EXCAVADOR END--'

    # DATOS DE LA PARTIDA

    torneo_mochila = "Tu mochila contiene: "
            
    for item in torneo.mochila:
        torneo_mochila += f"\n{item.nombre}, un {item.tipo} que {item.descripcion}"

    datos_equipo = ""

    for excavador in torneo.equipo:
        info = f"""\nNombre: {excavador.nombre}
        \nEdad: {excavador.edad}
        \nEnergia: {excavador.energia}
        \nFuerza: {excavador.fuerza}
        \nSuerte: {excavador.suerte}
        \nFelicidad: {excavador.felicidad}
        \n"""
        datos_equipo += info

        datos_partida = f"""\nDÍA: {torneo.dias_transcurridos} de {torneo.dias_totales}
        \nMetros cavados: {torneo.metros_cavados} m / {torneo.meta} m
        \nLa arena actual es: arena {torneo.arena.tipo}
        \nHan ocurrido los siguientes eventos: {torneo.eventos}
        \n{torneo_mochila}
        \n-------------------------------------
        \n*** DATOS EQUIPO ***
        \n
        \nEl equipo actual es: {datos_equipo}
        \n
        """

        destino = os.path.join('Partidas', nombre_archivo)

        # Escribimos todos los datos en el archivo

        archivo_nuevo = open(destino, "w", encoding='UTF-8')
        archivo_nuevo.writelines("*** DATOS PARA CARGAR ***")
        archivo_nuevo.writelines("\n--------------------------")
        archivo_nuevo.writelines(informacion_guardada)
        archivo_nuevo.writelines("\n--------------------------")
        archivo_nuevo.writelines("\n*** DATOS DE LA PARTIDA ***")
        archivo_nuevo.writelines("\n--------------------------")
        archivo_nuevo.writelines(datos_partida)

        archivo_nuevo.close()
