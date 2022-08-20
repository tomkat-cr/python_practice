# File: dict_comprehension.py
# CR | 2022-06-27

from math import sqrt

def run():
    my_dict = {num : sqrt(num) for num in range(1, 101)}
    print(my_dict)


if __name__ == '__main__':
    run()
