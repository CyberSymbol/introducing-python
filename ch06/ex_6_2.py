guess_me = 7
number = 1
while number <= guess_me:
    if number == guess_me:
        print('foud it!')
        number += 1
        continue
    print('too low')
    number += 1
else:
    print('oops')
