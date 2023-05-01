# Verkefni

### Verkefni 1
Opnið skipanagluggann (e. Terminal) og búið til nýja möppu með `mkdir` sem heitir `Verkefni`. Farið svo í þessa möppu með `cd`.

Búið til nýja skrá í þessari möppu sem heitir `verkefni1.py` og skrifið forrit í hana sem prentar út “**Hello World!**”.

```python
>>>mkdir Verkefni
>>>cd Verkefni
#skrifa forrit í editor
>>>python verkefni1.py
Hello World!
```

### Verkefni 2
Endurtakið verkefni 1 með því að nota breytu.
```python
>>>strengur = "Hello"
>>>#kóði hér
>>>print(strengur)
Hello World!
```

### Verkefni 3
Skrifið forrit sem biður um hitastig í Fahrenheit-gráðum frá notenda og skilar út Celsius-gráðum. Notið `input()`, sjá fylgiskjal.

Formúlan er `(Tf − 32) × 5/9`, þar sem Tf er hitastig í Fahrenheit-gráðum.

Prófið forritið með eftirfarandi gildum:

0°F = -17.78 °C

32°F = 0°C

70°F = 21.11°C

100°F = 37.78 °C

```python
>>>python verkefni3.py
>>>Sláðu inn hitastig í Fahrenheit-gráðum:
>>>32
100°F eru 37.77777777777778°C
```
**ATH** inntakið er strengur, svo áður en það er notað til að reikna þarf að breyta því í int. Sjá `int()` í fylgiskjali.

### Verkefni 4
Haldið áfram með `Verkefni 3` nema núna verður líka hægt að reikna í hina áttina, þar sem notandinn fær möguleikann á að velja hvort inntakið sé í Celsius eða Fahrenheit. 

Formúlan úr Celsius í Fahrenheit: `(Tc × 9/5) + 32`, þar sem Tc eru gráður í Celsius

Bætið við inntaki sem biður um hvort eigi að reikna úr celsius eða fahrenheit gráðum

```python
>>>python verkefni4.py
>>>Sláðu inn 'f' fyrir Fahrenheit í Celsius og 'c' fyrir Celsius í Fahrenheit: 
>>>c
>>>Sláðu inn hitastig í Celsius-gráðum:
>>>0
0°C eru 32°F
```

### Verkefni 5
