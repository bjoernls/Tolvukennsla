# Verkefni

### Verkefni 1 - Hello World
Opnið skipanagluggann (e. Terminal) og búið til nýja möppu með `mkdir` sem heitir `Verkefni`. Farið svo í þessa möppu með `cd`.

Búið til nýja skrá í þessari möppu sem heitir `verkefni1.py` og skrifið forrit í hana sem prentar út “**Hello World!**”.

```python
>>>mkdir Verkefni
>>>cd Verkefni
#skrifa forrit í editor
>>>python verkefni1.py
Hello World!
```

### Verkefni 2 - Strengjabreytur
Endurtakið verkefni 1 með því að nota breytu.
```python
>>>strengur = "Hello"
>>>#kóði hér
>>>print(strengur)
Hello World!
```

### Verkefni 3 - Reiknivél
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

### Verkefni 4 - Reiknivél áframhald
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

### Verkefni 5 - Villumeðhöndlun
Forritið er núna að verða flóknara og verður því brothættara fyrir vikið. Alltaf þegar beðið er um inntak frá notanda þarf að gera ráð fyrir **villumeðhöndlun**. 

Það eru tvö inntök í `Verkefni 4` og það þarf að passa upp á eftirfarandi:


* Inntak má aðeins vera `c` eða `f`, ef notandi slær inn eitthvað annað, þarf forritið að biðja um inntak þar til rétt svar er slegið inn.
    * **Auka valverkefni**: Notandinn fær 5 tilraunir og þá hættir forritið að keyra.
* Þegar slegið er inn gráðu sem á að reikna úr, verður inntakið að vera tölustafur. Sjáið kaflann um villumeðhöndlun.
    * Sama aukaverkefni og fyrir ofan.

```python
>>>python verkefni5.py
>>>Sláðu inn 'f' fyrir Fahrenheit í Celsius og 'c' fyrir Celsius í Fahrenheit: 
>>>a
>>>Vinsamlegast reyndu aftur (4 tilraunir eftir):
```
### Verkefni 6 - Fylkjareikningur
Skrifið fylki með a.m.k. 5 tölum og reiknið eftirfarandi:
* Meðaltal
* Hæsta gildi
* Lægsta gildi

```python
>>>gildi = [6, 2, -1, 9, 4]
>>>#kóði hér sem reiknar gildin fyrir ofan

```

Meðatal er fengið með að leggja saman tölurnar og deila með fjölda þeirra. Í dæminu fyrir ofan er meðaltalið:

```
Meðaltal = (6 + 2 + -1 + 9 + 4) / 5 
         = 4
```

### Verkefni 7 - Gagnavinnsla
Þið fáið skrá sem inniheldur alvöru gögn frá Veðurstofunni. Í þessari skrá er að finna meðalhitastig hvers mánaðar í Reykjavík frá árinu 1949 og til dagsins í dag. 

Verkefnið er að lesa inn þessa skrá og reikna út meðalhitastig fyrir hvert ár. Auk þess skal reikna hæsta og lægsta hitastig hvers árs.

Þar sem um óþekkt gögn sem fara mjög langt aftur í tímann er að ræða, teljið einnig fjölda mánaða í hverju ári og prentið út. Notið síðan þann fjölda mánaða sem þið tölduð til að reikna út meðaltalið.

```python
>>>python verkefni7.py
mánuðir árið 1949 eru 12
meðalhiti er 3.841666666666667
hámarkshitastig er 10.5
lágmarkshitastig er -2.7


mánuðir árið 1950 eru 12
meðalhiti er 4.791666666666667
hámarkshitastig er 12.4
lágmarkshitastig er -1.4


mánuðir árið 1951 eru 12
meðalhiti er 4.058333333333334
hámarkshitastig er 11.4
lágmarkshitastig er -3.0

...
```


### Verkefni 8 - Gagnavinnsla áframhald
Bætið við `Verkefni 7` þannig að fundið er hæsta og lægsta meðalhitastig hvers mánaðar.

T.d. ef meðalhitastig í Janúar 1949, 1950, 1951 eru 2,1°C, 2,2°C, 0.2°C, þá skilar forritið eftirfarandi
```python
Hæsta hitastig í Janúar var árið 1950 en þá var hitastigið 2.2°C. Lægsta hitastigið var árið 1951 en þá var það 0.2°C. Meðalhiti í Janúar er 1.5°C.
```
### Verkefni 9 - Föll (ef tími gefst)
Takið kóðan úr `Verkefni 5` og búið til fall úr því. Skilið svörunum úr `Verkefni 7` og `Verkefni 8` með valkostinum um að fá hitastigin í Fahrenheit-gráðum.
