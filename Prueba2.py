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

#4
print("")
print("------------------")
print("|Precio de frutas|")
print("------------------")
print("")
print("Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por")
print("pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre")
print("del mes.")
print("")
fruta = {
  'enero': 1,
  'febrero': 2,
  'marzo': 3,
  'abril': 4,
   'mayo': 5,
  'junio': 6,
   'julio': 7,
  'agosto': 8,
   'septiembre': 9,
  'octubre': 10,
   'Noviembre': 11,
  'diciembre': 12
}


esperar_tecla()
from os import system
system("clear")