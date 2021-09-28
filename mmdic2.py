import random

kleuren = ["oranje", "blauw", "groen", "bruin"]

def generateZak(amount:int):
    zak = {}
    for i in range(int(amount)):
        kleur = random.choice(kleuren)
        if kleur in zak:
            zak[kleur] += 1
        else:
            zak.update({kleur : 1})
    return zak
    
x = input("Hoeveel M&M's wil je in de zak  : ")
print(sorted(generateZak(x).items(), key= lambda kv:kv[1], reverse= True))