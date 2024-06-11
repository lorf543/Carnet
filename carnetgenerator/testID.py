import re




identification = "123-1234567-1"
pattern = "^[0-9\-]*$"

if re.match(pattern,identification):
    print("indetificacion valida")
else:
    print('Indentifiacion Invalida')

