import menu
import sys
import tty
import termios


#Pausar ejecucuion
def esperar_tecla():
  print('Presione cualquier tecla para continuar...')
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      sys.stdin.read(1)
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#Imprimir menu opciones
def mostrar_menu(opciones):
  print('Seleccione una opción:')
  for clave in sorted(opciones, key=int):
      print(f' {clave}) {opciones[clave][0]}')

#asigna la opcion ingresada a la variable a y si no esta en opciones vuelve a pedir
def leer_opcion(opciones):
  print('')
  while (a := input('Opción: ')) not in opciones:
      print('Opción incorrecta, vuelva a intentarlo.')
  return a

#Ejecuta la funcion asignada a la opcion ingresada
def ejecutar_opcion(opcion, opciones):
  opciones[opcion][1]()

#Se genera el menu llamando a la funcion mostrar_menu y se asigna el resultado
#de leer_opcion a la variable opcion
def generar_menu(opciones, opcion_salida):
  opcion = None 
  while opcion != opcion_salida:
      mostrar_menu(opciones)
      opcion = leer_opcion(opciones)
      ejecutar_opcion(opcion, opciones)
      print()

#Se definen las opciones del menu
def menu_principal():
  print('')
  print('Ejercicios De Variables')
  print('')
  opciones = { 
      '1': ('Mayor de edad?', accion1),
      '2': ('Contraseña', accion2),
      '3': ('divisor = 0', accion3),
      '4': ('Par o Impar', accion4),
      '5': ('Tributar', accion5),
      '6': ('Agrupar por nombre', accion6),
      '7': ('Renta Anual', accion7),
      '8': ('Evaluación de empleados', accion8),
      '9': ('Entrada por edad', accion9),
      '10': ('Pizzería', accion10),
      '11': ('Menu Anterior', accion11),
      '12': ('Salir', salir)
  }
  generar_menu(opciones, '12')

def accion1():
  from os import system
  system("clear")

  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion3():
  from os import system
  system("clear")

  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion4():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion5():
  from os import system
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion6():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion7():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion8():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion9():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")

  esperar_tecla()
  from os import system
  system("clear")

def accion10():
  from os import system
  system("clear")
  
  print("EL CODIGO VA AQUI")
  
  esperar_tecla()
  from os import system
  system("clear")

def accion11():
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