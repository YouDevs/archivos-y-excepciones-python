# ==== Abre el archivo ====
file_txt = open('files/pi_digits.txt')

# ==== Imprime el contenido ====
print( file_txt.read() )
# ==== Cerra el archivo ====
file_txt.close()
print( "archivo cerrado: ", file_txt.closed )

# ======================================

# ==== Con gestor de contexto: with ====
with open('files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print( contents.rstrip() )