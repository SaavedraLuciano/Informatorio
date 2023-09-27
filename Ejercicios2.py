anio_de_nacimiento=int(input('Ingrese su ano de nacimiento: '))
anio_actual= 2023
edad= anio_actual - anio_de_nacimiento
print('Su edad actual es: ', edad, 'o', (edad-1))

nombre= input('Coloque su nombre: ')
print(nombre)
edad_usuario= int(input('Coloque su edad actual: '))
edad_futura= edad_usuario + 10
print('La edad del usuario dentro de 10 anos sera de: ', edad_futura)

numero_solicitado= int(input('Coloque un numero entero: '))
doble= numero_solicitado * 2
triple= numero_solicitado * 3
print('El doble del numero es: ', doble)
print('EL triple del numero es: ', triple)

temperatura_celcius= int(input('Indique cuantos grados celcius quiere convertir: '))
convertira_f= (temperatura_celcius * 1.8) + 32
print('La temperatura en grados celcius equivale a ', convertira_f, 'grados fahrenheit')

altura_usuario= float(input('Ingrese su altura en metros: '))
peso_usuario= float(input('Ingrese su peso en kilogramos: '))
IMC= peso_usuario//altura_usuario**2
print('EL IMC del usuario es: ',IMC)

palabra1= input('Coloque la primer palabra: ')
palabra2= input('Coloque la segunda palabra: ')
print(palabra2, palabra1)

numero_decimal=float(input('Defina el numero decimal: '))
