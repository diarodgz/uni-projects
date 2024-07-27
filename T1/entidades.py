from abc import ABC, abstractmethod
import parametros as p
import random


class Excavador(ABC):
    def __init__(self, nombre: str, tipo: str, edad: int, energia: int, \
                 fuerza: int, suerte: int, felicidad: int):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = int(edad)
        self.__energia = int(energia)
        self.__fuerza = int(fuerza)
        self.__suerte = int(suerte)
        self.__felicidad = int(felicidad)
        self.dias_descanso = 0
        self.descansando = False
    
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, value):
        if value < 0:
            self.__energia = 0
        elif value >= 1 and value <= 100:
            self.__energia = value
        elif value > 100:
            self.__energia = 100

    @property
    def fuerza(self):
        return self.__fuerza
    
    @fuerza.setter
    def fuerza(self, value):
        if value < 1:
            self.__fuerza = 1
        elif value  >= 1 and value <= 10:
            self.__fuerza = value
        elif value > 10:
            self.__fuerza = 10

    @property
    def suerte(self):
        return self.__suerte
    
    @suerte.setter
    def suerte(self, value):
        if value < 1:
            self.__suerte = 1
        elif value >= 1 and value <= 10:
            self.__suerte = value
        elif value > 10:
            self.__suerte = 10
    
    @property
    def felicidad(self):
        return self.__felicidad
    
    @felicidad.setter
    def felicidad(self, value):
        if value < 1:
            self.__felicidad = 1
        elif value >= 1 and value <= 10:
            self.__felicidad = value
        elif value > 10:
            self.__felicidad = 10

    def cavar(self, dificultad_arena):
        return round((30/self.edad + (self.felicidad + 2 * self.fuerza) / 10 \
                        * (1 / (10 * (dificultad_arena)))), 2)
    
    def descansar(self):
        dias_descansar = int(self.edad / 20)
        if dias_descansar > 0 or self.dias_descanso < dias_descansar:
            self.descansando = True
        
        return dias_descansar
    
    def encontrar_item(self, arena):

        PROB_ENCONTRAR = p.prob_encontrar_item * (self.suerte / 10)

        def encontrar():
            return random.random() <= PROB_ENCONTRAR  
    
        def hallazgo():    
            actual_proba = random.random()
            if actual_proba <= p.prob_encontrar_tesoro:

                tesoro = random.choice(arena)
                
                while tesoro.tipo == 'consumible' and len(arena) > 0:
                    tesoro = random.choice(arena)

                return tesoro

            
            elif actual_proba <= p.prob_encontrar_tesoro + p.prob_encontrar_consumible:

                consumible = random.choice(arena)
                
                while consumible.tipo == 'tesoro' and len(arena) > 0:
                    consumible = random.choice(arena)

                return consumible
        
        if encontrar():
            return hallazgo()
        else:
            return "encontró nada."

    
    def gastar_energia(self):
        energia_gastada = int(10 / self.fuerza + self.edad / 6)
        self.energia -= energia_gastada
    
    def consumir(self, consumible):
        self.energia += int(consumible.energia)
        self.fuerza += int(consumible.fuerza)
        self.suerte += int(consumible.suerte)
        self.felicidad += int(consumible.felicidad)
    
    def __repr__(self) -> str:
        return f"""{type(self).__name__}({self.nombre}, {self.edad}, \
{self.tipo}, {self.__energia}, {self.__fuerza}, {self.__suerte}, {self.felicidad})"""
    


class ExcavadorDocencio(Excavador):
    def __init__(self, nombre, tipo, edad, energia, fuerza, suerte, felicidad):
        super().__init__(nombre, tipo, edad, energia, fuerza, suerte, felicidad)

    def cavar(self, dificultad_arena):
        self.felicidad += p.felicidad_adicional_docencio
        self.fuerza += p.fuerza_adicional_docencio
        return super().cavar(dificultad_arena)
    
    def gastar_energia(self):
        energia_gastada = int(10 / self.fuerza + self.edad / 6)
        self.energia -= energia_gastada + p.energia_perdida_docencio

class ExcavadorTareo(Excavador):
    def __init__(self, nombre, tipo, edad, energia, fuerza, suerte, felicidad):
        super().__init__(nombre, tipo, edad, energia, fuerza, suerte, felicidad)

    def gastar_energia(self):
        return super().gastar_energia()

    def consumir(self, consumible):
        #super().consumir(consumible)
        self.energia += consumible.energia + int(p.energia_adicional_tareo)
        self.fuerza += consumible.fuerza 
        self.suerte += consumible.suerte + int(p.suerte_adicional_tareo)
        self.edad += int(p.edad_adicional_tareo)
        self.felicidad += consumible.felicidad + int(p.felicidad_perdida_tareo)

