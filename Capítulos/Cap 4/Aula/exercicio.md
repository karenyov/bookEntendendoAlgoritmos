# Exercícios 

## 4.1
Escreva o código para a função soma, vista anteriormente.

```sh
def soma(lista):

    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])


print(soma([1,2,4])) # 6
```
    
## 4.2
Escreva ma função recursiva que conte o número de itens em uma lista.

```sh
def cont(lista):

    if lista == []:
        return 0
    return 1 + cont(lista[1:])


print(cont([2,3,4])) # 3
```

## 4.3
Encontre o valor mais alto em uma lista/

```sh
def maximo(lista):

    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]

    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maximo([1,2,4]))
```

## 4.4
Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo do tipo dividir para conqistar.
Você consegue determinar o caso-base e o caso recursivo para a pesquisa binária?

R: O caso-base para a pesquisa binária é um array com um item.
Se o item que você está procurando combina com o item presente no array, você o encontrou!
Caso contrário, ele não está no array.


Quanto tempo levaria, em notação Big O, para completar cada uma destas operações?

## 4.5
Imprimir o valor de cada elemento em um array.
R: O(n)

## 4.6
Duplicar o valor de cada elemento em um array.
R: O(n)

## 4.7
Duplicar o valor apenas do primeiro elemento do array.
R: O(1)

## 4.8
Criar uma tabela de manipulação com todos os elementos do array. Assim, caso o seu array seja [2, 3, 7, 8, 10],
você primeiro multiplicará cada elemento por 2. Depois, multiplicará cada elemento por 3 e então por 7, e assim por diante.
R: O(n^2)









