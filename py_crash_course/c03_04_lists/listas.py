from operator import eq


naipes_truco = ['Zap', 'Copas', 'Espadilha', 'Pica fumo']

# acessando elementos
paus = naipes_truco[0]

print(paus)  # Zap
sete_copas = f"O famoso 7 {naipes_truco[1]}".upper()

print(sete_copas)  # O FAMOSO 7 COPAS

# sintaxe para acessar o último elemento de uma coleção: [-1]
# para o penúltimo: -2 (e assim sucessivamente)

ouros = naipes_truco[-1]  # Pica fumo
print(ouros)

espadas = f"4 de {naipes_truco[-2].upper()}"
print(espadas)  # 4 de ESPADILHA

# Changing, Adding, and Removing elements
# changing
print(naipes_truco)  # ['Zap', 'Copas', 'Espadilha', 'Pica fumo']
naipes_truco[2] = 'Espadas'
print(naipes_truco)  # ['Zap', 'Copas', 'Espadas', 'Pica fumo']

# appending to the end
bares = ["Porto Madalena", "Pasquim"]
print(bares)  # ['Porto Madalena', 'Pasquim']

bares.append("FrangÓ")
print(bares)  # ['Porto Madalena', 'Pasquim', 'Frang�']

# inserting (anywhere)
bares.insert(1, "Seu Domingos")
bares.insert(1, "quintal do espeto".title())
bares[0] = bares[0].upper()  # PORTO
# ['Porto Madalena', 'Quintal do Espeto', 'Seu Domingos', 'Pasquim', 'Frang�']
print(bares)

# Removing elements w/ index
# ['PORTO MADALENA', 'Quintal Do Espeto', 'Seu Domingos', 'Pasquim', 'Frang�']
print(bares)
print(bares[-1])  # Frangó


del bares[-1]
# ['PORTO MADALENA', 'Quintal Do Espeto', 'Seu Domingos', 'Pasquim']
print(bares)
print(bares[-1])  # Pasquim

# Removing with pop() (popping)
# o pop remove um item da lista e retorna o item removido para ser utilizado
# ['PORTO MADALENA', 'Quintal Do Espeto', 'Seu Domingos', 'Pasquim']
print(bares)
quintal_1 = bares[1]  # Quintal do Espeto
quintal_2 = bares.pop(1)  # Quintal do Espeto

print(quintal_1)
print(quintal_2)
print(quintal_1 == quintal_2)  # True
print(bares)  # ['PORTO MADALENA', 'Seu Domingos', 'Pasquim']

pasquim = bares.pop()
print(pasquim)  # Pasquim
print(bares)  # ['PORTO MADALENA', 'Seu Domingos']
bares.append("Pirajá")
bares.append("Seu Boteco")
bares.append("Água Doce Cachaçaria")
bares.append("Bar do Zeca Pagodinho")
bares.append("Bar da Alcione")
bares.append("Pirajá")
# ['PORTO MADALENA', 'Seu Domingos', 'Pirajá', 'Seu Boteco', 'Água Doce Cachaçaria', 'Bar do Zeca Pagodinho', 'Bar da Alcione', 'Pirajá']
print(bares)

# Removing and item by value
# remove apenas a primeira ocorrência, os demais elementos repetidos serão mantidos
bares.remove("Pirajá")
# ['PORTO MADALENA', 'Seu Domingos', 'Seu Boteco', 'Água Doce Cachaçaria', 'Bar do Zeca Pagodinho', 'Bar da Alcione', 'Pirajá']
print(bares)

sweet_water = "Água Doce Cachaçaria"
# aparentemente é void, o retorno foi 'None'
remocao = bares.remove(sweet_water)

# ['PORTO MADALENA', 'Seu Domingos', 'Seu Boteco', 'Bar do Zeca Pagodinho', 'Bar da Alcione', 'Pirajá']
print(bares)

print(remocao)  # None

# Organizing a list
# Sorting a list permanently with the sort() ***Method***
animais_alfabeto = ["Leão", "Cachorro", "Gato",
                    "Papagaio", "Baleia", "Águia", "Abelha", "Burro"]
animais_100_ordem = animais_alfabeto
# ['Leão', 'Cachorro', 'Gato', 'Papagaio', 'Baleia', 'Águia', 'Abelha', 'Burro']
print(animais_alfabeto)

animais_alfabeto.sort()
# ['Abelha', 'Baleia', 'Burro', 'Cachorro', 'Gato', 'Leão', 'Papagaio', 'Águia']
print(animais_alfabeto)
# ['Abelha', 'Baleia', 'Burro', 'Cachorro', 'Gato', 'Leão', 'Papagaio', 'Águia']
print(animais_100_ordem)
print(animais_100_ordem == animais_alfabeto)  # True

animais_alfabeto.sort(reverse=True)
# ['Águia', 'Papagaio', 'Leão', 'Gato', 'Cachorro', 'Burro', 'Baleia', 'Abelha']
print(animais_alfabeto)
print(animais_100_ordem == animais_alfabeto)  # True

# Sorting a List temporarily with the sorted() ***function***
equipes = ["Mercedes AMG", "Ferrari", "RBR", "Alpha Tauri", "McLaren"]

print("Fora de ordem:")
print(equipes)  # ['Mercedes AMG', 'Ferrari', 'RBR', 'Alpha Tauri', 'McLaren']

# diferente do método sort(), a função sorted() possui retorno
equipes_ordenadas = sorted(equipes)
print("Ordenadas:")
print(equipes_ordenadas)
print("A lista original permanece intacta:")
print(equipes)  # ['Mercedes AMG', 'Ferrari', 'RBR', 'Alpha Tauri', 'McLaren']

# Invertendo uma lista (não é reordenando em ordem oposta/decrescente, é exibindo ao contrário)
# .sort(reverse=True) é diferente de .reverse()
equipes.reverse()
equipes_ordenadas.reverse()

# ele quebra linha automaticamente na coluna 80
print(equipes)  # ['McLaren', 'Alpha Tauri', 'RBR', 'Ferrari', 'Mercedes AMG']
# ['RBR', 'Mercedes AMG', 'McLaren', 'Ferrari', 'Alpha Tauri']
print(equipes_ordenadas)

# 2 reverses em seguida retornam a lista ao estado original
equipes.reverse()
print(equipes)  # ['Mercedes AMG', 'Ferrari', 'RBR', 'Alpha Tauri', 'McLaren']

equipes.append("Alfa Romeo")
equipes.append("Aston Martin")
equipes.append("Haas")
equipes.append("Williams")
equipes.append("Alpine")
# Finding the length of a list
paddock = len(equipes)  # 10
print("# de garagens no paddock: ")
print(paddock)
