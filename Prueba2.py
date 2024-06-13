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

#3
print("")
print("------------------")
print("|Consultar Moneda|")
print("------------------")
print("")
print("Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,")
print("pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio")
print("de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un")
print("mensaje informando de ello.")
print("")
print("   Fruta   Precio")
print("  ---------------")
print("  Plátano   1.35")
print("  ---------------")
print("  Manzana   0.80")
print("  ---------------")
print("   Pera	   0.85")
print("  ---------------")
print("  Naranja   0.70")
print("")

esperar_tecla()
from os import system
system("clear")