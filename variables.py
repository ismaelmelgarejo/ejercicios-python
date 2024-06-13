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
      '1': ('Imprimir texto', accion1),
      '2': ('Formula ((a+b)/(c*d))^2', accion2),
      '3': ('Suma de enteros', accion3),
      '4': ('Indice de masa Corporal(IMC)', accion4),
      '5': ('Interés simple', accion5),
      '6': ('Juguetería', accion6),
      '7': ('Menu Anterior', accion7),
      '8': ('Salir', salir)
  }
  generar_menu(opciones, '8')

def accion1():
  from os import system
  system("clear")
  print("")
  print("------------------------")
  print("Imprimir texto ingresado")
  print("------------------------")
  print("Escribir un programa que almacene la cadena en una variable y luego muestre por pantalla el contenido de la variable.")
  print("")
  text = input("Ingresa un texto: ")
  print("El texto usando input: ", text)
  print("")
  esperar_tecla()
  from os import system
  system("clear")
  
def accion2():
  from os import system
  system("clear")
  print("")
  print("-----------------------")
  print("formula ((a+b)/(c*d))^2")
  print("-----------------------")
  print("Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((a+b)/(c*d))^2")
  print("")
  print("Ingresar los datos para 4 variables")
  print("")
  a= input("Ingresa el valor de a: ")
  b= input("Ingresa el valor de b: ")
  c= input("Ingresa el valor de c: ")
  d= input("Ingresa el valor de d: ")
  print("")
  a= int(a)
  b= int(b)
  c= int(c)
  d= int(d)
  resultado= ((a+b)/(c*d))**2
  print("El tipo de dato de a: ",type(a))
  print("El tipo de dato de b: ",type(b))
  print("El tipo de dato de c: ",type(c))
  print("El tipo de dato de d: ",type(d))
  print("")
  print("((a+b)/(c*d))^2 = ",resultado)
  esperar_tecla()
  from os import system
  system("clear")
  
def accion3():
  from os import system
  system("clear")
  print("")
  print("-------------------------")
  print("Suma de todos los enteros")
  print("-------------------------")
  print("Escribir un programa que lea un entero positivo,n introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hastan . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n + 1))/2")
  print("")
  n = input("Ingresar el numero n: ")
  n = int(n)
  print("")
  suma = (n*(n + 1))/2
  print("Resultado = ",suma)
  esperar_tecla()
  from os import system
  system("clear")

def accion4():
  from os import system
  system("clear")
  print("")
  print("----------------------------")
  print("Indice de masa Corporal(IMC)")
  print("----------------------------")
  print("Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase (Tu índice de masa corporal es <imc>) donde <imc> es el índice de masa corporal calculado redondeado con dos decimales")
  print("")
  pesoKG = input("Ingresa tu peso en kg: ")
  estaturaMTS = input("Ingresa tu estatura en Metros: ")
  pesoKG = int(pesoKG)
  estaturaMTS = float(estaturaMTS)
  print("")
  IMC = pesoKG / (estaturaMTS)**2
  print("Su IM es: %.2f" % IMC)
  esperar_tecla()
  from os import system
  system("clear")

def accion5():
  from os import system
  system("clear")
  print("")
  print("--------------")
  print("Interés simple")
  print("--------------")
  print("Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.")
  print("")
  print("Interés simple = Capital invertido x Tiempo x Tasa de interés")
  print("")
  monto = input("Cantidad a invertir: ")
  monto = int(monto)
  interes_inicial = input("Interés anual en %: ")
  interes_inicial = int(interes_inicial)
  interes_final = int(monto) * (int(interes_inicial) / 100)
  anhos = input("Cuantos años desea invertir? ")
  anhos = int(anhos)
  print("Capital obtenido en la inversión:", int(monto * anhos * interes_final))
  esperar_tecla()
  from os import system
  system("clear")

def accion6():
  from os import system
  system("clear")
  print("")
  print("----------")
  print("Juguetería")
  print("----------")
  print("Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.")
  print("")
  precio_payaso = input("Monto por peso de Payasos: ")
  precio_payaso = int(precio_payaso)
  precio_munheca = input("Monto por peso de Muñeca: ")
  precio_munheca = int(precio_munheca)
  print("")
  payaso = input("Cantidad de Payasos: ")
  payaso = int(payaso)
  munheca = input("Cantidad de Muñecas: ")
  munheca = int(munheca)
  print("")
  print("Peso de Payasos: ", (payaso * 112)/1000, "KG")
  print("Peso de Muñecas: ", (munheca * 75)/1000, "KG")
  print("")
  print("Peso de Payasos: ", (payaso * 112)*precio_payaso, "USD")
  print("Peso de Muñecas: ", (munheca * 75)*precio_munheca, "USD")
  esperar_tecla()
  from os import system
  system("clear")

def accion7():
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