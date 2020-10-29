

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
       if plaintext[i].isalpha():
           a=ord(plaintext[i])+shift
           if plaintext[i].islower():
               if a>ord('z'):
                a=a-26
               ciphertext=ciphertext+chr(a)
           else:
               if a>ord('Z'):
                a=a-26

               ciphertext=ciphertext+chr(a)
       else:
           ciphertext=ciphertext+plaintext[i]



    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for i in range(len(ciphertext)):
       if ciphertext[i].isalpha():
           a=ord(ciphertext[i])-shift
           if ciphertext[i].islower():
               if a<ord('a'):
                a=a+26
               plaintext=plaintext+chr(a)
           else:
               if a<ord('A'):
                a=a+26
               plaintext=plaintext+chr(a)
       else:
           plaintext=plaintext+ciphertext[i]

    return plaintext

