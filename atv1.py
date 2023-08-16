'''
Exercícios sobre os comandos básicos em python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo Delgado Preti')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q02():
    print('30 27')
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q03():
    print(5+8+12/3)
#4. Faça um programa que leia e imprima um número inteiro.
def q04():
    num1 = int(input('Digite um número: '))
    print(f'O número escolhido foi: {num1}')

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(f'O valor do primeiro número foi: {num1}, o valor do número foi: {num2} ')
#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    num1 = int(input('Qual o número desejado para a operação?: '))
    print(f'O sucessor de {num1} é {num1+1}')
    print(f'O antecessor de {num1} é {num1-1}')
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q07():
    nome = str(input('Digite seu nome completo: '))
    endereço = str(input('Digite o endereço da sua residência: '))
    telefone = str(input('Digite seu número de telefone completo: '))
    print(f'Os dados fornecidos foram \n{nome}\n{endereço}\n{telefone}')
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
    num1 = int(input('Digite O primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print(f'O resultado da subtração dos valores foi: {num1-num2}')

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    num1 = float(input(f'Digite o valor desejado: '))
    print(f'O valor final foi de: {num1/4}')
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

q08()