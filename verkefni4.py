fOrC = input("Sláðu inn 'f' fyrir Fahrenheit í Celsius og 'c' fyrir Celsius í Fahrenheit: ")

if (fOrC == "f"):
    c = input("Sláðu inn hitastig í Celsius-gráðum: ")
    Tf =  (int(c) * 9/5) + 32
    txt = "{}°C eru {}°F"
    print(txt.format(c, Tf))

elif (fOrC == "c"):
    f = input("Sláðu inn hitastig í Farennheit-gráðum: ")
    Tc = (int(f) - 32) * 55/9
    txt = "{}°F eru {}°C"
    print(txt.format(f, Tc))