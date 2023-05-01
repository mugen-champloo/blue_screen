def password_generator(num):
    from string import ascii_lowercase, ascii_uppercase
    import random
    lowers = list(ascii_lowercase)
    uppers = list(ascii_uppercase)
    symbols = ['@', '#', '$', '%', '&', '!', '?', '^', '~', '<', '>']
    a = num // 4
    b = num - a * 3
    numbers = ''
    up = ''
    low = ''
    symb = ''
    for i in range(a):
        numbers += str(random.randint(0, 9))
        symb += random.choice(symbols)
        low += random.choice(uppers)
    for i in range(b):
        up += random.choice(lowers)
    pswd = list(numbers + up + low + symb)
    random.shuffle(pswd)
    return "".join(pswd)


n = int(input())
print(password_generator(n))
