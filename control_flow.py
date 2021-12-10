semafor = input("kaksna je barva semaforja? ")
#print(semafor)
if semafor != "zelena" and semafor != "rumena" and semafor != "rdeca":
    print("napacna barva, poskusi se enkrat")

if semafor == "zelena" or semafor == "rumena" or semafor == "rdeca":
    print("tako je")

if semafor == "zelena":
    print("lahko speljes")
elif semafor == "rumena":
    print("stop na gas")
else:
    print("ustavi se!") 
 