from partida import Partida
from jugador import Jugador
from pregunta import Pregunta
from respuesta import Respuesta
from modo import Modo

# Creación de una pregunta y sus respuestas
p1 = Pregunta(1,'¿Es verano?')
r1 = Respuesta(1,'Si',False)
r2 = Respuesta(2,'No',True)

p1.respuestas = [r1,r2]
col_preguntas = [p1]
# creacion de Jugador
j = Jugador('Fer')

# Modo de juego
m = Modo()

#Creacion de la partida
mi_partida = Partida(j,m,col_preguntas)

# Iniciar Partida
mi_partida.iniciar()