guess_me = 5
number = 1
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('foud it!')
    else:
        print('oops')
        break
