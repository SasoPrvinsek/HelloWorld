import random

racunalnik = random.randint(1, 10)

user = int(input("izberi stevilko: "))

if user == racunalnik:
    print("bravo, uganili ste")
    exit()

while user != racunalnik:
    if user > racunalnik:
        print("imate previsoko stevilo")
    else:
        print("imate prenizko stevilo")    
    user = int(input("napacna stevilka... \nposkusi drugacno stevilko: "))
     
print("bravo uganili ste, racunalnik je izbral", racunalnik)

