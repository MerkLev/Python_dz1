
import math

X1 = int(input("Введите координату Х1: "))
Y1 = int(input("Введите координату y1: "))
X2 = int(input("Введите координату Х2: "))
Y2 = int(input("Введите координату y2: "))


Distance = (math.sqrt(((X2-X1))**2+((Y2-Y1))**2))
print('Расстояние = ', Distance)
