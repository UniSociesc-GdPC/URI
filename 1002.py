#1002 - Área do Círculo
import math

raio=float(input())
n = 3.14159
area = n*(math.pow(raio, 2))
print("A=",end="")
print(format(area, '.4f'))