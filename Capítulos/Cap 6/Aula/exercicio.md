# Exercícios 

Execute o algoritmo de pesquisa em largura em cada um desses grafos para encontrar a solução.

## 6.1
Encontre o menor caminho do ínicio ao fim.

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/1.png" width="500">

R: O caminho mais curto tem comprimento de 2.

## 6.2
Encontre o menor caminho de "jato" até "gato".

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/2.png" width="500">

R: O caminho mais curto tem comprimento de 2.

Este é um pequeno grafo da minha rotina matinal.

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/3.png" width="500">

Ele mostra que não posso tomar café da manhã antes de escovar meus dentes. Então "tomar café da manhã" depende de "escovar os dentes".

Por outro lado, tomar banho não depende de escovar os dentes, pois posso tomar banho antes de escovar os dentes. A partir desse grafo
você pode fazer uma lista relacionando a ordem das atividades da minha rotina matinal.

- 1. Acordar.
- 2. Tomar banho.
- 3. Escovar os dentes.
- 4. Tomar café da manhã.

Note que "tomar banho" pode ser movido, logo essa lista também é válida:
- 1. Acordar.
- 2. Escovar os dentes.
- 3. Tomar banho.
- 4. Tomar café da manhã.

## 6.3

Quanto a estas três listas, marque se elas são válidas ou inválidas.

| A | B     | C                      |
| :---------- | :---------- | :---------- |
| 1. ACORDAR | 1. ACORDAR | 1. TOMAR BANHO |
| 2. TOMAR BANHO | 2. ESCOVAR OS DENTES | 2. ACORDAR |
| 3. TOMAR CAFÉ DA MANHÃ | 3. TOMAR CAFÉ DA MANHÃ | 3. ESCOVAR OS DENTES |
| 4. ESCOVAR OS DENTES | 4. TOMAR BANHO | 4. TOMAR CAFÉ DA MANHÃ |

R: A - Inválida; B - Válida; C - Inválida.

## 6.4
Aqui temos um grafo maior. Faça uma lista válida para ele.

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/4.png" width="500">


Você poderia dizer que essa lista é, de certa forma, ordenada. Se a tarefa A depende da tarefa B, a tarefa A aparece 
depois na lista. Isso é chamado de ordenação topológica, e é uma maneira de criar uma lista ordenada a partir de um grafo.
Imagine que você esteja planejando um casamento e tenha um grafo enorme de tarefas a serem realizadas.

Porém você não sabe nem por onde começar. Assim, uma ordenação topológica do grafo poderia ser feita e, dessa forma, uma lista
de tarefas já em ordem seria elaborada.

Suponha que você tenha uma árvore genealógica.

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/5.png" width="500">

Esta árvore é um grafo, pois existem vértices (as pessoas) e arestas, e as arestas apontam para os pais dos vértices.
Porém todas as arestas apontam para baixo, pois não faria sentido uma árvore genealógica ter arestas apontando
para cima! Seu pai não pode ser o pai do seu avô!

Isso é chamado de árvore. Uma árvore é um tipo especial de grafo em que nenhuma arestas jamais aponta de volta.


R: 1 - Acordar; 2 - Praticar exercício; 3 - Tomar banho; 4 - Escovar os dentes; 5 - Trocar de roupa; 6 - Embrulhar o lanche; 7 - Tomar café da manhã.


## 6.5
Quais desses grafos também são árvores?

<img src="https://github.com/karenyov/bookEntendendoAlgoritmos/blob/main/Cap%C3%ADtulos/Cap%206/img/6.png" width="500">

R: A - Árvore; B - Não é uma árvore; C - Árvore.
O último exemplo é uma árvore na lateral. Árvore são um subconjunto dos grafos. Assim, uma árvore sempre será um grafo, mas um grafo pode ou não ser uma árvore.


