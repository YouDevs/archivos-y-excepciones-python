def count_words( filename ):
    try:
        with open('./files/' + filename) as f_obj:
            contents = f_obj.read()
            # print(contents)
    except FileNotFoundError:
        msg = "mmm... parece que el archivo " + filename + " no existe"
        print( msg )
    else:
        # Contar las palabras:
        words = contents.split()
        num_words = len( words )
        print("El archivo " + filename + " contiene: " + str( num_words) )

filenames = ['schopenhauer.txt', 'george_orwel.txt', 'zaratustra.txt']

for filename in filenames:
    count_words( filename )