def encryptType(pss):
    if len(pss) % 3 == 0:
        type = "binBin"
    elif len(pss) % 3 == 1:
        type = "avanti"
    elif len(pss) % 3 == 2:
        type = "numeral"
    return type

def encryptor(pss, type):
    res = ""
    if type == "binBin":
        pass

def binBin(s):
    for char in s:
        n = ord(char)
        bin = ""
        while n >= 2:
            bin += str(n % 2)
            n /= 2
        bin = int(bin[::-1])
        res = ""
        while bin >= 2:
            res += str(bin % 2)
            bin /= 2
    return res