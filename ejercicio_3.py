import math

print("*****Para calcular area del circulo ingrese radio*****\n")

r = float(input("Ingrese valor del radio: "))

area = round(math.pi * (r**2),2)

print(f"El area del circulo es {area}\n")

print("*****Para calcular el volumen de un cilindro agrega la altura****")

h = float(input("Ingrese altura: "))

volumen = round(area * h,2)

print(f"El volumen del cilindro es {volumen}")
