import random

winComp = "zmagal je racunalnik"
winIgralec = "zmagal je igralec"

izbira = ["kamen", "skarje", "papir"]
trenutnaIzbira = random.choice(izbira)

igralec = input("kamen, skarje, papir? ")

if igralec != "kamen" and igralec != "skarje" and igralec != "papir":
    print("vnesel si napacno orodje")

print("racunalnik je izbral -", trenutnaIzbira)

if trenutnaIzbira == igralec:
    print("izenaceno")
    exit()

if trenutnaIzbira == "kamen" and igralec == "skarje":
    print(winComp)
elif trenutnaIzbira == "kamen" and igralec == "papir":
    print(winIgralec)

if trenutnaIzbira == "skarje":
    if igralec == "papir":
        print(winComp)
    elif igralec == "kamen":
        print(winIgralec)

if trenutnaIzbira == "papir":
    if igralec == "kamen":
        print(winComp)
    elif igralec == "skarje":
        print(winIgralec)
            
