
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = 0
    while len(keyword) < len(plaintext):
        keyword += keyword
    keyword = keyword.upper()
    for i in plaintext:
        if not i.isalpha():
            ciphertext += i
        else:
            r1 = ord(keyword[k])
            r2 = ord(i)
            r3 = r2 + (r1 - ord('A'))
            if i.isupper():
                if r3 > ord('Z'):
                    r3 -= 26
            else:
                if r3 > ord('z'):
                    r3 -= 26
            ciphertext += chr(r3)
        k =k+1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = 0
    while len(keyword) < len(ciphertext):
        keyword += keyword
    keyword = keyword.upper()
    for i in ciphertext:
        if not i.isalpha():
            plaintext += i
        else:
            r1 = ord(keyword[k])
            r2 = ord(i)
            r3 = r2 - (r1 - ord('A'))
            if i.isupper():
                if r3 < ord('A'):
                    r3 += 26
            else:
                if r3 < ord('a'):
                    r3 += 26
            plaintext += chr(r3)
        k =k+1
    return plaintext