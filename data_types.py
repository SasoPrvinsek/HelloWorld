celoStevilo = input("Vnesi celo stevilo: ")
decStevilo = input("Vnesi decimalno stevilo: ")
text = input("Vnesi text: ")
boolean = input("Vnesi true ali false: ")

print(type(celoStevilo), type(decStevilo), type(text), type(boolean))

celoStevilo = int(celoStevilo)
decStevilo = float(decStevilo)
boolean = bool(boolean)


print(type(celoStevilo), type(decStevilo), type(text), type(boolean))
print(celoStevilo, decStevilo, text, boolean)
