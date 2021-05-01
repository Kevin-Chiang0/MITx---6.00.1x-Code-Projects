import string
def A(shift):
    cipher = {}
    x = string.ascii_lowercase[shift:] + (string.ascii_lowercase[0:shift]) + string.ascii_uppercase[shift:] + (string.ascii_uppercase[0:shift])
    print(x)
    print(string.ascii_letters)
    count = 0
    print()
    for a in string.ascii_letters:
        cipher[a] = x[count]
        count += 1
    print (cipher.values)

A(26)
