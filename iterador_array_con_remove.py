# iterador_array_con_remove.py
# 2022-10-31 | CR
#
arr = [3, 3, 2, 2, 1, 1]
for item in arr:
    print(item)
    if item == 2:
        print("Remueve 2")
        arr.remove(item)
print(len(arr))
# R: 5
# porque al remover el 1er 2, el segundo se corre una posicion y el iterador sigue con el proximo 1.
