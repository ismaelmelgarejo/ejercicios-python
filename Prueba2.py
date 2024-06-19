import sys
import tty
import termios

def esperar_tecla():
  print('Presione cualquier tecla para continuar...')
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      sys.stdin.read(1)
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#5
print("")
print("-----------------------------")
print("|créditos de las asignaturas|")
print("-----------------------------")
print("")
print("Escribir un programa que almacene el diccionario con los créditos de las asignaturas")
print("de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después mues-")
print("tre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene")
print("<créditos> créditos, donde <asignatura> es cada una de las asignaturas del")
print("curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de")
print("créditos del curso.")
print("")
creditos = {
   'Matemáticas': 6,
   'Física': 4,
   'Química': 5
  }

esperar_tecla()
from os import system
system("clear")