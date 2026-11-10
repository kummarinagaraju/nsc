def encrypt(text, key):
    text = text.replace(" ", "").upper()

    n = len(key)
    rows = (len(text) + n - 1) // n

    text = text.ljust(rows * n, 'X')

    matrix = [
        text[i:i+n]
        for i in range(0, len(text), n)
    ]

    order = sorted(range(n), key=lambda i: key[i])

    cipher = ""

    for col in order:
        for row in matrix:
            cipher += row[col]

    return cipher


def decrypt(cipher, key):
    n = len(key)
    rows = len(cipher) // n

    order = sorted(range(n), key=lambda i: key[i])

    matrix = [[''] * n for _ in range(rows)]

    pos = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[pos]
            pos += 1

    return ''.join(''.join(row) for row in matrix)


text = input("Enter plaintext: ")
key = input("Enter key: ").upper()

cipher = encrypt(text, key)

print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))