# Skrifið forrit sem fær inntak hitastig í Fahrenheit-gráðum frá notenda og skilar út Celsius-gráðum.

# Fá intak frá notanda
Tf = input("Sláðu inn hitastig í Farenheit: ")

# Formúlan er (f − 32) × 5/9, þar sem f er hitastig í Fahrenheit-gráðum.
fToC = (int(Tf) - 32) * 5/9

# setja breytuna fyrir celsius inn í streng til að segja hvað það er heitt úti í celcius gráðum
txt = "{}°F eru {}°C"
print(txt.format(Tf, fToC))

# Prófið forritið með eftirfarandi gildum:
# 0°F = -17.78 °C
# 32°F = 0°C
# 70°F = 21.11°C
# 100°F = 37.78 °C

