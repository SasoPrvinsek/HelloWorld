import random

winComp = "zmagal je racunalnik"
winIgralec = "zmagal je igralec"

izbira = ["kamen", "skarje", "papir"]
trenutnaIzbira = random.choice(izbira)

igralec = input("kamen, skarje, papir? ")

if igralec != "kamen" and igralec != "skarje" and igralec != "papir":
    print("vnesel si napacno orodje")
    exit()

print("racunalnik je izbral -", trenutnaIzbira)

if trenutnaIzbira == igralec:
    print("izenaceno")
    exit()


def izbiraKamen(izbiraIgralec):
    if izbiraIgralec == "skarje":
        return "zmagal je racunalnik"
    elif izbiraIgralec == "papir":
        return "zmagal je igralec"

def izbiraSkarje(izbiraIgralec):
    if izbiraIgralec == "papir":
        return "zmagal je racunalnik"
    elif izbiraIgralec == "kamen":
        return "zmagal je igralec"

def izbiraPapir(izbiraIgralec):
    if izbiraIgralec == "kamen":
        return "zmagal je racunalnik"
    elif izbiraIgralec == "skarje":
        return "zmagal je igralec"

if trenutnaIzbira == "kamen":
    print(izbiraKamen(igralec))

if trenutnaIzbira == "skarje":
    print(izbiraSkarje(igralec))

if trenutnaIzbira == "papir":
    print(izbiraPapir(igralec))
    
