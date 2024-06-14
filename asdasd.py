frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
ingresar_fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if ingresar_fruta in frutas:
    print(kg, 'kilos de', ingresar_fruta, 'valen', frutas[ingresar_fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", ingresar_fruta, "no está disponible.")