e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
# Новое в Python 3.8
# reversed(e2f)

# Решение Любановича
# f2e = {}
# for english, french in e2f.items():
#     f2e[french] = english

# В одну строку по мотивам
# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/obratnyj-porjadok-revers-slovarja/
f2e = {fr: en for en, fr in e2f.items()}

print(f2e)
