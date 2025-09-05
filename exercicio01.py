"""Listagem 1"""

def ex01():

    """Faça um programa que mostre a mensagem "Alô mundo" na tela."""
    print("Alô mundo")

def ex02():

    """Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]."""

    print("Digite um número: ")
    input_num = input()
    print(f"O número informado foi: {input_num}")

def ex03():

    """Faça um Programa que peça dois números e imprima a soma."""
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    soma = num1 + num2
    print(f"A soma dos dois números é: {soma}")

def ex04():
    """Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média das notas é: {media}")

def ex05():
    """Faça um programa que converta metros para centímetros."""
    metros = float(input("Digite o valor em metros: "))
    centimetros = metros * 100
    print(f"O valor em centímetros é: {centimetros} cm")

def ex06():
    """Faça um Programa que peça o raio de um círculo, calcule e mostre sua área e perímetro."""
    import math
    raio = float(input("Digite o valor do raio do círculo: "))
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio
    print(f"A área do círculo é: {area}")
    print(f"O perímetro do círculo é: {perimetro}")

def ex07():
    """Faça um Programa que peça a altura e calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""
   
    altura = float(input("Digite a altura do quadrado: "))
    area = altura * altura
    dobro_area = area * 2
    print(f"O dobro da área do quadrado é: {dobro_area}")   

def ex08():
    """Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

    valor_hora = int(input("Digite quanto você ganha por hora: "))
    horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
    salario = valor_hora * horas_trabalhadas
    print(f"O total do seu salário no mês é: R$ {salario}")

def ex09():
    """Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)."""
    temperatura_f = float(input("Digite a temperatura em graus Fahrenheit: "))
    temperatura_c = 5 * ((temperatura_f - 32) / 9)
    print(f"A temperatura em graus Celsius é: {temperatura_c} °C")

def ex10():
    """Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""
    temperatura_c = float(input("Digite a temperatura em graus Celsius: "))
    temperatura_f = (temperatura_c * 9/5) + 32
    print(f"A temperatura em graus Fahrenheit é: {temperatura_f} °F")

def ex11():
    """Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo."""
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = float(input("Digite um número real: "))
    produto = (2 * num1) * (num2 / 2)
    soma = (3 * num1) + num3
    elevado = num3 ** 3
    print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
    print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
    print(f"O terceiro elevado ao cubo é: {elevado}")
    
def ex12():
    """Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""
def ex13():
    """Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7"""
def ex14():
    """João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""
def ex15():
    """Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme
    a tabela abaixo:
     + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Líquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido."""  
def ex16():
    """Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total."""     
def ex17():
    """Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    Misture latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
def ex18():
    """Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

if __name__ == "__main__":
    ex11()
    ex12()
    ex13()
    ex14()
    ex15()
    ex16()
    ex17()
    ex18()

