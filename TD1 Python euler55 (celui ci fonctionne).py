def palyndrome(word):
    word=str(word)
    return word==word[::-1]

def lychrel(n):
    for k in range(50):
        n+=int(str(n)[::-1])
        if palyndrome(n):
            return 0
    return 1   

def solve55(n):
    return sum(lychrel(k) for k in range(0,n))

print(solve55(10000))