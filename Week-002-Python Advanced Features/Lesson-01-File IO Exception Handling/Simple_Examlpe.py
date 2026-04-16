text = []
print('Write a text here; quit with # sign')
while True:
    line = input()
    to_write = line.replace('#','') + '\n'
    text.append(to_write)
    if '#' in line:
        break

with open('mytext.txt', 'w') as f:
    f.writelines(text)

#       Outputs:
#               Write a text here; quit with # sign
#               Salamlar
#               #Salamlar