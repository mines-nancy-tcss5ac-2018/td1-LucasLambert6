def solve16(n):
    a=2**n
    chaine=str(a)
    somme = 0
    for k in range (len(chaine)):
        somme+=int(chaine[k])
    return somme
assert solve16(15)==26
print (solve16(1000))
