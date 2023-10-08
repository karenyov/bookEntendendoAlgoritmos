def cont(lista):

    if lista == []:
        return 0
    return 1 + cont(lista[1:])


print(cont([2,3,4]))


