# File: list_comprehension_squares.py
# CR | 2022-06-26

def run():
    challenge_type = 1

    if challenge_type == 0:
        top_range = 12
        # multiple_of = None
        multiple_of = 3
        print('Method 0: with lambda')
        squares = get_squares(top_range, multiple_of, 0)
        print(squares)
        squares_as_tuple = get_squares_as_tuple(top_range, multiple_of, 0)
        print(squares_as_tuple)
        print('Method 1: with list comprehension')
        squares = get_squares(top_range, multiple_of, 1)
        print(squares)
        squares_as_tuple = get_squares_as_tuple(top_range, multiple_of, 1)
        print(squares_as_tuple)

    if challenge_type == 1:
        response = get_multiples_of_4_6_9()
        print(response)


def get_squares(top_range, multiple_of, method):
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    # We can calculate the list of squares without any side effects like creating (or overwriting)
    # a variable named x that still exists after the loop completes, by using `list comprehensions`,
    # that provides a concise way to create lists:

    if method == 0:
        squares = list(map(lambda x: x**2, range(1, top_range+1), ))
    elif method == 1:
        # or, equivalently:
        squares = [x**2 for x in range(1, top_range+1) if multiple_of == None or x % 3 != 0]
        # which is more concise and readable.

    return squares


def get_squares_as_tuple(top_range, multiple_of, method):
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    if method == 0:
        # squares = list(map(lambda x: x**2, range(top_range)))
        # numbers = list(map(lambda x: x, range(top_range)))
        squares = list(map(lambda x: (x, x**2), range(1, top_range+1)))
    elif method == 1:
        # squares = [x**2 for x in range(top_range)]
        # numbers = [x for x in range(top_range)]
        squares = [(x, x**2) for x in range(1, top_range+1) if multiple_of == None or x % 3 != 0]

    # return (numbers, squares)
    return squares


def get_multiples_of_4_6_9():
    return [x for x in range(1, 99999+1) if x % 4 == 0 and x % 6 == 0 and x % 9 == 0]


if __name__ == '__main__':
    run()
