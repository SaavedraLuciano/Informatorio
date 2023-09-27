nombre=input('Escriba su nombre: ')
print(nombre)
print('Hola ' + nombre + ' Bienvenido')
edad= input('Coloque su edad: ')
print(edad)

num1=0
num2=0
suma=0

print('Ingrese numero entero:')
num1=int(input())
print('Ingrese otro numero entero:')
num2=int(input())
suma=num1+num2
print('El resultado de la suma es:', suma)

import math
print('Coloque valor del radio: ')
r = float(input())
areacirculo= math.pi * (r * r)
print('El valor del area es:', areacirculo)

print('Coloque el valor de la base: ')
base=float(input())
print('Coloque el valor de la altura: ')
altura=float(input())
areatriangulo= (base * altura) // 2
print ('El valor del area es: ', areatriangulo)

print('Coloque el valor del radio del circulo: ')
r2 = float(input())
diametro= r2 * 2
circunferencia= (2 * math.pi) * r2
area= math.pi * (r2 * r2)
print('El valor del diametro es: ', diametro)
print('El valor de la circunferencia es: ', circunferencia)
print('El valor del area es: ', area)

print('Ingrese numero entero:')
num3=int(input())
print('Ingrese otro numero entero:')
num4=int(input())
suma=num3+num4
resta=num3-num4
multiplicacion=num3 * num4
division= num3//num4
print('El resultado de la suma es:', suma)
print('El resultado de la resta es:', resta)
print('El resultado de la multiplicacion es:', multiplicacion)
print('El resultado de la division es: ', division)

print('Ingrese los dolares a cambiar:')
dolar = float(input())
cambioaeuro = dolar * 0.84
print('El valor en euros de la cantidad de dolares ingresados es: ', cambioaeuro)