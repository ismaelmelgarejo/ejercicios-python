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
  print("")
  print("--------------")
  print("Mayor de edad?")
  print("--------------")
  print("")
  print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es")
  print("mayor de edad o no.")
  print("")
  edad = input("Ingrese su edad: ")
  if int(edad) >= 18:
    print("Usted es mayor de edad")
  else:
    print("Usted es menor de edad")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion2():
  from os import system
  system("clear")
  print("")
  print("----------")
  print("Contraseña")
  print("----------")
  print("")
  print("Escribir un programa que almacene la cadena de caracteres contraseña en una")
  print("variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña")
  print("troducida por el usuario coincide con la guardada en la variable sin tener en cuenta")
  print("mayúsculas y minúsculas.")
  print("")
  contrasenha_ingresada = input("Ingrese su contraseña para verificar: ")
  contrasenha_ingresada = contrasenha_ingresada.lower()
  contrasenha_guardada= "Hola que tal"
  contrasenha_guardada = contrasenha_guardada.lower()
  print("")
  if contrasenha_guardada == contrasenha_ingresada:
    print("La contraseña es correcta")
  else:
    print("La contraseña no es correcta")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion3():
  from os import system
  system("clear")
  print("")
  print("-----------")
  print("divisor = 0")
  print("-----------")
  print("")
  print("Escribir un programa que pida al usuario dos números y muestre por pantalla su")
  print("división. Si el divisor es cero el programa debe mostrar un error.")
  print("")
  dividendo = input("Ingresa el dividendo: ")
  dividendo = int(dividendo)
  divisor = input("Ingresa el divisor: ")
  divisor = int(divisor)
  print("")
  if divisor == 0:
      print("Error, el divisor des 0")
  else:
      print("El dividendo esta sin error")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion4():
  from os import system
  system("clear")
  print("")
  print("-----------")
  print("Par o Impar")
  print("-----------")
  print("")
  print("Escribir un programa que pida al usuario un número entero y muestre por pantalla si es")
  print("par o impar.")
  print("")
  numero = input("Ingresar un numero: ")
  numero= int(numero)
  modulo = numero % 2
  print("")
  if modulo == 0:
      print("El numero es par")
  else:
      print("El numero es impar")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion5():
  from os import system
  system("clear")
  print("")
  print("--------")
  print("Tributar")
  print("--------")
  print("")
  print("Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos")
  print("ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al")
  print("usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que")
  print("tributar o no.")
  print("")
  edad = input("Edad: ")
  ingreso = input("Ingreso: ")
  print("")
  if (int(edad) > 16) and (int(ingreso) > 1000):
      print("Puede Tributar")
  else:
      print("No puede Tributar")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion6():
  from os import system
  system("clear")
  print("")
  print("------------------")
  print("Agrupar por nombre")
  print("------------------")
  print("")
  print("Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el")
  print("nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los")
  print("hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa")
  print("que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le")
  print("corresponde.")
  print("")
  nombre=input("Ingresa el nombre: ")
  sexo=input("Ingresa el sexo F o M: ")
  if ((nombre[0] > "m") and (sexo == "F")) or ((nombre[0] > "m") and (sexo == "M")):
      print("Grupo A")
  else:
      print("Grupo B")
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion7():
  from os import system
  system("clear")
  print("")
  print("-----------")
  print("Renta Anual")
  print("-----------")
  print("")
  print("Los tramos impositivos para la declaración de la renta en un determinado país son los")
  print("siguientes:")
  print("")
  print("        Renta            Tipo impositivo")
  print("----------------------------------------")
  print("   Menos de 10000€	     5%")
  print("----------------------------------------")
  print("Entre 10000€ y 20000€       15%")
  print("----------------------------------------")
  print("Entre 20000€ y 35000€	    20%")
  print("----------------------------------------")
  print("Entre 35000€ y 60000€	    30%")
  print("----------------------------------------")
  print("    Más de 60000€	    45%")
  print("")
  print("Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el")
  print("tipo impositivo que le corresponde.")
  print("")
  ingreso = input("Cual es su renta anual?: ")
  ingreso = int(ingreso)
  print("")
  if ingreso < 10000:
    print('Tu tipo impositivo es: 5%')
  elif (ingreso >= 10000) and (ingreso <= 20000):
      print('Tu tipo impositivo es: 15%')
  elif (ingreso > 20000) and (ingreso <= 35000):
      print('Tu tipo impositivo es: 20%')
  elif (ingreso > 35000) and (ingreso <= 60000):
      print('Tu tipo impositivo es: 35%')
  elif ingreso > 60000:
      print('Tu tipo impositivo es: 45%')
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion8():
  from os import system
  system("clear")
  print("")
  print("-----------------------")
  print("Evaluación de empleados")
  print("-----------------------")
  print("")
  print("En una determinada empresa, sus empleados son evaluados al final de cada año. Los")
  print("puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir")
  print("aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los")
  print("empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras")
  print("mencionadas. A continuación se muestra una tabla con los niveles correspondientes a")
  print("cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€")
  print("multiplicada por la puntuación del nivel.")
  print("")
  print("   Nivel	Puntuación")
  print("--------------------------")
  print("Inaceptable	   0.0")
  print("--------------------------")
  print(" Aceptable	   0.4")
  print("--------------------------")
  print(" Meritorio       0.6 o más")
  print("")
  print("Escribir un programa que lea la puntuación del usuario e indique su nivel de")
  print("rendimiento, así como la cantidad de dinero que recibirá el usuario.")
  print("")
  puntuacion = input("Cual es su puntuacion?: ")
  puntuacion=float(puntuacion)
  inaceptable=0.0
  aceptable=0.4
  meritorio=0.6
  if puntuacion == inaceptable:
      print('Su nivel de rendimiento es de 0.0 y es Inaceptable')
      print('El dinero que recibirá es: ',2400 * puntuacion)
  elif puntuacion == aceptable:
      print('Su nivel de rendimiento es de 0.4 y es Aceptable')
      print('El dinero que recibirá es: ',2400 * puntuacion)
  elif puntuacion >= meritorio:
      print('Su nivel de rendimiento es 0.6 o mas y es Meritorio')
      print('El dinero que recibirá es: ',2400 * puntuacion)
  elif puntuacion != inaceptable:
      print('Este monto no es correcto')
  esperar_tecla()
  from os import system
  system("clear")

