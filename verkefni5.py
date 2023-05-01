print("Settu inn 'f' fyrir Fahrenheit í Celsius og 'c' fyrir Celsius í Fahrenheit: ")
unit = input()

tilraunir = 4
while (unit != "c" and unit != "f" and tilraunir > 0):
    print("Aðeins 'c' eða 'f' eru leyfileg inntök. Vinsamlegast reyndu aftur ("+ str(tilraunir) +" tilraunir eftir)")
    unit = input()
    tilraunir = tilraunir - 1
    

if (tilraunir == 0):
    print("Slekk á forriti")
    import sys
    sys.exit(0)

if (unit == "c"):
    print("Sláðu inn hitastig í Celsius-gráðum:")
elif (unit == "f"):
    print("Sláðu inn hitastig í Fahrenheit-gráðum:")
gildi = input()

tilraunir = 4
gildiTolustafur = None
while (gildiTolustafur is None and tilraunir > 0):
    try:
        gildiTolustafur = int(gildi)
    except ValueError:
        print("Inntak verður að vera tölustafur ("+ str(tilraunir) +" tilraunir eftir)")
        gildi = input()
        tilraunir = tilraunir - 1
        

if (tilraunir == 0):
    print("Slekk á forriti")
    import sys
    sys.exit(0)

if (unit == "c"):
    fahrenheit = (int(gildiTolustafur) * (9/5)) + 32
    print(gildi + "°C eru "+ str(fahrenheit) +"°F")
elif (unit == "f"):
    celsius = (int(gildiTolustafur) - 32) * (5/9)
    print(gildi + "°F eru "+ str(celsius) +"°C")

