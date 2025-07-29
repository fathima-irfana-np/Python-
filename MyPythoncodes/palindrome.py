import sys
umar=input("Umar: ")
if not umar:
    print("Ramu: You didn’t say anything, Umar!")
    sys.exit(0)
ramu=input("Ramu: ")
rev=umar[::-1]
if rev==ramu:
    print("Umar: Ramu, You won!, Congrats!")
else:
    print("Umar: Sorry, Your answer is wrong ! Better try well next time !")