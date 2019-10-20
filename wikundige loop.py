import os
your_number1 = float(input("geef mij een nummer : "))
your_number2 = float(input("geef mij een nummer: "))
ja_neen = input("zijn je nummers  " + str(your_number1) + " en " + str(your_number2) + " ?\nantwoord met ja of neen")
if ja_neen == "neen":
    your_number1 = float(input("geef mij het correcte nummer: "))
    your_number2 = float(input("geef mij het correcte nummer: "))
else: print("Dat is goed")

bewerking = input("wat wil je doen? \n + , - , *, of / ? ")
if bewerking == "+":
    print(your_number1 + your_number2)
elif bewerking == "-":
    print(your_number1 - your_number2)
elif bewerking == "*":
    print(your_number1 * your_number2)
elif bewerking == "/":
    print(your_number1 / your_number2)
else:
    print("verkeerde wiskundige formule")
voortdoen = str(input("wil je voortdoen\n antwoord met ja of neen: ? "))
while voortdoen != str("neen"):
    your_number1 = float(input("geef mij een nummer : "))
    your_number2 = float(input("geef mij een nummer: "))
    ja_neen = input(
        "zijn je nummers  " + str(your_number1) + " en " + str(your_number2) + " ?\nantwoord met ja of neen")
    if ja_neen == "neen":
        your_number1 = float(input("geef mij het correcte nummer: "))
        your_number2 = float(input("geef mij het correcte nummer: "))
    else:
        print("Dat is goed")

    bewerking = input("wat wil je doen? \n + , - , *, of / ? ")
    if bewerking == "+":
        print(your_number1 + your_number2)
    elif bewerking == "-":
        print(your_number1 - your_number2)
    elif bewerking == "*":
        print(your_number1 * your_number2)
    elif bewerking == "/":
        print(your_number1 / your_number2)
    else:
        print("verkeerde wiskundige formule")
    voortdoen = str(input("wil je voortdoen\n antwoord met ja of neen: ? "))
os.system('pause')
