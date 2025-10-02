import math
cases = int(input().rstrip())


for i in range(cases):
    line = int(input().rstrip())
    
    print(line, end = " ") #print number back out
    
    #yin and yang
    if line%2==0:
        print("Yang", end = " ")
    else:
        print("Yin", end = " ")
    
    #element
    elements = ["wood", "fire", "earth", "metal", "water"]
    element = line - 4
    element = element%10
    element = math.floor(element/2)
    print(elements[element], end = " ") 
    
    #figurwe out animal
    animals = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "goat", "monkey", "rooster", "dog", "pig"]
    year = line - 4
    year = year%12
    print(animals[year])
