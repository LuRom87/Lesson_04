
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num - 1] < my_list[num]]
print(f'Первый список {my_list}')
print(f'Второй список {my_new_list}')