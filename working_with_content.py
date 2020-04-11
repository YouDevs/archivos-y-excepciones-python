filename = 'files/youtube_channels.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())

# ==== Contar las líneas ====
print( len( lines ) )

# ==== Buscando un elemento ====
print( 'YouDevs\n' in lines )
print( lines.index('YouDevs\n') )
print( lines.count( 'YouDevs\n' ) )