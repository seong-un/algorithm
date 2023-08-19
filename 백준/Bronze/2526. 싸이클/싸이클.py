N, P = map(int, input().split())

object = N
list_object = []
while True:
    object = (object * N) % P
    if object not in list_object:
        list_object.append(object)
    else:
        print(len(list_object) - list_object.index(object))
        break