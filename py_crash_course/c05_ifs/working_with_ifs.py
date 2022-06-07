teams = ["Mercedes", "RBR", "Ferrari", "McLaren"]

# checking for equality
for team in teams:
    if team == "Mercedes":
        print(f"The best team: {team}")
    else:
        print(f"Just a regular team: {team}")

# checking for inequality
my_age = 29

if my_age != 28:
    print("Wrong age!")

some_age = 30
if some_age > my_age:
    print(my_age)

first_name = "Lucas"
middle_name = "Xavier"
last_name = "Ferreira"

if ('Lucas' == first_name and 'Ferreira' == last_name):
    print(f"{first_name} {last_name}")

if ('Lucas' == first_name or 'Xavier' == middle_name):
    print("at least one of the names is correct")

# Checking whether a value is in a list
if "Merc" or "Mercedes" in teams:
    print("The teams are alright")
    print(teams)  # ['Mercedes', 'RBR', 'Ferrari', 'McLaren']

if "Ferrari" and "McLaren" in teams:
    print("The teams are still ok")

if "Alfa Romeo" not in teams:
    print("The teams were missing Alfa Romeo... adding it to them")
    teams.append("Alfa Romeo")
    print(teams)  # ['Mercedes', 'RBR', 'Ferrari', 'McLaren', 'Alfa Romeo']

# Boolean expressions
age = 16
if age >= 18:
    print("Cê já pode beber rs")
else:
    print("Você é jovem demais para ingerir bebidas alcoólicas")


setores = ["arquibancada", "numerada", "camarote", "paddock"]

valor_ingresso = "Valor do ingresso: R$"

for setor in setores:
    if setor == "arquibancada":
        print(f"{valor_ingresso}300.00")
    elif setor == "numerada":
        print(f"{valor_ingresso}800.00")
    elif setor == "camarote":
        print(f"{valor_ingresso}3000.00")
    else:
        print(f"{valor_ingresso}45000.00")

# checking that a list is not empty
equipes = []

# Paddock vazio
if equipes:
    print("Paddock cheio")
else:
    print("Paddock vazio")

equipes.append("Mercedes")


if equipes:
    print("Paddock cheio")
    print(equipes)  # ['Mercedes']
else:
    print("Paddock vazio")

# multiple lists
from_software_games = ["Elden Ring", "Bloodborne",
                       "Dark Souls", "Demon's Souls", "Sekiro"]
bungie_games = ["Destiny", "Destiny 2"]
nintendo_games = ["Zelda", "Pokemon HG", "Pokemon SS", "Super Mario"]
favorite_games = ["Elden Ring", "Bloodborne",
                  "God of War", "Pokemon HG", "Destiny 2"]
if favorite_games and from_software_games:
    for fav in favorite_games:
        if fav in from_software_games:
            print(f"{fav} is a favorite game by From Software")
        if fav in nintendo_games:
            print(f"{fav} is a favorite game by Nintendo")

# Elden Ring is a favorite game by From Software
# Bloodborne is a favorite game by From Software
# Pokemon HG is a favorite game by Nintendo

# try it yourself
# hello admin
users = ["lucas", "xavier", "ferreira",
         "admin", "fulano", "ciclano", "beltrano"]
if users:
    for user in users:
        if 'admin' == user:
            print("Hello admin, here are the systems latest logs:")
        else:
            print(f"Hello {user}, welcome!")

print(users)
while(users):
    print(users.pop())

# no users
if users:
    print(users)
else:
    print("We need to find some users!")

# checking usernames
current_users = ['admin', 'hr', 'lucas', 'xavier', 'ferreira', 'joao', 'maria']
new_users = ['fulano', 'maria', 'ciclano', 'ferreira', 'joaozinho']

if current_users and new_users:
    for user in new_users:
        if user in current_users:
            print(
                f"The username: '{user}' us currently in used. Please enter a different one.")
        else:
            print(f"The username '{user}' is currently available.")

# ordinal numbers
regular_numbers = range(1, 10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in regular_numbers:
    if 1 == n:
        print(f"{n}st")
    elif 2 == n:
        print(f"{n}nd")
    elif 3 == n:
        print(f"{n}rd")
    else:
        print(f"{n}th")
