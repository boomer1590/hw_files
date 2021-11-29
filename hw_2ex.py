from pprint import pprint
import os

path_1 = os.path.join((os.getcwd()), 'first.txt')
path_2 = os.path.join((os.getcwd()), 'second.txt')
path_3 = os.path.join((os.getcwd()), 'third.txt')

with open(path_1, 'r') as file_1:
    count_1 = 0
    for count in file_1:
        count_1 += 1
    # print(count_1)
with open(path_1, 'r') as file_1:
    data_1 = file_1.read()
    # print(data_1)

with open(path_2, 'r') as file_2:
    count_2 = 0
    for count in file_2:
        count_2 += 1
    # print(count_2)
with open(path_2, 'r') as file_2:
    data_2 = file_2.read()
    # print(data_2)


with open(path_3, 'r') as file_3:
    count_3 = 0
    for count in file_3:
        count_3 += 1
    # print(count_3)
with open(path_3, 'r') as file_3:
    data_3 = file_3.read()
    # print(data_3)

with open('all_data.txt', 'w', encoding='utf-8') as f:
    if count_1 >= count_2 >= count_3:
        f.write(f'first.txt\n{count_3}\n{data_3}\n')
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
        f.write(f'third.txt\n{count_1}\n{data_1}\n')
    elif count_1 >= count_3 >= count_2:
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
        f.write(f'third.txt\n{count_3}\n{data_3}\n')
        f.write(f'first.txt\n{count_1}\n{data_1}\n')
    elif count_2 >= count_1 >= count_3:
        f.write(f'third.txt\n{count_3}\n{data_3}\n')
        f.write(f'first.txt\n{count_1}\n{data_1}\n')
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
    elif count_2 >= count_3 >= count_2:
        f.write(f'first.txt\n{count_1}\n{data_1}\n')
        f.write(f'third.txt\n{count_3}\n{data_3}\n')
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
    elif count_3 >= count_1 >= count_2:
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
        f.write(f'first.txt\n{count_1}\n{data_1}\n')
        f.write(f'third.txt\n{count_3}\n{data_3}\n')
    else:
        f.write(f'first.txt\n{count_1}\n{data_1}\n')
        f.write(f'second.txt\n{count_2}\n{data_2}\n')
        f.write(f'third.txt\n{count_3}\n{data_3}\n')



with open('all_data.txt', 'r', encoding='utf-8') as f:
    print(f.read())
