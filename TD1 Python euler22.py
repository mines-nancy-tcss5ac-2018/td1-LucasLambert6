def valeurlettre(x):
    alphabet=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    valeur =0
    for k in range(len(alphabet)):
        if x == alphabet[k]:
            valeur= k
    return valeur

def solve22():
    f=open('p022_names.txt','r')
    liste=[]
    for ligne in f:
        liste+=ligne.split()
    liste=sorted(liste)
    total=0
    for k in range (len(liste)):
        score=0
        for i in range (len(liste[k])):
            score+=valeurlettre(liste[k][i])
        total+=score*(k+1)
    return total
print (solve22())
#le programme retourne une valeur incorrecte mais je ne vois pas du tout où peut être mon erreur