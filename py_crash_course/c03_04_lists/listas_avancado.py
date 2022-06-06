equipes = ["Mercedes AMG", "Ferrari", "RBR", "Alpha Tauri", "McLaren"]
i = 1
# Iterating/looping through an entire list
for equipe in equipes:
    print(equipe)

print("All teams are here. Let's race!")

# Numerical lists
# Using the range() Function
# in for
for value in range(1, 5):  # non-inclusive (will print 1 through 5)
    print(value)

x = range(-5, 1)
print(x)
for v in x:
    print(f"valor:{v}")  # printa "valor:-5" até "valor:0"

zero_ao_dez = range(11)
print(zero_ao_dez)  # range(0, 11)
for n in zero_ao_dez:
    print(f"no.{n}")  # no.0 - no.10

tabuada_do3 = range(0, 31, 3)
print(tabuada_do3)  # range(0, 31, 3)

tabuada3 = list(tabuada_do3)
print(tabuada3)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

quadrados = []
for value in range(1, 11):
    quadrado = value ** 2
    quadrados.append(quadrado)

print(quadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Simple statistics with a list of numbers
menor = min(quadrados)  # 1
maior = max(quadrados)  # 100
soma = sum(quadrados)  # 385

print(f"menor:{menor}\nmaior:{maior}\nsoma:{soma}")

# List comprehensions
# a list comprehension combines the for loop and the creation of new elements
# into one line, and automatically appends each new element
quads = [value ** 2 for value in range(1, 11)]

print(quads == quadrados)  # True
print(quads)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# try it yourself (exercícios)
# counting to twenty
for value in range(1, 21):
    print(value)

# one million
# [Done] exited with code=0 in 4.553 seconds
um_ao_milhao = range(1, 1_000_001)

# for value in um_ao_milhao:
#   print(value)

# summing a million
min_milhao = min(um_ao_milhao)  # 1
print(min_milhao)
max_milhao = max(um_ao_milhao)  # 1000000
print(max_milhao)
# 500000500000 (500_000_500_000) - 500.5 bilhões

sum_milhao = sum(um_ao_milhao)
print(sum_milhao)
# [Done] exited with code=0 in 0.338 seconds

# odd numbers
impares = range(1, 21, 2)
for impar in impares:
    print(impar)

# cubes
cubos = [value ** 3 for value in range(1, 11)]
print(cubos)  # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Working with part of a lsit
# Slicing a list
pilotos = ["Lewis Hamilton", "George Russel", "Charles Leclerc",
           "Carlos Sainz", "Valteri Bottas", "Checo Perez", "Verstappen"]
# ['Lewis Hamilton', 'George Russel', 'Charles Leclerc', 'Valteri Bottas', 'Carlos Sainz', 'Checo Perez']
print(pilotos)

pilotos_mercedes = pilotos[0:2]
print(pilotos_mercedes)  # ['Lewis Hamilton', 'George Russel']

pilotos_ferrari = pilotos[2:4]
print(pilotos_ferrari)  # ['Charles Leclerc', 'Carlos Sainz']

# últimos 2 pilotos, da RBR
print(pilotos[5:])  # ['Checo Perez', 'Verstappen']

pilotos.remove("Valteri Bottas")


rbr_ferrari = pilotos[-4:]
# ['Charles Leclerc', 'Carlos Sainz', 'Checo Perez', 'Verstappen']
print(rbr_ferrari)

ferrari_bois = pilotos[-4:2]
print(ferrari_bois)  # []

proper_ferrari_bois = pilotos[-4:-2]
print(proper_ferrari_bois)  # ['Charles Leclerc', 'Carlos Sainz']

proper_ferrari_bois2 = pilotos[-4:4]
print(proper_ferrari_bois2)  # ['Charles Leclerc', 'Carlos Sainz']

pilotos.append("Norris")
pilotos.append("Ricciardo")
pilotos.append("Bottas")
pilotos.append("Zhou")

print("The Alfa Romeo guys:")
for pilot in pilotos[8:]:
    print(pilot)

# Copying a list - use an unbounded slice
pilotos2 = pilotos[:]
print(pilotos == pilotos2)  # True
pilotos2.sort()
print(pilotos == pilotos2)  # False

print(pilotos)
print(pilotos2)

pilotos.append("Mick Schummacher")
pilotos2.append("Magnussen")

print(pilotos)
print(pilotos2)

# try it yourself
# slices
print("Os 3 1os pilotos são:")
for p in pilotos[0:3]:
    print(p)

print("O mid field:")
for p in pilotos[4:7]:
    print(p)

print("Retardatários:")
for p in pilotos2[-3:]:
    print(p)
