# Tarea 1: DCCavaCava 🏖⛏


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

La tarea puede / ocupa: 
- Despliegar correctamente el menú inicial y el menú principal. 
- Puedes escoger una opción del menú principal y puede volver a despliegar el menú principal. 
- Puede volver al menú inicial. Puede simular un día, ver items de la mochila, usar un consumible, mostrar el estado del torneo.
- Puede despliegar el menú de items. Puede emplear el método usar_consumible(), mostrando los efectos debidos, y volver al menú principal desde el menú de items. Puede actualizar la lista de items cuando se usa un consumible.
- Puede crear una nueva partida, guardarla con nombre, y sobreescribir archivos.
- Puede despliegar el menú de carga, y desde aquí, volver al menú de inicio.
- Herencia, clases abstractas y properties.
- Revisa errores.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Programación Orientada a Objetos: 42 pts (35%)
##### ✅  Diagrama
##### ✅ Definición de clases, atributos, métodos y properties
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (9%)
##### ✅ Creación de partidas
- Se puede crear una partida nueva. Sobreescribe el archivo.
#### Entidades: 22 pts (18%)
##### 🟠 Excavador
- Puede cavar, gastar energía, y consumir un consumible correctamente. El método descansar presenta fallos, pero muchas veces funciona correctamente. Sus atributos se setean dentro del rango correspondiente. Estas habilidades se extienden a las clases hijas, cuyos métodos fueron modificados según los parámetros correspondientes.
##### ✅ Arena
- Puede almacenar items. Se instancia correctamente. Método dificultad_arena() implementada correctamente.
##### ✅ Torneo
- Puede simular el día, ver el estado, abrir la mochila, iniciar un evento, usar un consumible, abrir un tesoro, y aplicar los efectos debidos.
#### Flujo del programa: 31 pts (26%)
##### ✅ Menú de Inicio
- Se despliegan todas las opciones correctamente. Se manejan los inputs.
##### ✅ Menú Principal
- Se despliegan las opciones correctamente. Se puede abrir el menú de items y volver al menú principal. Todas las opciones se ejecutan correctamente.
##### ✅ Simulación día Torneo
- Se indica el día del torneo, los metros cavados por cada excavador, qué items encontró y detalles, cuántos de cada tipo de ítem encontró, la arena final, y quiénes se fueron a descansar.
##### ✅ Mostrar estado torneo
- Se indica el día del torneo, metros cavados / metros por cavar hasta llegar a la meta, tipo de arena actual, y los detalles relevantes de cada miembro del equipo.
##### ✅ Menú Ítems
- Se despliegan los items en la mochila junto con los datos relevantes. Se puede volver al menú principal o utilizar un consumible.
##### ✅ Guardar partida.
- Se guarda correctamente la partida.
##### ✅ Robustez
- Se manejan los inputs y los errores correctamente.
#### Manejo de archivos: 14 pts (12%)
##### ✅ Archivos CSV 
##### ✅ Archivos TXT
##### ✅ parametros.py
- Los tres archivos se procesan o están establecidos correctamente.
#### Bonus: 3 décimas máximo
##### ✅ Guardar Partida
- Se puede guardar archivos con distintos nombres y elegir una de ellas para cargarla.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Partidas``` en ```Tareas\T1```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```sys.exit()```
2. ```os```: ```os.path.join()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:


1. ```torneo.py```: Contiene solamente la definición de la clase Torneo.
2. ```entidades.py```: Contiene las clases Excavador, Arena, Item, y sus clases hijas.
3. ```instancias.py```: Contiene un método ```obtener_datos()``` para accesar y procesar los archivos .csv, y otro ```crear_objetos()``` para instanciar los objetos del juego. En este mismo módulo se instancian todos los objetos requeridos.
4. ```guardar_partida.py```: Hecha para almacenar información de la partida en DCCavaCava.txt y archivos .txt para que quede registro de la partida, y los datos para volver a cargar la partida. Tiene un método ```guardar()```.
5. ```cargar_partida.py```: Hecha para procesar el archivo DCCavaCava.txt y los archivos dentro de ```\Partidas``` para reconstruir el objeto Torneo con las clases correspondientes, y mantener sus atributos correspondientes. Tiene un método ```cargar()```.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los items de la arena se van reciclando. Es decir, desaparecen de la mochila y pueden volver a encontrarse dentro de la arena. Esto para que nunca esté vacío la arena, pues le quitaría un aspecto fundamental de flujo del juego.

2. Los excavadores deben tener un atributo que indiquen la cantidad de días descansadas y otro atributo que indica si es que está descansando o no para ejecutar el método de descansar.


-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://github.com/IIC2233/Syllabus/blob/bc087c1e66b7178ee1bb13ffd9da4b7de9659b5f/Tareas/T1/Sala%20Ayuda/Sala%20Ayuda%20-%20Probabilidades.ipynb: este hace que se cumplan las condiciones de probabilidad pedidas para un excavador encontrar un item, y está implementado en el archivo ```entidades.py``` en las líneas 94-123, y también en el archivo ```torneo.py``` en las líneas 220-293 y hace que ocurra un evento bajo la probabilidad correspondiente.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
