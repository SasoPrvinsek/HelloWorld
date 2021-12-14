myDict = {
    "bmw": 2.0, 
    "audi": 1.8, 
    "ford": 8.0,  
}
"""
for key, value in myDict.items(): 
    print("moc motorja", key, "je", value)

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

print(myDict["ford"])"""

cars = {
    "bmw": {
        "bhp": 250,
        "model": "e46",
        "engine": "3.0",
        "gear": 15,
    },
    "audi": {
        "bhp": 300,
        "model": "a4",
        "engine": "8.0",
        "gear": 18,
    },
    "ford": {
        "bhp": 500,
        "model": "mustang",
        "engine": "V8",
        "gear": 4,
    },
}

for znamka, lastnosti in cars.items():
    print(znamka)
    for lastnost, vrednost in lastnosti.items():
        print("\t", lastnost, "je", vrednost)

print(type(cars.keys()))
print(cars.keys())

"""znamke = []
for key in cars.keys():
    znamke.append(key)
"""
znamke = [key for key in cars.keys()]

print("koliko je moc", znamke[0])    