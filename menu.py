import variables
import strings
import condicionales
import diccionarios
import funciones


#Se definen las opciones del menu
def menu_principal():
  print('')
  print('Ejercicios Del Curso de Fundamentos de Python')
  opciones = { 
      '1': ('Ejercicios de Variables', accion1),
      '2': ('Ejercicios de Strings', accion2),
      '3': ('Ejercicios de Condicionales', accion3),
      '4': ('Ejercicios de Diccionarios', accion4),
      '5': ('Salir', salir)
  }
  funciones.generar_menu(opciones, '5')

def accion1():
  from os import system
  system("clear")
  variables.menu_principal()

def accion2():
  from os import system
  system("clear")
  strings.menu_principal()

def accion3():
  from os import system
  system("clear")
  condicionales.menu_principal()

def accion4():
  from os import system
  system("clear")
  diccionarios.menu_principal()

def salir():
  print('Saliendo')
  exit()

#Primera ejecucion, llama a la funcion menu_principal
if __name__ == '__main__':
  menu_principal()