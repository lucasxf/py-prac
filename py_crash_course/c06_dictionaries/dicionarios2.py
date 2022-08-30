# nesting
# dictionaries within a list
# lists within a dictionary
snkr_0 = {'color': 'black', 'manufacturer': 'Nike', 'brand': 'Air Force'}
snkr_1 = {'color': 'white', 'manufacturer': 'Nike', 'brand': 'Air Jordan'}
snkr_2 = {'color': 'grey', 'manufacturer': 'Adidas', 'brand': 'Yeezy'}

snkrs = [snkr_0, snkr_1, snkr_2]

for snkr in snkrs:
    print(snkr)

# output
# {'color': 'black', 'manufacturer': 'Nike', 'brand': 'Air Force'}
# {'color': 'white', 'manufacturer': 'Nike', 'brand': 'Air Jordan'}
# {'color': 'grey', 'manufacturer': 'Adidas', 'brand': 'Yeezy'}
sneakers = []
for i in range(1, 11):
    new_snkr = {}
    if (i % 2 == 0):
        new_snkr['color'] = 'black'
    else:
        new_snkr['color'] = 'white'
    if (i % 5 == 0):
        new_snkr['manufacturer'] = 'Adidas'
    else:
        new_snkr['manufacturer'] = 'Nike'
    if (i <= 5):
        new_snkr['size'] = i+5
    else:
        new_snkr['size'] = i+1
    sneakers.append(new_snkr)

# print first 5 sneakers
for snkr in sneakers[:5]:
    print(snkr)

# resultado
# {'color': 'white', 'manufacturer': 'Nike', 'size': 6}
# {'color': 'black', 'manufacturer': 'Nike', 'size': 7}
# {'color': 'white', 'manufacturer': 'Nike', 'size': 8}
# {'color': 'black', 'manufacturer': 'Nike', 'size': 9}
# {'color': 'white', 'manufacturer': 'Adidas', 'size': 10}

print(f"Total collection of sneakers: {len(sneakers)}")

for snkr in sneakers:
    if snkr['color'] == 'black':
        snkr['model'] = 'Air Jordan 4 Retro'
    else:
        snkr['model'] = 'Air Force 1'

for snkr in sneakers[:4]:
    print(snkr)

# resultado
# {'color': 'white', 'manufacturer': 'Nike', 'size': 6, 'model': 'Air Force 1'}
# {'color': 'black', 'manufacturer': 'Nike', 'size': 7, 'model': 'Air Jordan 4 Retro'}
# {'color': 'white', 'manufacturer': 'Nike', 'size': 8, 'model': 'Air Force 1'}
# {'color': 'black', 'manufacturer': 'Nike', 'size': 9, 'model': 'Air Jordan 4 Retro'}

# a list in a dictionary
snkr_0 = {
    'sizes': [40, 40.5, 41],
    'model': 'Air Force 1 Mid x Off-White',
    'colors': ['Black', 'White']
}

snkr_1 = {
    'sizes': [40, 41, 42],
    'model': 'Air Jordan 4 Retro Canvas',
    'colors': ['Black']
}
snkrs = [snkr_0, snkr_1]

for snkr in snkrs:
    for size in snkr['sizes']:
        print(f"Numerações disponíveis do modelo {snkr['model']}: {size}")

# resultado (original)
# Numerações disponíveis: 40
# Numerações disponíveis: 40.5
# Numerações disponíveis: 41

# output novo
# Numerações disponíveis do modelo Air Force 1 Mid x Off-White: 40
# Numerações disponíveis do modelo Air Force 1 Mid x Off-White: 40.5
# Numerações disponíveis do modelo Air Force 1 Mid x Off-White: 41
# Numerações disponíveis do modelo Air Jordan 4 Retro Canvas: 40
# Numerações disponíveis do modelo Air Jordan 4 Retro Canvas: 41
# Numerações disponíveis do modelo Air Jordan 4 Retro Canvas: 42

for snkr in snkrs:
    print(f"Cores do modelo {snkr['model']}: {snkr['colors']}")
