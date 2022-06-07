from email import message
from re import M
from tkinter import N


mensagem = "oi, mundão! ;)" # every variable is connected to a [value]
print("Msg:" + mensagem)
maiusculas = mensagem.capitalize() # pq não "capitaliou"?
print("Msg: " + mensagem)
print("Maiúsculas: " +maiusculas)
#print(palavras) # name 'palavras' is not defined
palavras = mensagem.split()
print("Msg: " + mensagem)
print(palavras) # ['Oi,', 'mundão!', ';)']
print(mensagem.capitalize()) # entendi, capitaliza apenas a primeira letra ¬¬


# naming rules and conventions
# only letters, numbers & underscodres: ex: My_variable_01
# they can start with letters or underscores, not numbers

name = "lUcAs xavier FerreirA"
name2 = "XAVIER ferreira"
name_title = name.title()
name_title2 = name2.title()
name_upper = name.upper()
name_lower = name.lower()
print(name) # lUcAs xavier FerreirA
print(name2) # XAVOER ferreira
print(name_title) # Lucas Xavier Ferreira
print(name_title2) # Xavier Ferreira
print(name_upper) # LUCAS XAVIER FERREIRA
print(name_lower) # lucas xavier ferreira

first_name = "Lucas"
middle_name = "Xavier"
last_name = "Ferreira"

# format Strings
full_name = f"Sr. {last_name.upper()}, {first_name}-{middle_name.lower()}" # f-Strings w/ placeholders: f as in Format,
print(full_name) # Sr. FERREIRA, Lucas-xavier

# Adding whitespaces to Strings with tabs or newlines
lu = "Lu" # Lu
lu_tab = f"\t{lu}" # '     Lu' (tab + str)
nl = "\n"
lu_new_line = "\nLu" # '[linha]Lu'
lu_new_line_f = f"{nl}{lu}"
print(lu_tab)
print(lu_new_line_f)

# Stripping whitespace
leading_ws = "     Salve"
trailing_ws = "E aí     "
both_paddings = "  coé  " #
print(leading_ws.lstrip()) # Salve
print(trailing_ws.rstrip()) # E aí
print(both_paddings.strip()) # 'coé' - o verdadeiro "trim()"
