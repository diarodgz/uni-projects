import parametros as p
import instancias as inst
from entidades import ArenaMagnetica, ArenaMojada, ArenaNormal, ArenaRocosa
from entidades import ExcavadorTareo, ExcavadorDocencio, ExcavadorHibrido
import random


class Torneo:
    def __init__(self, arena, equipo, meta, dias_totales):
        self.arena = arena
        self.eventos = []
        self.equipo = equipo
        self.mochila = []
        self.__metros_cavados = 0
        self.meta = meta
        self.dias_transcurridos = 0
        self.dias_totales = dias_totales
        

    @property
    def metros_cavados(self):
        return self.__metros_cavados
    
    @metros_cavados.setter
    def metros_cavados(self, value):
        if value < 0:
            self.__metros_cavados = 0
        else:
            self.__metros_cavados = value



    def simular_dia(self):

        if self.arena.tipo == 'magnetica':
            self.arena.humedad = random.randint(1, 10)
            self.arena.dureza = random.randint(1, 10)

        print(f"** Día {self.dias_transcurridos} **")
        print("------------------------------------")

        # Excavar
        for persona in self.equipo:

            # Revisar si tienen energía
            if persona.energia > 0:
                print(f"{persona.nombre} ha cavado \
{persona.cavar(self.arena.dificultad_arena())} metros.")
                persona.gastar_energia()
                self.metros_cavados += persona.cavar(self.arena.dificultad_arena())

        print(f"El equipo ha cavado {self.metros_cavados} totales.")
        print(" ")
        
        # Encontrar items

        consumibles = 0
        tesoros = 0

        print("Items Encontrados:")
        for persona in self.equipo: 
            if persona.energia > 0:
                item = persona.encontrar_item(self.arena.items)
                
                if item != 'encontró nada.':
                    print(f"{persona.nombre} encontró un {item.nombre} de tipo {item.tipo}.")
                    self.mochila.append(item)
                    if item.tipo == 'consumible':
                        consumibles += 1
                    elif item.tipo == 'tesoro':
                        tesoros +=1
                else:
                    print(f"{persona.nombre} no ha encontrado nada.")
        
        print(f"Se han encontrado {consumibles} consumibles y {tesoros} tesoros.")


        self.iniciar_evento()
        # Qué evento sucedió
        
        print(" ")
        if len(self.eventos) != 0:
            print(f"Durante el día de trabajo sucedió el siguiente evento: {self.eventos[-1]}")
            if self.eventos[-1] != "No ha ocurrido algún evento hoy.":
                # Cómo se vió afectado el equipo.
                print(f"El equipo perdió {p.felicidad_perdida} de felicidad.")

        # Arena final
        print(f"La arena final es: {type(self.arena).__name__}")

        # Quiénes se fueron a descansar
        print("")
        for persona in self.equipo:
            if persona.energia == 0:
                persona.descansar()
                print(f"{persona.nombre} se fue a descansar.")
                #Agregar día de descanso
                persona.dias_descanso += 1

            if persona.dias_descanso >= persona.descansar():
                persona.descansando = False
                persona.energia = 100
                persona.dias_descanso = 0
               

        self.dias_transcurridos += 1

        

    def mostrar_estado(self):

        titulo = "*** ESTADO TORNEO ***"
        titulo_ex = "EXCAVADORES"
        estado = f"Día actual: {self.dias_transcurridos}"
        arena = f"Tipo de arena: {type(self.arena).__name__}"
        cavado = f"Metros excavados: {self.metros_cavados} / {self.meta}"

        divider = '-'
        for i in range(150):
            divider += '-'

        print(divider)
        print(titulo.center(150))
        print(divider)
        print(estado.center(150))
        print(arena.center(150))
        print(cavado.center(150))
        print(" ")
        print(divider)
        print(titulo_ex.center(150))
        print(divider)
        n = "NOMBRE"
        t = "TIPO"
        e = "ENERGÍA"
        f = "FUERZA"
        s = "SUERTE"
        fe = "FELICIDAD"

        print(f"{n:37.37s} | {t:20.20s} | {e:10.10s} | \
{f:10.10s} | {s:10.10s} | {fe:10.10s} |")

        print(divider)

        for i in range(len(self.equipo)):
            print(f"[{(i + 1):2d}] | {self.equipo[i].nombre:30.30s} | \
{type(self.equipo[i]).__name__:20.20s} | \
{self.equipo[i].energia:10d} | {self.equipo[i].fuerza:10d} | \
{self.equipo[i].suerte:10d} | {self.equipo[i].felicidad:10d} |")

        print(divider)
        print("\n")

    def mostrar_mochila(self):
        divider = '-'
        for i in range(150):
            divider += '-'

        print(divider)
        titulo = "*** MENÚ ÍTEMS ***"
        n = "NOMBRE"
        t = "TIPO"
        d = "DESCRIPCION"

        print(titulo.center(150))
        print(divider)
        print(f"{n:42.42s} | {t:15.15s} | {d:65.65s} |")
        

        print(divider)
        for i in range(len(self.mochila)):
            print(f"[{(i + 1):2d}] | {self.mochila[i].nombre:35.35s} | \
{type(self.mochila[i]).__name__:15.15s} | \
{self.mochila[i].descripcion:65.65s} |")

        print(divider)
        print("\n")

    def usar_consumible(self):
        # Mostrar tabla
        # Seleccionar item según índice
        # Ejecutar efectos item sobre cada uno de los excavadores

        # Revisar si hay items para usar o no.
        if len(self.mochila) > 0:
            
            options = []

            for i in range(1, len(self.mochila) + 1):
                options.append(int(i))
                
            print("")
            print(f"Escoge un item del 1 al {len(self.mochila)}:")
            print("")
            choice = int(input())

            while choice not in options:
                print(f"Por favor elige una opción del 1 al f{len(self.mochila)}")
                choice = int(input())

            chosen_consumible = self.mochila.pop(choice - 1)
            self.arena.items.append(chosen_consumible)

            if type(chosen_consumible).__name__ == 'Consumibles':
                for excavador in self.equipo:
                    excavador.consumir(chosen_consumible)

                print(f"El equipo experimentó los siguientes cambios:\nEnergia: +\
        {chosen_consumible.energia}\nFuerza: +{chosen_consumible.fuerza}\
        \nSuerte: +{chosen_consumible.suerte}\nFelicidad: +{chosen_consumible.felicidad}")
                
            else:
                self.abrir_tesoro(chosen_consumible)
        else:
            print("Aún no tienes items.")

    def abrir_tesoro(self, chosen_tesoro):
        
        # Agrandar el equipo.

        if chosen_tesoro.cambio == 'docencio':
            nuevo_excavador = random.choice(inst.excavador_docencio)
            self.equipo.append(nuevo_excavador)
            print(f"El equipo ha adquirido un excavador docencio: {nuevo_excavador.nombre}")

        elif chosen_tesoro.cambio == 'tareo':
            nuevo_excavador = random.choice(inst.excavador_tareo)
            self.equipo.append(nuevo_excavador)
            print(f"El equipo ha adquirido un excavador docencio: {nuevo_excavador.nombre}")

        elif chosen_tesoro.cambio == 'hibrido':
            nuevo_excavador = random.choice(inst.excavador_hibrido)
            self.equipo.append(nuevo_excavador)
            print(f"El equipo ha adquirido un excavador docencio: {nuevo_excavador.nombre}")

        # Cambiar la arena.

        if chosen_tesoro.cambio == 'normal':
            nueva_arena = random.choice(inst.arena_normal)
            self.arena = nueva_arena
            print(f"La arena se ha cambiado a: {nueva_arena.tipo}")

        elif chosen_tesoro.cambio == 'mojada':
            nueva_arena = random.choice(inst.arena_mojada)
            self.arena = nueva_arena
            print(f"La arena se ha cambiado a: {nueva_arena.tipo}")
        elif chosen_tesoro.cambio == 'rocosa':

            nueva_arena = random.choice(inst.arena_rocosa)
            self.arena = nueva_arena
            print(f"La arena se ha cambiado a: {nueva_arena.tipo}")
        elif chosen_tesoro.cambio == 'magnetico' or chosen_tesoro.cambio == 'magnético':
            nueva_arena = random.choice(inst.arena_magnetica)
            self.arena = nueva_arena
            print(f"La arena se ha cambiado a: {nueva_arena.tipo}")



    def iniciar_evento(self):
        # Acá usar probabilidades
        # Ejecutar efectos de lluvia, terremoto o derrumbe

        PROB_INICIAR_EVENTO = p.prob_iniciar_evento

        def event_start():
            return random.random() <= PROB_INICIAR_EVENTO    
            
        def cual_evento():    
            actual_proba = random.random()
            if actual_proba <= p.prob_lluvia:
                self.lluvia()
            elif actual_proba <= p.prob_lluvia + p.prob_derrumbe:
                self.derrumbe()
            elif actual_proba <= p.prob_lluvia + p.prob_derrumbe + p.prob_terremoto:
                self.terremoto()
    
        if event_start():
            for excavador in self.equipo:
                excavador.felicidad -= p.felicidad_perdida
            cual_evento()
        else:
            self.eventos.append("No ha ocurrido algún evento hoy.")

    def lluvia(self):
        # Colocar efectos lluvia
        if self.arena.tipo == 'normal':
            nueva_arena = random.choice(inst.arena_mojada)
            nueva_arena.items += inst.items_totales                        
            self.arena = nueva_arena

        elif self.arena.tipo == 'rocosa':
            nueva_arena = random.choice(inst.arena_magnetica)
            nueva_arena.items += inst.items_totales
            self.arena = nueva_arena

        self.eventos.append('Lluvia')

    def terremoto(self):
        # Colocar efectos terremoto
        if self.arena.tipo == 'normal':
            nueva_arena = random.choice(inst.arena_rocosa)
            nueva_arena.items += inst.items_totales
            self.arena = nueva_arena

        elif self.arena.tipo == 'mojada':
            nueva_arena = random.choice(inst.arena_magnetica)
            nueva_arena.items += inst.items_totales
            self.arena = nueva_arena

        self.eventos.append('Terremoto')

    def derrumbe(self):
        # Colocar efectos derrumbe
        if self.arena.tipo != 'normal':
            nueva_arena = random.choice(inst.arena_normal)
            nueva_arena.items += inst.items_totales
            self.arena = nueva_arena
            self.metros_cavados -= p.metros_perdidos_derrumbe

        self.eventos.append('Derrumbe')