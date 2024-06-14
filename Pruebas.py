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

#1
print("")
print("----------------")
print("Consultar Moneda")
print("----------------")
print("")
print("Escribir un programa que guarde en una variable el diccionario {'Euro':'€',")
print("'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su")
print("bolo o un mensaje de aviso si la divisa no está en el diccionario.")
print("")
moneda = {
  'Euro': "€",
  'Dollar': '$',
  'Yen': '¥',
}
ingresar_moneda = input("Ingresar moneda para su consulta: ")

if ingresar_moneda.title() in moneda:
    print(moneda[ingresar_moneda.title()])
else:
    print("La divisa no está.")
esperar_tecla()
from os import system
system("clear")


#2
print("")
print("-----------------")
print("|Consultar Moneda|")
print("-----------------")
print("")
print("Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y")
print("lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>")
print("tiene <edad> años, vive en <dirección> y su número de teléfono es")
print("<teléfono>.")
nombre = input("cual es su Nombre? ")
edad= input("Cual es su Edad? ")
direccion = input("Cual es su Direccion? ")
telefono = input("Cual es su Telefono? ")
persona = {
  'nombre': nombre,
  'edad': edad,
  'direccion': direccion,
  'telefono': telefono
}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
esperar_tecla()
from os import system
system("clear")

#3
print("")
print("------------------")
print("|Precio de frutas|")
print("------------------")
print("")
print("Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,")
print("pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio")
print("de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un")
print("mensaje informando de ello.")
print("")
print(" --------------------")
print(" |**Fruta**|*Precio*|")
print(" --------------------")
print(" | Plátano |  1.35  |")
print(" --------------------")
print(" | Manzana |  0.80  |")
print(" --------------------")
print(" |  Pera   |  0.85  |")
print(" --------------------")
print(" | Naranja |  0.70  |")
print(" --------------------")
print("")
fruta = {
  'Platano': 1.35,
  'Manzana': 0.80,
  'Pera': 0.85,
  'Naranja': 0.70
}
print("")
ingresar_fruta = input("Que fruta desea? ").title()
print("")
ingresar_peso = float(input("Que cantidad necesita? en KG "))
print("")
if ingresar_fruta in fruta:
    print("Usted compro ",ingresar_peso,"KG de ",ingresar_fruta,"por ", fruta[ingresar_fruta] * ingresar_peso)
else:
    print("La fruta no está.")

esperar_tecla()
from os import system
system("clear")