def accion9():
  from os import system
  system("clear")
  print("")
  print("----------------")
  print("Entrada por edad")
  print("----------------")
  print("")
  print("Escribir un programa para una empresa que tiene salas de juegos para todas las")
  print("edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por")
  print("entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de")
  print("la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18")
  print("años debe pagar 5€ y si es mayor de 18 años, 10€.")
  print("")
  edad = input("Cual es tu edad?: ")
  edad = int(edad)
  print("")
  if edad < 4:
      print('Tu juegas gratis')
  elif (edad >= 4) and (edad < 18):
      print('Tu juegas por 5€')
  elif (edad >= 18):
      print('Tu juegas por 10€')
  print("")
  esperar_tecla()
  from os import system
  system("clear")

def accion10():
  from os import system
  system("clear")
  print("")
  print("--------")
  print("Pizzería")
  print("--------")
  print("")
  print("La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los")
  print("ingredientes para cada tipo de pizza aparecen a continuación.")
  print("")
  print(" * Ingredientes vegetarianos: Pimiento y tofu.")
  print(" * Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
  print("")
  print("Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en")
  print("función de su respuesta le muestre un menú con los ingredientes disponibles para que")
  print("elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están")
  print("en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegeta")
  print("riana o no y todos los ingredientes que lleva.")
  print("")
  print("Bienvenida a la pizzería Bella Napoli")
  print("")
  print("Tenemos estos dos tipos de Pizzas")
  print("")
  print("  1. Vegetariana")
  print("  2. No Vegetariana")
  print("")
  pizzas = input("Que opcion prefiere: ")
  pizzas = int(pizzas)
  if (pizzas == 1):
      print("")
      print('Genial! Estos son los ingredientes Vegetarianos')
      print("")
      print('Puedes elejir uno de estos ingredientes:')
      print("")
      print(' 1. Pimiento')
      print(' 2. Tofu')
      print("")
      ingrediente = input("Ingrediente deseado: ")
      ingrediente = int(ingrediente)
      if ingrediente == 1:
          print('La pizza tiene los siguiente ingredientes')
          print('  Mozzarella')
          print('  Tomate')
          print('  Pimiento')
      elif ingrediente == 2:
          print('La pizza tiene los siguiente ingredientes')
          print('  Mozzarella')
          print('  Tomate')
          print('  Tofu')
      else:
          print('la opcion es incorrecta')
  elif (pizzas == 2):
      print("")
      print('Genial! Estos son los ingredientes no Vegetarianos')
      print("")
      print('Puedes elejir uno de estos ingredientes:')
      print("")
      print(' 1. Peperoni')
      print(' 2. Jamón')
      print(' 3. Salmón')
      print("")
      ingrediente = input("Ingrediente deseado: ")
      ingrediente = int(ingrediente)
      if ingrediente == 1:
          print('La pizza tiene los siguiente ingredientes')
          print('  Mozzarella')
          print('  Tomate')
          print('  Peperoni')
      elif ingrediente == 2:
          print('La pizza tiene los siguiente ingredientes')
          print('  Mozzarella')
          print('  Tomate')
          print('  Jamón')
      elif ingrediente == 3:
          print('La pizza tiene los siguiente ingredientes')
          print('  Mozzarella')
          print('  Tomate')
          print('  Salmón')
      else:
          print('la opcion es incorrecta')
  else:
      print('la opcion es incorrecta')
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