# Exercícios 

## 3.1
Suponha que eu forneça uma pilha de chamada como esta:

Sauda 2
Nome: Maggie
Sauda
Nome: Maggie

Quais informações você pode retirar baseando-se apenas nesta pilha de chamada?
Agora, vamos ver esta pilha de chamada sendo executada como uma função recursiva.

R:
Aqui estão algumas coisas que você poderia me dizer:
- A função sauda é chamada primeiro, com nome = maggie.
- Então a função sauda chama sauda2, com nome = maggie.
- Neste ponto, a função greet está em um estado incompleto e suspenso.
- A atual função de chamada é a função sauda2.
- Após esta função de chamada ser finalizada, a função sauda será retornada.


## 3.2
Suponha que você acidentalmente escreva uma função recursiva que fique executando infinitamente. 
Como você viu, seu computador aloca memória na pilha para cada chamada de função.
O que acontece com a pilha quando a função recursiva fica executando infinitamente?

R: A pilha cresce eternamente. Cada programa tem uma limitada quantidade de espaço na pilha de chamada. Quando o seu programa fica sem espaço 
(o que eventualmente acontece), ele é finalizado com um erro de overflow (estouro) da pilha.



