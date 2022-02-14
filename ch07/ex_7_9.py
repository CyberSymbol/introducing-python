# 7.9. Напишите последний элемент списка surprise со строчной буквы, затем вы-
# ведите эту строку в обратном порядке и с прописной буквы.

surprize = ['Groucho', 'Chico', 'Harpo']
last_name = surprize[-1].lower()
revers_last_name = "".join(reversed(last_name))
print(revers_last_name.capitalize())

for i in surprize:
    print(i)
