# Exercícios 

## 1.1
Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária.
Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

- 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

R: 7 etapas.


## 1.2
Suponha que você deplique o tamanho da lista. Qual seria o número máximo de etapas agora?

R: 8


## 1.3
Você tem um nome e deseja encontrar o número de telefone para esse nome na agenda telefônica.
R:O(log n)


## 1.4
Você tem o número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: deve procurar pela agenda inteira!)
R:O(n)


## 1.5
Você quer ler o número de cada pessoa da agenda telefônica.
R:O(n)

## 1.6                                                      
Você quer ler o número de apenas dos novos que começam com A. (Isso é complicado! Esse algoritmo envolve conceitos que são abordados mais aprofundamente no Capítulo 4. Leia a resposta - você ficará surpreso )
R:O(n)
Você pode pensar: "Só estou fazendo isso para 1 dentre 26 caracteres, portanto o tempo de execução deve ser O(n/26)". 
Uma regra simples é a de ignorar números que são somadados, subtraídos, multiplicados ou divididos. Nenhum desses são tempos de execução Big O: O(n +26), O(n -26), O(n / 26).
Eles são todos o mesmo que O(n)! Por quê? Se você está com dúvidas, vá para "Notação Big O revisada",
no Capítulo 4, e leia a parte sobre constantes na notação Big O (uma constante é apenas um número; 26 era a constante desta questão).
