x = int(input("Введите значение X: ",))
y = int(input("Введите значение y: ",))

if (x > 0 and y > 0):
    print("Первая четверть.")
elif (x < 0 and y > 0):
    print(" Вторая четверть.")
elif (x < 0 and y < 0):
    print(" Третья четверть.")
elif (x > 0 and y < 0):
    print(" Четвертая четверть.")
