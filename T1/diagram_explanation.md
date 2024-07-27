# Diagrama de Clase - DCCavaCava 🏖⛏

## 1. Torneo

Tiene los siguientes atributos: 

- arena: Arena[] - Este argumento tiene que ser uno de los tipos de arena que heredan de la clase abstracta Arena.
- eventos: list
- equipo: list
- mochila: list
- metros_cavados: float
- meta: float
- dias_transcurridos: int
- dias_totales: int

Tiene los siguientes métodos:

- simular_dia(): str
- mostrar_estado(): None
- ver_mochila(): None
- usar_consumible(): None
- abrir_tesoro(): None
- iniciar_evento(): None
- lluvia(): None
- terremoto(): None
- derrumbe(): None

La mayoría de estos métodos retorna None por el momento. Hasta el momento, es porque estos se encargarán solamente de efectuar prints de lo que será pedido, como es el caso de **simular_dia()**, **mostrar_estado()**, y **ver_mochila()**. Los métodos que quedan efectuan cambios dentro de los atributos de _Torneo_ por lo que estos no retornarán nada.

## 2. Item

Tiene los siguientes atributos:

- nombre: str
- tipo: str
- descripcion: str

El enunciado no especifica algún método, por lo tanto, hasta aquí llega. El diagrama indica que existe una relación de composición entre la clase Item y Torneo. Esto porque la mochila conlleva items, y aunque Torneo seguirá existiendo sin Item, sus métodos no se podrían emplear en la ausencia de este último.

## 3. Tesoro

Tiene los siguientes atributos:

- calidad: int
- cambio: int

**Hereda de Item**. No tiene método alguno.

## 4. Consumible

- energia: int
- fuerza: int
- suerte: int
- felicidad: int

Por la misma razón que Item tiene una relación de composición con Torneo.

## 5. Arena (Clase Abstracta)

Tiene los siguientes atributos:

- nombre: str
- tipo: str
- rareza: int (Privado)
- humedad: int (Privado)
- dureza: int (Privado)
- estatica: int (Privado)
- items: list (Privado)

Los atributos privados se asignaron así para obtener los setters que aseguran que los valores se mantengan entre 1 y 10.

Tiene los siguientes métodos:

- dificultad_arena(): float

## 5.1 ArenaNormal, ArenaRocosa, ArenaMojada

**Heredan de arena**. Poseen el mismo método:

- dificultad_arena(): float

Pero se hacen los overrides correspondientes con lo que pide el enunciado.

## 5.3 ArenaMagnetica

**Hereda de ArenaRocosa y ArenaMojada**. 

Sus métodos son:

- dificultad_arena(): float
- calcular_valor(): None - Este tiene el propósito de cambiar los valores de humedad y dureza cada vez que se inicie el proceso de Simular día Torneo.

## 6. Excavador (Clase Abstracta)

Tiene los siguientes atributos:

- nombre: str
- edad: int
- energia: int
- fuerza: int
- suerte: int
- felicidad: int

Tiene los siguientes métodos:

- cavar(): float
- descansar(): int
- encontrar_item(): int
- gastar_energia(): int
- consumir(): None

El método **consumir()** retorna None porque efectua cambios dentro del objeto, es decir, en sus atributos.

## 6.1 ExcavadorDocencio

**Hereda de Excavador.** 
Tiene los siguientes métodos:

- cavar(): None.

## 6.2 ExcavadorTareo

**Hereda de Excavador.** 
Tiene los siguientes métodos:

- consumir(): None.

## 6.3 ExcavadorHibrido

**Hereda de ExcavadorDocencio y ExcavadorTareo.** 
Tiene los siguientes métodos:

- cavar(): None.