# try_except_finally_test.py
# 2022-07-01 | CR
# Ref: https://docs.python.org/3/tutorial/errors.html

import sys

MY_FILE = 'myfile.txt'

try:
    f = open(MY_FILE)
    s = f.readline()
    i = int(s.strip())
    print("Data read from '" + MY_FILE + "' was: " + str(i))
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
finally:
    # https://www.techiedelight.com/how-to-check-if-variable-is-defined-in-python/
    if 'f' in locals():
        if f:
            f.close()
    # Si se pone solito, y no consigue el archivo, da este error:
    # Exception has occurred: NameError
    # name 'f' is not defined
    #f.close()
