def palyndrome(word):
    if len(word)<=1:
        return True
    else:
        if word[0]!=word[len(word)-1]:
            return False
        else:
            return palyndrome(word[1:len(word)-1])

def inversestring(word):
    inverse=str()
    for k in range(len(word)):
        inverse+=word[len(word)-1-k]
    return inverse

def solve55(n):
    total=0
    for k in range (n):
        if palyndrome(str(k))==False:
            compteur=0
            numero= str(k)
            while compteur<50 or not palyndrome(numero):
                compteur+=1
                numero=str(k+int(inversestring(str(k))))
            if compteur==50:
                total+=1
    return total
print(solve55(10000))
#le programme est très très long, il donne de bonne réponses pour des petits nombres mais sa compléxité
#est très handicapante pour 10 000, je n'ai pas pu avoir de résultat