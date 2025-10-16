a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a == b:
    print("Числа равны.")
else:
    min_value = a if a < b else b
    print("Наименьшее число:", min_value)
