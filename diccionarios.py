import menu
import sys
import tty
import termios
import funciones
#Se definen las opciones del menu
def menu_principal():
  print('')
  print('Ejercicios De Diccionarios')
  print('')
  opciones = { 
      '1': ('Consultar Moneda', accion1),
      '2': ('Datos personales', accion2),
      '3': ('Precio de frutas', accion3),
      '4': ('Fechas', accion4),
      '5': ('Menu Anterior', accion5),
      '6': ('Salir', salir)
  }
  funciones.generar_menu(opciones, '6')

def accion1():
  from os import system
  system("clear")
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

def accion2():
  from os import system
  system("clear")
  print("")
  print("------------------")
  print("|Datos personales|")
  print("------------------")
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
  

def accion3():
  from os import system
  system("clear")
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

def accion4():
  from os import system
  system("clear")
  print("")
  print("--------")
  print("|Fechas|")
  print("--------")
  print("")
  print("Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por")
  print("pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre")
  print("del mes.")
  print("")
  entrada = input("Ingrese la fecha en formato dd/m/aaaa separados por /: ")
  print("")
  dia, mes, anho = entrada.split('/')# Dividir la entrada en las variables correspondientes
  mes = int(mes.strip())
  meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'agosto',
    10: 'octubre',
    11: 'Noviembre',
    12: 'diciembre'
  }
  if mes in meses:
      print(dia,"/",meses[mes],"/", anho)
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion5():
  esperar_tecla()
  from os import system
  system("clear")
  menu.menu_principal()

def salir():
  print('Saliendo')
  exit()

#Primera ejecucion, llama a la funcion menu_principal
if __name__ == '__main__':
  menu_principal()