class ExcavadorHibrido(ExcavadorDocencio, ExcavadorTareo):
    def __init__(self, nombre, tipo, edad, energia, fuerza, suerte, felicidad):
        super().__init__(nombre, tipo, edad, energia, fuerza, suerte, felicidad)
        self.__energia = energia

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, value):
        if value < 20:
            self.__energia = 20
        elif value >= 20 and value <= 100:
            self.__energia = value
        elif value > 100:
            self.__energia = 100

    def gastar_energia(self):
        energia_gastada = int(10 / self.fuerza + self.edad / 6) + int(p.energia_perdida_docencio)
        self.energia -= energia_gastada

    def consumir(self, consumible):
        self.energia += consumible.energia + int(p.energia_adicional_tareo)
        self.fuerza += consumible.fuerza 
        self.suerte += consumible.suerte + int(p.suerte_adicional_tareo)
        self.edad += int(p.edad_adicional_tareo)
        self.felicidad += consumible.felicidad + int(p.felicidad_perdida_tareo)


class Arena(ABC):
    def __init__(self, nombre: str, tipo: str, rareza: int, humedad: int, \
                 dureza: int, estatica: int, items: list):
        self.nombre = nombre
        self.tipo = tipo
        self.__rareza = int(rareza)
        self.__humedad = int(humedad)
        self.__dureza = int(dureza)
        self.__estatica = int(estatica)
        self.items = items

    @property
    def rareza(self):
        return self.__rareza
    
    @rareza.setter
    def rareza(self, value):
        if value < 0:
            self.__rareza = 0
        elif value >= 1 and value < 10:
            self.__rareza = value
        elif value > 10:
            self.__rareza = 10
    
    @property
    def humedad(self):
        return self.__humedad
    
    @humedad.setter
    def humedad(self, value):
        if value < 0:
            self.__humedad = 0
        elif value >= 1 and value <= 10:
            self.__humedad = value
        elif value > 10:
            self.__humedad = 10

    @property
    def dureza(self):
        return self.__dureza
    
    @dureza.setter
    def dureza(self, value):
        if value < 0:
            self.__dureza = 0
        elif value >= 1 and value <= 10:
            self.__dureza = value
        elif value > 10:
            self.__dureza = 10

    @property
    def estatica(self):
        return self.__estatica
    
    @estatica.setter
    def estatica(self, value):
        if value < 0:
            self.__estatica = 0
        elif value >= 1 and value <= 10:
            self.__estatica = value
        elif value > 10:
            self.__estatica = 10

    def __repr__(self) -> str:
        return f"""{type(self).__name__}({self.nombre},\
{self.tipo}, {self.__rareza}, {self.__humedad}, {self.__dureza},\
{self.__estatica}, {self.items})"""

    @abstractmethod
    def dificultad_arena():
        pass

class ArenaNormal(Arena):
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica, items):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    def dificultad_arena(self):
        dificultad = round((self.rareza + self.humedad + self.dureza + self.estatica) / 40, 2)
        return round(dificultad * p.pond_arena_normal, 2)
        

class ArenaMojada(Arena):
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica, items):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    def dificultad_arena(self):
        dificultad = round((self.rareza + self.humedad + self.dureza + self.estatica) / 40, 2)
        return round(dificultad, 2)


class ArenaRocosa(Arena):
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica, items):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    def dificultad_arena(self):
        dificultad = round((self.rareza + self.humedad + 2 * self.dureza + self.estatica) / 50, 2)
        return dificultad


class ArenaMagnetica(ArenaRocosa, ArenaMojada):
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica, items):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    def dificultad_arena(self):
        dificultad_rocosa = round((self.rareza + self.humedad + 2 * self.dureza + self.estatica) / 50, 2)
        return round(dificultad_rocosa * p.pond_arena_normal, 2)


class Item(ABC):
    def __init__(self, nombre: str, tipo: str, descripcion: str):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion

    def __repr__(self) -> str:
        return f"""{type(self).__name__}({self.nombre}, {self.tipo}, {self.descripcion})"""

class Tesoros(Item):
    def __init__(self, nombre, tipo, descripcion, calidad: int, cambio: str):
        super().__init__(nombre, tipo, descripcion)
        self.calidad = calidad
        self.cambio = cambio

    def __repr__(self) -> str:
        return f"""{type(self).__name__}({self.nombre}, {self.tipo},\
{self.descripcion}, {self.calidad}, {self.cambio})"""

class Consumibles(Item):
    def __init__(self, nombre: str, tipo: str, descripcion: str, energia: int, \
                 fuerza: int, suerte: int, felicidad: int):
        super().__init__(nombre, tipo, descripcion)
        self.energia = int(energia)
        self.fuerza = int(fuerza)
        self.suerte = int(suerte)
        self.felicidad = int(felicidad)
    
    def __repr__(self) -> str:
        return f"""{type(self).__name__}({self.nombre}, {self.tipo}, {self.descripcion},\
{self.energia}, {self.fuerza}, {self.suerte}, {self.felicidad})"""
    

    