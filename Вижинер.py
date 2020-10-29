
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
    for i in range(len(plaintext)):
       if plaintext[i].isalpha():

           if plaintext[i].islower():
               a = ord(plaintext[i]) + (ord(keyword[i % len(keyword)]) - ord('a'))
               if a>ord('z'):
                a=a-26
               ciphertext=ciphertext+chr(a)
           else:
               a = ord(plaintext[i]) + (ord(keyword[i % len(keyword)]) - ord('A'))
               if a>ord('Z'):
                a=a-26

               ciphertext=ciphertext+chr(a)
       else:
           ciphertext=ciphertext+plaintext[i]
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
    for i in range(len(ciphertext)):
       if ciphertext[i].isalpha():

           if ciphertext[i].islower():
               a = ord(ciphertext[i]) - (ord(keyword[i % len(keyword)]) - ord('a'))
               if a<ord('a'):
                a=a+26
               plaintext=plaintext+chr(a)
           else:
               a = ord(ciphertext[i]) - (ord(keyword[i % len(keyword)]) - ord('A'))
               if a<ord('A'):
                a=a+26
               plaintext=plaintext+chr(a)
       else:
           plaintext=plaintext+ciphertext[i]
    return plaintext