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

print("")
print("-----------------------")
print("Pizzería")
print("-----------------------")
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
    print(' 2. Salmón')
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