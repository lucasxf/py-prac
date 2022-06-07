# a simple dictionary
piloto_goat = {'nome': 'Lewis Hamilton', 'numero': 44,
               'WDC': 8, 'equipe': 'Mercedes'}

# {'nome': 'Lewis Hamilton', 'WDC': 8, 'equipe': 'Mercedes'}
print(piloto_goat)

print(piloto_goat['numero'])  # 44

print(f"{piloto_goat['nome']} {piloto_goat['numero']}")  # Lewis Hamilton 44

# working with dictionaries
# a dictionary in Python is a collection of key-value pairs

wdc_count = piloto_goat['WDC']
print(wdc_count)  # 8

# adding new key-value pairs
piloto_goat['pais'] = 'Inglaterra'
piloto_goat['age'] = 37

# {'nome': 'Lewis Hamilton', 'numero': 44, 'WDC': 8, 'equipe': 'Mercedes', 'pais': 'Inglaterra', 'age': 37}
print(piloto_goat)

# starting with an empty dictionary
k_dot = {}
k_dot['name'] = 'Kendrick Lamar'
k_dot['latest_album'] = 'Mr. Morale and the Big Steppers'
k_dot['fav_album'] = 'GoOd Kid MaAad City'
# {'name': 'Kendrick Lamar', 'latest_album': 'Mr. Morale and the Big Steppers'}
print(k_dot)

print(f"My fav album from {k_dot['name']} was '{k_dot['fav_album']}'")
# modifying values in a dictionary
k_dot['fav_album'] = 'DAMN'
# {'name': 'Kendrick Lamar', 'latest_album': 'Mr. Morale and the Big Steppers',
# 'fav_album': 'DAMN'}
# print(k_dot)

print(f"My fav {k_dot['name']} album now is '{k_dot['fav_album']}'")

k_dot['album_count'] = 4

# {'name': 'Kendrick Lamar', 'latest_album': 'Mr. Morale and the Big Steppers',
#    'fav_album': 'DAMN', 'album_count': 4}
print(k_dot)

k_dot['album_count'] = k_dot['album_count'] + 1

# {'name': 'Kendrick Lamar', 'latest_album': 'Mr. Morale and the Big Steppers',
# 'fav_album': 'DAMN', 'album_count': 5}
print(k_dot)

# removing key-value pairs
del k_dot['latest_album']

# {'name': 'Kendrick Lamar', 'fav_album': 'DAMN', 'album_count': 5}
print(k_dot)

# a dictionary of similar objects
fav_artists = {
    'lucas': 'Jorge Ben',
    'princesa': 'Ludmilla',
    'mulecao': 'Kendrick Lamar'
}

print(fav_artists)

artist = fav_artists['lucas']  # Jorge Ben
print(f"O arista favorito do Lucas é : {artist}")


# using get() to Access Values
# the get() method requires a key as a first argument
# as a second optoinal argument, you can pass the value to be returned
# if the key doesn't exist

# Traceback(most recent call last):
#   File "c:\repo\py-prac\py_crash_course\c06_dictionaries\dicionarios.py", line 75, in <module >
#     print(fav_artists['fulano'])
# KeyError: 'fulano'
# print(fav_artists['fulano'])

# .get(chave, valor-default-caso-chave-nao-exista)
desconhecido = fav_artists.get('fulano', 'Nao ha artistas para o Fulano')
print(desconhecido)  # Nao ha artistas para o Fulano

# .get(chave)
jorge = fav_artists.get('lucas')
print(jorge)  # Jorge Ben

# try it yourself
# person
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Xavier Ferreira',
    'idade': 28,
    'cidade': 'São Paulo'
}

print(pessoa['cidade'])  # São Paulo

# favorite numbers
numeros_favoritos = {
    'eren': 999_999_999,  # the rumbling
    'naruto': 1,  # hokage
    'luffy': 5,  # gear
    'vegeta': 8001,  # + de 8 mil
    'yusuke': 1_000  # sem criatividade pro Urameshi
}

print(numeros_favoritos['eren'])  # 999999999
print(numeros_favoritos['vegeta'])  # 8001

# looping through a Dictionary
# looping through all key-value pairs
pais_tropical = {
    'nome': 'Brasil',
    'clima': 'tropical (subtropical em boa parte do território, na verdade)',
    'bonito': 'por natureza',
    'carnaval': 'em fevereiro'
}

items = pais_tropical.items()
# dict_items([('nome', 'Brasil'),
# ('clima', 'tropical (subtropical em boa parte do territ�rio, na verdade)'),
# ('bonito', 'por natureza'), ('carnaval', 'em fevereiro')])
print(items)

# key-value pairs
for conjunto in pais_tropical.items():
    print(f"key-value pair: {conjunto}")

# key-value pair: ('nome', 'Brasil')
# key-value pair: ('clima', 'tropical (subtropical em boa parte do territ�rio, na verdade)')
# key-value pair: ('bonito', 'por natureza')
# key-value pair: ('carnaval', 'em fevereiro')

# key-value pairs
for chave, valor in pais_tropical.items():
    print(f"chave: {chave}, valor: {valor}")  # chave: nome, valor: Brasil...

# looping through all the keys in a dictionary
pagode_90 = {
    'Soweto': 'Maçã do Amor',
    'Exaltasamba': 'Cartão Postal',
    'Raça Negra': 'Jeito Felino',
    'SPC': 'Domingo',
    'Art Popular': 'Falando Segredo'
}

# apenas chaves
for grupo in pagode_90.keys():
    print(grupo)

# faz a mesma coisa que o bloco acima
for grupo in pagode_90:
    print(grupo)

for grupo, hit in pagode_90.items():
    print(f'Essa arranha:{ grupo} - {hit}')

# xpto tá vazio
xpto = {}
if xpto:
    print("Ok")
else:
    print("xpto  tá vazio")
