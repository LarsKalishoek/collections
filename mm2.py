import random
#kleuren m&m
kleuren = ["oranje ", " blauw ", " groen ", " bruin"]

#lijst van m&m
def generateZak(amount):
    zak = []    
    for i in range(int(amount)):
        zak.append(random.choice(kleuren))
    return zak

x = input("Hoeveel M&M's wil je in de zak  : ")
print(sorted(generateZak(x)))