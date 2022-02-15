# Упражнение 110. Порядок сортировки
# (Решено. 22 строки)
# Напишите программу, которая будет запрашивать у пользователя цело-
# численные значения и сохранять их в виде списка. Индикатором окончания
# ния ввода значений должен служить ноль. Затем программа должна вы-
# вести на экран все введенные пользователем числа (кроме нуля) в порядке
# возрастания – по одному значению в строке. Используйте для сортировки
# либо метод sort, либо функцию sorted.
# Упражнение 111. Обратный порядок
# (20 строк)

# Напишите программу, которая, как и в предыдущем случае, будет за-
# прашивать у пользователя целые числа и сохранять их в виде списка.
# Индикатором окончания ввода значений также должен служить ноль. На
# этот раз необходимо вывести на экран введенные значения в порядке
# убывания.

numbers = []
while True:
    number = input("Введите целое положительное число "
                   "(0 для окончания ввода): ")
    if not number.isdigit():
        print("Ошибка ввода!")
        continue
    if int(number) == 0:
        print("Введенные числа в порядке убывания:")
        break
    numbers.append(int(number))
    print("Ещё!")

numbers.sort(reverse=True)
for number in numbers:
    print(number)
