# Моё решение

# squares = {}
# for key in range(10):
#     item = {key: key ** 2}
#     squares.update(item)

# Решение при помощи "генератора словаря" по мотивам:
# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/vyrazhenie-slovar/

squares = {key: key**2 for key in range(10)}
print(squares)
