vstup = input(">")

samohlasky_count = 0
souhlasky_count = 0
cisla_count = 0
specialni_count = 0

for znak in vstup:
    if znak in "0123456789":
        cisla_count += 1
    elif znak in "aeiouy":
        samohlasky_count += 1
    elif znak in "bcdfghjklmnpqrstvwxz":
        souhlasky_count += 1
    else:
        specialni_count += 1

print(f"Samohlásek: {samohlasky_count}\nSouhlásek: {souhlasky_count}\nČísel: {cisla_count}\nSpeciální znaky: {specialni_count}\n")
