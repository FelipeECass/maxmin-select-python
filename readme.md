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

## Relatório Técnico

- **Recorrência do número de comparações:**  
  \(C(1)=0,\; C(2)=1,\; C(n)=C(\lfloor n/2\rfloor)+C(\lceil n/2\rceil)+2\).

- **Caso \(n=2^k\):**  
  \(C(n)=\tfrac{3n}{2}-2\).

- **Limites gerais:**  
  \(n \leq C(n) \leq 2n-2 \;\;\Rightarrow\;\; C(n)=\Theta(n)\).

- **Teorema Mestre:**  
  \(T(n)=2T(n/2)+O(1)\) → \(a=2,\; b=2,\; f(n)=O(1)\).  
  Logo, \(T(n)=\Theta(n)\).

- **Complexidade final:**  
  O algoritmo executa em **tempo linear** \(O(n)\).

- **Observação prática:**  
  O método *pairwise* também encontra min e max em \(3n/2-2\) comparações no pior caso (ótimo).  
  O algoritmo divide-e-conquista coincide com isso quando \(n\) é potência de 2, mas pode usar um pouco mais para outros valores de \(n\).

## Trablho Anterior
Por favor, considerar a entrega da primeira atividade para esse repositório: https://github.com/FelipeECass/karatsuba-python-fpa
Pedido feito pelo professor durante a aula a citação da primeira atividade que foi entregue um dia depois, conforme enviado via canvas ao professor. Agradeço a compreensão
