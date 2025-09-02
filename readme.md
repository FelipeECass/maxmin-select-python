## MaxMin Select - Divisão e Conquista
# Descrição do projeto
Este projeto implementa em Python o algoritmo MaxMin Select, que encontra simultaneamente o maior e o menor elemento de uma sequência de números, utilizando a abordagem de divisão e conquista.
A ideia principal é dividir o problema em partes menores, resolver cada parte e depois combinar os resultados:
Divide o array em duas metades.
Recursivamente encontra o mínimo e o máximo de cada metade.
Combina os resultados pegando o menor dos mínimos e o maior dos máximos.

# Como executar o projeto
1. Clone o repositório:
`git clone https://github.com/felipeECass/maxmin-select-python`
`cd maxmin-divide-conquer`
2. Execute o programa com:
`python3 main.py`
3. Saída esperada (para o exemplo do código):
Lista: [42, 7, 19, 73, -5, 0, 88, 23, 17]
Mínimo: -5
Máximo: 88