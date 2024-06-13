import variables
import strings
import condicionales
import diccionarios

#Imprimir menu opciones
def mostrar_menu(opciones):
  print('')
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
  print('Ejercicios Del Curso de Fundamentos de Python')
  opciones = { 
      '1': ('Ejercicios de Variables', accion1),
      '2': ('Ejercicios de Strings', accion2),
      '3': ('Ejercicios de Condicionales', accion3),
      '4': ('Ejercicios de Diccionarios', accion4),
      '5': ('Opción 5', accion5),
      '6': ('Opción 6', accion6),
      '7': ('Opción 7', accion7),
      '8': ('Opción 8', accion8),
      '9': ('Opción 9', accion9),
      '10': ('Opción 10', accion10),
      '11': ('Salir', salir)
  }
  generar_menu(opciones, '11')

def accion1():
  variables.menu_principal()

def accion2():
  strings.menu_principal()

def accion3():
  condicionales.menu_principal()

def accion4():
  diccionarios.menu_principal()

def accion5():
  print('Has elegido la opción 5')

def accion6():
  print('Has elegido la opción 6')

def accion7():
  print('Has elegido la opción 7')

def accion8():
  print('Has elegido la opción 8')

def accion9():
  print('Has elegido la opción 9')

def accion10():
  print('Has elegido la opción 10')

def salir():
  print('Saliendo')
  exit()

#Primera ejecucion, llama a la funcion menu_principal
if __name__ == '__main__':
  menu_principal()