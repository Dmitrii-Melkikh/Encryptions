def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    k=1
    l=int(n**0.5)
    for i in range(2,l+1):
        if n % l==0:
            k=0
            break
    if k==0:
        return False
    else:
        return True
    pass