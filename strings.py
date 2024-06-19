import menu
import sys
import tty
import termios
import funciones
#Se definen las opciones del menu
def menu_principal():
  print('')
  print('Ejercicios De Strings')
  print('')
  opciones = { 
      '1': ('Multiplicar Nombre', accion1),
      '2': ('Nombre y Apellido', accion2),
      '3': ('Imprimir texto ingresado', accion3),
      '4': ('Extraer el prefijo y el sufijo', accion4),
      '5': ('Invertir palabras de una frase', accion5),
      '6': ('Menu Anterior', accion6),
      '7': ('Salir', salir)
  }
  funciones.generar_menu(opciones, '7')

def accion1():
  from os import system
  system("clear")
  print("")
  print("---------------------")
  print("Mulltiplica el Nombre")
  print("---------------------")
  print("Escribir un programa que pregunte el nombre del usuario en la consola y un      número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.")
  print("")
  nombre = input("Ingresa tu nombre: ")
  numero = int(input("Ingresa un numero: "))
  print("")
  print((nombre + "\n") * numero)
  esperar_tecla()
  from os import system
  system("clear")

def accion2():
  from os import system
  system("clear")
  print("")
  print("-----------------")
  print("Nombre y Apellido")
  print("-----------------")
  print("Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.")
  print("")
  nombre = input("Ingresa tu nombre completo: ")
  print("")
  print(nombre.lower())
  print(nombre.upper())
  print(nombre.title())
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion3():
  from os import system
  system("clear")
  print("")
  print("------------------------")
  print("Imprimir texto ingresado")
  print("------------------------")
  print("Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.")
  print("")
  nombre = input("Ingresa tu nombre: ")
  total_caracteres = len(nombre)
  print("")
  print(nombre.upper(), "tiene", total_caracteres, "letras")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion4():
  from os import system
  system("clear")
  print("")
  print("------------------------------")
  print("Extraer el prefijo y el sufijo")
  print("------------------------------")
  print("Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.")
  print("")
  telefono = input("Ingrege el numero telefono completo: ")
  print("El numero telefonico es: ", telefono[4:-3])
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion5():
  from os import system
  system("clear")
  print("")
  print("------------------------------")
  print("Invertir palabras de una frase")
  print("------------------------------")
  print("Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.")
  print("")
  oracion = input("Ingrese una oracion: ")
  palabras = oracion.split()
  cont_palabra = len(palabras)
  cont_palabra = int(cont_palabra)
  count = 1
  while count < (int(cont_palabra/2)+1):
      cambiar=palabras[cont_palabra-count]
      palabras[cont_palabra-count] = palabras[count-1]
      palabras[count-1]=cambiar
      count+= 1
  print("")
  print(palabras)
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion6():
  from os import system
  system("clear")
  menu.menu_principal()

def salir():
  print('Saliendo')
  exit()

#Primera ejecucion, llama a la funcion menu_principal
if __name__ == '__main__':
  menu_principal()