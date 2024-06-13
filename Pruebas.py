print("")
print("----------")
print("Contraseña")
print("----------")
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

for ingresar_moneda in moneda:
  if ingresar_moneda == moneda:
    print(ingresar_moneda)
  else:
    print("Esta moneda no esta en la lista")