import random

# Nota random 0 - 2 til að ákveða hvort það sé skæri blað eða steinn
random_num = random.randint(0, 2)
# Gera lista með valmöguleika tölvunar
listi = ["skæri", "blað", "steinn"]

# Fá intak fá notanda. vista í breytu
# Breytu intak í lágstafi
val_notandi = input("Sláðu inn skæri, blað eða steinn: ").lower()

# búa til breytu með vali tölvunar
val_tolva = listi[random_num]


# bera saman intökin og skila hvort það var jafntefli
if val_notandi == val_tolva:
    print("Jafntefli")
elif val_notandi == "steinn" and val_tolva == "skæri":
    print("Notandi valdir {}, tölvan valdi {}, þú vanst".format(val_notandi, val_tolva))
elif val_notandi == "blað" and val_tolva == "steinn":
    print("Notandi valdir {}, tölvan valdi {}, þú vanst".format(val_notandi, val_tolva))
elif val_notandi == "skæri" and val_tolva == "blað":
    print("Notandi valdir {}, tölvan valdi {}, þú vanst".format(val_notandi, val_tolva))

else:
    print("Notandi valdir {}, tölvan valdi {}, þú tapaðir".format(val_notandi, val_tolva))

