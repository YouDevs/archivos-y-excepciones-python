filename = 'files/youtube_channels.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()
    # print(lines)
    # Forma noob:
    # for line in f_obj:
        # # print(line)
        # print(line.rstrip())

for line in lines:
    print(line.rstrip())