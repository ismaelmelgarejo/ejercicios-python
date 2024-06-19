# Solicitar al usuario que ingrese sus datos en una sola línea
entrada = input("Ingrese su nombre, edad y ciudad separados por /: ")

# Dividir la entrada en las variables correspondientes
nombre, edad, ciudad = entrada.split('/')

# Convertir la edad a un entero
edad = int(edad.strip())

# Mostrar los datos ingresados
print(f"Nombre: {nombre.strip()}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad.strip()}")
