#exercícios:
#-------------------------------BASKARA-------------------------------
#4 - Crie uma função python que cálcule uma função de 2º Grau

  #Delta = B² - 4AC
  #Bhāskara = -B +- (raiz de delta)/ 2A

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
raiz = ''
delta = 0
x1 = 0
x2 = 0

print('Sua equação é: ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c) + ' = 0')

def baskara(){
delta = ((b ** 2)-(4*a*c))
raiz = (delta ** 0.5) 
x1 = ((-b) + (raiz/(2*a)))
x2 = ((-b) - (raiz/(2*a)))
# b² - 4*a*c
# -b+- raiz(delta)
print('Suas raizes são x1:' + str(x1) + ' e x2:' + str(x2))
}

print(baskara)





#-------------------------------AREA E COMPRIMENTO-------------------------------
#5 - Faça um programa que leia o raio de um círculo e faça duas
#funções: uma que calcule a área do círculo e outra que calcule
#o comprimento do círculo.
 raio = float(input('Digite o valor do raio: '))
 area = 0
 pi = 3.1415
 comprimento = 0

  def calculoRaio(){
       if raio > 0:
        area = pi*(raio ** 2)
        print('Area: ' + str(area))

  }
  def calculoComprimento(){
     if raio > 0:
      comprimento = 2*pi*raio
      print('Comprimento: ' + str(comprimento))

  }







#-------------------------------SALARIO-------------------------------
#1 - Escreva um programa que leia o nome de um funcionário,
#seu número de horas trabalhadas, o valor que recebe por hora
#e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.
 nome = input('Digite seu nome: ')
 horas = int(input('Digite quantas horas voce trabalhou: '))
 valor = float(input('Digite quanto ganha por hora: '))
 salario = (valor*horas)*22
 print('Voce é ' + str(nome) + ' e seu salario é de ' + str(salario) 'reais')





# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar
# apenas o maior valor e printar em tela.

import random as r
v_lista =[]
i = 1

 while i <= 20:
    v_lista.append(r.randrange(1, 100, 3))
    i+=1
    print(f'Lista Gerada Randomicamente: {v_lista}')    

  def maioral(v_lista):
    print('Maior valor: ', max(v_lista))
  
  maioral(v_lista)




# 3 - crie uma lista com 10 números aleatórios,
# itere essa lista e printar em tela os
# valores que são ímpares e pares.

# Essa foi a lista gerada aleatóriamente:
# [37, 52, 73, 91, 49, 67, 19, 64, 58, 22]
# ímpares: [37, 73, 91, 49, 67, 19]
# pares: [52, 64, 58, 22]

lista = []
import random as r
i = 0

 while i <= 20:
    lista.append(r.randrange(1, 100, 3))
    i+=1
    print(f'Lista Gerada Randomicamente: {lista}')    
  
  def maioral(lista):
    par = []
    impar = []
  for i in lista:
    if(i%2==0):
      par.append(i)
    else
      impar.append(i)
  print(impar{f'{numeros}'})
  print(par{f'{numeros}'})
maioral(lista)




maioral(v_lista)








