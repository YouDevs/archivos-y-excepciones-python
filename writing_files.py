# ==== Modos de apertura: ====
# default (read mode): 'r'
# write mode: 'w'
# append mode: 'a'
# read and write: 'r+'

filename = 'files/programming_languages.txt'

# with open(filename, 'w') as f_obj:
#     f_obj.write('PHP\n')
#     f_obj.write('Python\n')
#     f_obj.write('Javascript\n')

# ==== Append Mode: ====
# with open(filename, 'a') as f_obj:
#     f_obj.write('C++\n')
#     f_obj.write('Rust\n')
#     f_obj.write('C#\n')

# ==== Un ejemplo más chido! ====
languages = ['PHP\n', 'Python\n', 'Javascript\n', 'C++\n', 'Rust\n', 'C#\n' ]
with open(filename, 'w') as f_obj:
    for language in languages:
        f_obj.write(language)