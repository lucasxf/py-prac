# Integers
a = 5
b = 10
x = 2
y = 5

add = a + b # 15
subtract = a - b # -5
multiply = a * b # 50
divide = a / b # 0.5
power = x ** y # 2 ^ 5 = 32

multi_expressoes = a + b * x # 5 + 10 * 2 => 5 + 20 => 25
multi_expressoes2 = (a + b) * x # (5 + 10) * 2 => 15 * 2 => 30

tab = "\t"
lf = "\n"
tab_lf = f"{lf}{tab} - "
# to do: aprender a concatenar strings em múltiplas linhas rs
result = f"Operações: {tab_lf}soma: {add}{tab_lf}subtração: {subtract}{tab_lf}multiplicação: {multiply}{tab_lf}divisão: {divide}"
print(result)
result_potencia = f"{x}^{y}={power}"
print(result_potencia)

result_exp = f"{a}+{b}*{x}={multi_expressoes}" # 25
result_exp2 = f"({a}+{b})*{x}={multi_expressoes2}" # 30
print(result_exp)
print(result_exp2)

# Floats (pontos flutuantes)

fx = 0.1
fy = 0.2
fa = 0.3
fz = fx + fy
fb = 3
fc = fb * fx
print(fz) # 0.30000000000000004
print(fz == fa) # False
print(fc == fz) # True

# Integers & floats
# qualquer operação entre um int e um float, não importa o resultado, gera um float
int_a = 10 # inteiro
int_b = 2 # inteiro
xpto = int_a / int_b # 5.0 - flutuante (mesmo sendo um resultado inteiro)
zyx = int_a + 10.0 # 20.0 - flutuante
print(xpto)
print(zyx)

# é possível separar os dígitos com underscore (a partir do python 3.6)
numerao = 123456789
numerao_legivel = 123_456_789
numerissimo = 1_2_3_4_5_678_9
numerinho = 2_8 # jovem ainda
print(numerao == numerao_legivel == numerissimo) # True
print(numerinho) # 28

# Multiple assignment
nome, idade, sexo, feliz = "Lucas", 28, 'M', True # que recurso muito louco, pqp
lf_tab = "\n\t"
cadastro = f"\tNome: {nome}{lf_tab}Idade: {idade}{lf_tab}Sexo: {sexo}{lf_tab}Feliz: {feliz}"
print(cadastro)

# Constants 
# - convenção de nomenclatura = Java (snake_case + CAPS) ex.: => NOME_COMPLETO
# - não tem constantes em python, por convenção quando uma variavel seguir o padrão de nomenclatura
# de constantes, ela não deverá ser atualizada
DATA_NASCIMENTO = "05/11/1993"
print(DATA_NASCIMENTO)
DATA_NASCIMENTO = "01/01/1900" # funciona, mas é má prática (deveria ter sido tratada como constante)
print(DATA_NASCIMENTO)
