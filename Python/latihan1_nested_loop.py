# Nested Loop For
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')

# Nested Loop While
string = ""
bar = 1
while bar <= 5:
    kol = bar
    while kol > 0:
        string += "*"
        kol -= 1
    string += "\n"
    bar += 1
print(string)

# Nested Loop Terbalik
a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('* ', end='')
    a -= 1
    print('')

# Nested Loop Segitiga
a = 5
s = a - 1
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
