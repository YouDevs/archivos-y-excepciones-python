filename = 'youdevs.txt'

# ==== Manejo de exception: FileNotFoundError ====
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "mmm... parece que el archivo " + filename + " no existe"
    print( msg )
