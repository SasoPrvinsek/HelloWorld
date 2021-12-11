import random

def rezultat(izbiraIgralec, winCondition, loseCondition):
    if izbiraIgralec == winCondition:
        return "zmagal je racunalnik"
    elif izbiraIgralec == loseCondition:
        return "zmagal je igralec"

izbira = ["kamen", "skarje", "papir"]
trenutnaIzbira = random.choice(izbira)

igralec = input("kamen, skarje, papir? ")

if igralec != "kamen" and igralec != "skarje" and igralec != "papir":
    print("vnesel si napacno orodje")
    exit()

print("racunalnik je izbral -", trenutnaIzbira)

while trenutnaIzbira == igralec:
    igralec = input("izenaceno...\nizberi ponovno: ")
    trenutnaIzbira = random.choice(izbira)
    print("racunalnik je izbral -", trenutnaIzbira)

trenutniRezultat = ""

if trenutnaIzbira == "kamen":
    trenutniRezultat = rezultat(igralec, "skarje", "papir")

if trenutnaIzbira == "skarje":
    trenutniRezultat = rezultat(igralec, "papir", "kamen")

if trenutnaIzbira == "papir":
    trenutniRezultat = rezultat(igralec, "kamen", "skarje")

print(trenutniRezultat)

