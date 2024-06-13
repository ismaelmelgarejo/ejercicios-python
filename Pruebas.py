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
