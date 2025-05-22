# EXERCÍCIO 1
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada.
# Calcular e escrever: o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência.

#Variáveis Iniciais
LarguraComodo = float(input("Informe a largura do cômodo: "))
ComprimentoComodo = float(input("Informe o comprimento do cômodo: "))
PotenciaLampada = float(input("Informe a potência das lâmapadas que você escolheu: "))

#Variáveis de Cálculo
MedidaQuarto = LarguraComodo*ComprimentoComodo
PotNecessaria = MedidaQuarto*3
QuantLampadas = round((PotNecessaria/PotenciaLampada), 0)

print("Você precisará de ", QuantLampadas, "lâmpadas para iluminar o cômodo.")



# Exercício 2 -Escreva um programa para ler as dimensões de uma cozinha 
# retangular (comprimento, largura e altura), calcular e escrever a 
# quantidade de caixas de azulejos para se colocar em todas as 
# suas paredes (considere que não será descontada a área 
# ocupada por portas e janelas).
# Cada caixa de azulejos possui 1,5 m²

#Varivél inicial
largura = float(input('Informe a largura em metros:'))
comprimento = float(input('Informe o comprimento em metros:'))
altura = float(input('Informe a altura em metros:'))

#Variavél de cálculo
l_x_c_m2 = largura * comprimento
l_x_a_m2 = largura * altura
m2_t = l_x_a_m2 + l_x_c_m2
totalcaixas = round((m2_t / 1.5), 2)
print('Total de caixas:', totalcaixas)



# EXERCÍCIO 3
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros  de combustível gasto e o valor total (R$) recebido dos passageiros.
# Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia.

#Variáveis Iniciais
kminic = float(input("Informe a quilometragem inicial do dia de hoje:"))
kmfim = float(input("Informe a quilometragem final do dia de hoje:"))
combgasto = float(input("Informe quantos litros de combustível você consumiu no dia de hoje:"))
valorrecebido = float(input("Informe o valor recebido dos passageiros no dia de hoje:"))

#Variáveis de Cálculo
kmdia = round((kmfim-kminic), 2)
mediakm = (kmdia/combgasto)
lucrodia = (round((valorrecebido - (kmdia*4.87)),2))

#Resultados
print("A sua média de consumo hoje foi de ", mediakm, "km/L, enquanto seu lucro foi de R$", lucrodia)



# Exercício 4: Escreva um programa que leia o código de origem de um 
# produto e imprima na tela a região de sua procedência, conforme 
# a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o 
# produto deve ser encarado como “Importado”.

codigo = int(input("Digite o código de origem do produto: "))

if codigo == 1:
    regiao = "Sul"
elif codigo == 2:
    regiao = "Norte"
elif codigo == 3:
    regiao = "Leste"
elif codigo == 4: 
    regiao = "Oeste"
elif codigo == 5 or codigo == 6:
    regiao = "Nordeste"
elif codigo in [7,8,9]:
    regiao = "Sudeste"
elif 10 <= codigo <= 20:
    regiao = "Centro-Oeste"
elif 21 <= codigo <=30:
    regiao = "Nordeste"
else:
    regiao = "Importado"
print(f"A região de procedência do produto é {regiao}")



# Exercício 5
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

if nota_optativa != -1:
    if nota1 < nota2:
        nota1 = nota_optativa
    else:
        nota2 = nota_optativa

media = (nota1 + nota2) / 2

if media >= 6.0:
    situacao = "Aprovado"
elif media < 3.0:
    situacao = "Reprovado"
else:
    situacao = "Exame"

print(f"Média do semestre: {media:.1f}")
print(f"Situação: {situacao}")
