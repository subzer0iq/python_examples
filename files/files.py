poem = '''There was a young lady named bright.
Whose speed was faster than light;
She started one day
In a relative way.
And returned on the previous night.'''
# Запись в файл
fout = open('relativity.txt','w')
print(poem, file=fout, sep='', end='')
fout.close()

# Запись в большой файл частями

fout = open('relativity.txt','w')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()
# read() - читает из файла за раз. readline() - Читает по одной строке за раз. readlines() - так же, но еще возврвщает список строк.
# Читать часями можно так:
poem = ''
fin = open('relativity.txt', 'r')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))