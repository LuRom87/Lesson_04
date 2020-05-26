from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el, end='')
    quit = input()
    if quit == 'z':
        break


from itertools import cycle

my_list = input('Введите список: ').split()
new_list = cycle(my_list)
quit = None


while quit != 'q':
    print(next(new_list), end='')
    quit = input()