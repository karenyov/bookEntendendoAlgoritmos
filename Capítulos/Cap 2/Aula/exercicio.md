# Exercícios 

## 2.1
Suponha que você esteja criando um aplicativo para acompanhar as suas finanças.

- 1. Compras
- 2. Cinema
- 3. Mensalidade do SFBC

Todos os dias você escreve tudo o que gastou e onde. No final do mês, você revisa os seus gastos e resumo o quanto gastou.
Logo, você tem um monte de inserções e poucas leituras. Você deve usar um array ou uma lista para implementar esse aplicativo?

R: Neste caso, você está adicionando despesas na lista todos os dias e lendo todas as despesas uma vez por mês.
Arrays têm leitura rápida, mas inserção lenta. Listas encadeadas têm leituras lentas e rápidas inserções.
Como você inserirá mais vezes do que lerá, faz mais sentido usar uma lista encadeada. Além disso, listas encadeadas
têm leitura lenta  somente quando você acessa elementos da lista. Como estará lendo todos os elementos da lista, a lista encadeada terá
também uma boa velocidade de leitura. Portanto, uma lista encadeada é uma boa solução para este problema.


## 2.2
Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante.
Seu aplicativo precisa de uma lista de pedidos. Os garçons adicionam os pedidos a essa lista e os chefes
retiram os pedidos da lista.  Funciona como uma fila. Os garçons colocam os pedidos no final da fila e os chefes retiram os 
pedidos do começo dela para cozinhá-los.
Você utilizaria um array ou lista encadeada para implementar essa lista? (Dica: Listas encadeadas são boas para inserção/eliminações e arrays
são bons para acesso aleatório. O que vai fazer nesse caso?)

R: Uma lista encadeada. Muitas inserções estão ocorrendo (garçons adicionando ordens), sendo essa uma das vantagens
da lista encadeada. Você não precisa pesquisar ou ter acesso aleatório (nisso os arrays são bons), pois
o chef sempre pega a primeira ordem da fila

## 2.3
Vamos analisar um experimento. Imagine que o Facebook guarde uma lista de usuários. Quando alguém tenta acessar o Facebook, uma busca é feita pelo nome de usuário.
Se o nome da pessoa está na lista, ela pode continuar o acesso. As pessoas acessam o Facebook com muita frequência, então existem muitas buscas nessa lista.
Presuma que o Facebook use a pesquisa binária para procurar um nome na lista. A pesquisa binária precisa de acesso aleatório - você
precisa ser capaz de acessar o meio da lista de nomes instanttaneamente. Sabendo disso, você implementaria essa lista como array ou uma lista encadeada?

R: Um array ordenado. Arrays fornecem acesso aleatório, então voc6e pode pegar um elemento do meio do array instantaneamente. Isso não é possível
com listas encadeadas. Para acessar o elemento central de uma lista encadeada, você deve iniciar com o primeiro elemento e seguir por todos os links até o elemento central.

## 2.4
As pessoas se inscrevem no Facebook com muita frequência também. Suponha que você decida usar um array para armazenar a lista de usuários.
Quais as desvantagens de um array em relação ãs inserções? Em particular, imagine que você esteja usando a pesquisa binária para buscar os logins. O que acontece quando você adiciona novos usuários em um array?

R: Inserções em arrays são lentas. Além, se você estiver utilizando a pesquisa binária para procurar os nomes de
usuário, o array precisará estar ordenado. Suponha que alguém chamado Adit B se registre no Facebook. O nome dele será inserido no final do array. Assim, você  precisa ordenar o array
cada vez que um nome for inserido!


## 2.5
Na verdade, o Facebook não usa nem arrays nem listas encadeadas para armazenar informações. Vamos considerar uma estrutura de dados híbrida: um 
array de listas encadeadas. Voc6e tem um array com 26 slots. Cada slot do array aponta para uma lista encadeada. Por exemplo, o primeiro slot do array aponta para uma lista encadeada que contém todos os usuários que 
começam com a letra A. O segundo slot aponta para a lista encadeada que contém todos os usuários que começam com a letra A. 
O segundo slot aponta para a lista encadeada que contém todos os usuários que começam com a letra B, e assim por diante.
Suponha que o Adit B se inscreva no Facebook e você queira adicioná-lo ã lista. Você vai ao slot 1 do array, a seguir para a lista encadeada do slot 1, e adiciona Adit B no final. 
Agora, suponha que você queira procurar
o Zakhir H. Você vai ao slot 26, que aponta para a lista encadeada de todos os nomes começados em Z. Então, procura a lista até encontrar o Zakhir H.

Compare esta estrutura híbrida com arrays e listas encadeadas.
É mais lento ou mais rápido fazer inserções e eliminações nesse caso? Você nào precisa responder dando o tempo de execução Big(O),
apenas diga se a nova estrutura de dados é mais rápida ou mais lenta do que os arrays e as listas encadeadas.

R: Para buscas - mais lenta do que arrays, masi rápida do que listas encadeadas. Para inserções  - mais rápida do que arrays, mesmo tempo que as listas encadeadas. 
Portanto é mais lenta para buscas que os arrays, porém mais rápida ou igual das listas encadeadas para tudo. Falaremos sobre outra estrutura de dados híbridos chamada tabela hash depois.
Isto deve dar uma ideia sobre como é possível construir estruturas de dadis mais complexas a partir das estreuturas mais simples.
Então, o que o Facebook realmente utiliza? Provavelmente uma dúzia de diferentes bancos de dados com diferentes estruturas por trás deles,
como tabela hash, árvores B e outras. os arrayse as listas encadeadas são os blocos fundamentais para estruturas de dados mais complexas.





