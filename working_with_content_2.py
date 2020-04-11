filename = 'files/lorem_ipsu.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

large_str = ''
for line in lines:
    large_str += line.rstrip()

# Contar las líneas
# print( lines )

# Accediendo al contenido por partes
print( large_str[:100] + "..." )

print( len( large_str ) )