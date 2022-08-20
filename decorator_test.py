# decorator_test.py
# 2022-07-02 | CR

from decorator_execution_time import execution_time

@execution_time
def random_func():
    for _ in range(1, 10000000):
        # print('*', end="")
        pass

@execution_time
def suma(a: int, b:int) -> int:
    return a + b

random_func()

suma(5, 5)

