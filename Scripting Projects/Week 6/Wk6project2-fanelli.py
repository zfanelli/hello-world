code = input("Enter the encrypted message: ")
distance = int(input("Enter the distance value used for encryption: "))

plainText = ""

for ch in code:
    if ch.islower():
        ordValue = ord(ch)
        plainValue = ordValue - distance

        if plainValue < ord('a'):
            plainValue = ord('z') - (distance - (ord('a') - ordValue - 1))

        plainText += chr(plainValue)
    elif ch.isupper():
        ordValue = ord(ch)
        plainValue = ordValue - distance

        if plainValue < ord('A'):
            plainValue = ord('Z') - (distance - (ord('A') - ordValue - 1))

        plainText += chr(plainValue)
    else:
        plainText += ch  

print("Decrypted message:", plainText)


