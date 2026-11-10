def encrypt(text, rails):
    fence = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(cipher, rails):
    pattern = []
    row = 0
    direction = 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]

    fence = []
    pos = 0

    for count in counts:
        fence.append(list(cipher[pos:pos+count]))
        pos += count

    indexes = [0] * rails
    result = ""

    for r in pattern:
        result += fence[r][indexes[r]]
        indexes[r] += 1

    return result


text = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

cipher = encrypt(text, rails)

print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, rails))