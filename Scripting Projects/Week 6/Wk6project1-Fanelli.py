plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

code = ""

for ch in plainText:
    if ch.islower():
        ordValue = ord(ch)
        cipherValue = ordValue + distance

        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)

        code += chr(cipherValue)
    elif ch.isupper():
        ordValue = ord(ch)
        cipherValue = ordValue + distance

        if cipherValue > ord('Z'):
            cipherValue = ord('A') + distance - (ord('Z') - ordValue + 1)

        code += chr(cipherValue)
    else:
        code += ch  

print("Encrypted text:", code)
