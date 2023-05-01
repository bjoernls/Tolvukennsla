# Print
Til að prenta texta í skipunargluggann notum við   `print()`.

# Athugasemdir
Athugasemdir eru notaðar til þess að útskýra kóðann eða sem minnispunkta fyrir forritarann. Athugasmedir byrja á `#` og svo kemur athugasemdin t.d.

```python
# þetta er athugasemd!
```

# Breytur
**Breytur** eru notaðar til að geyma gögn og þær verða til um leið og við setjum þær samasem þá gagna týpu sem við viljum geyma.
Í þessu dæmi er `nafn` breytan og `"Jane"` er það sem við viljum geyma í breytuni. 

```python
nafn = "Jane" 
```

Í Python þurfum við ekki að skilgreyna týpuna sem við viljum geyma í breytunni.
Heiti á breytum geta verið stuttar eins og til dæmis x eða y, eða lýsandi eins og nafn, aldur, meðaltal osf.

### Breytu nöfn
Breytur verða að:
- Byrja á bókstaf a-z eða undirstriki _.
- Breytur mega bara innihalda stafi, tölustafi , undirstriki  (A-z, 0-9, and _ ).
- Breytur eru hástafanæmar sem þíðir að *nafn, Nafn, og NAFN* eru þrjár mismunandi breytur.
- Breyta má **EKKI** byrja á tölustaf.
- Breyta má ekki vera eitt af Python lykilorðum (keywords) → sjá lista aftast.

Það er oft erfitt að lesa breytur með fleiri en eitt orð en það er hægt að gera margt til að einfalda það.
Við getur notað undirstrik _ `fjöldi_sæta`. 
Við getum notað eitthvað sem heitir Camel Case 🐫 þar sem að hvert orð eftir fyrsta orðið byrjar á stórum staf f`jöldiSæta.` 
Við getur líka notað eittvað sem heitir snake case 🐍 en þá notum við undirstriki  `fjöldi_sæta_í_sal.` 

# Frálag
Í Python notum við `print()` fallið til að skila því sem við erum að gera.

```python
x = 5
print(x)

>>> 5
```
Við getum skilað mörgum breytum í  `print()` fallið með því að aðskilja þær með kommu `,`.

```python
x = "Python "
y = "er "
z = "skemtilegt "

print(x, y, z)
```

# Gerðir gagna
Hægt er að sjá af hvaða gerð gögnin erum sem við erum að vinna með með því að nota `type()` fallið.

```python
x = 5
print(type(x))
```

Hérna eru nokkrar algengar gerðir gagna:


| Syntax			| Type 				|
| ----------------- | ----------------- |
| x = "Hello World" | str  				|
| x = 20			| int  				|
| x = 20.5 		    | float				|


# Tölur
Í Python eru tvær gerðir af tölum:

- `int` 
- `float`

Breytur meða tölu gagna gerðini eru búnar til þegar meður setur breytu samasem tölu.

```python
x = 1    # int
y = 2.8  # float
```

Eins og var útskýrt hér á undan þá getum við notað `type()`  til að sjá af hvaða tölu gerð gögnin eru.

### Int
 Int eru helitölur jákvæðar eða neikvæðar án kommu.

```python
x = 1
y = 35656222554887711
z = -3255522
```
### Float
Float eða (floating point number) eru jákvæðar eða neikvæðar kommu tölur með fleiri ein eða fleiri aukastafi.

```python
x = 1.10
y = 1.0
z = -35.59
```
# Strengir
Strengir eru umluktir gæsalöppum sem eru annað hvort enfaldarar `'`  eða tvöfaldar `"`.
Við getum gert strengi sem eru nokkrar línur með því að nota þrjár tvöfaldar gæsalappir `"""` eða þrjár einfaldar gæsalappir `'''`.
Við getum sé hversu langur strengurinn er mað því að nota `len()` fallið.

```python
a = "Hello, World!"
print(len(a))

11
```
### Samskeyting
Í forritun virkar plúsin eins og í stærðfræði hann leggur saman tvær tölur. En eð við notum + með strengjum þá skeytir hann strengina saman. 

```python
fornafn = "Viktor"
eftirnafn = "Hollanders"

print(fornafn + eftirnafn)

ViktorHollanders
```
Eins og þið sjáið þá varð þetta eitt orð þrátt fyrir að við settum bil á milli `fornafns  + og eftirnanfn` . Þetta er vegna þess að samskeytingin les ekki bilin. Við þurfum sjálf að setja þau inn. Við getum gert að með því að bæta inn streng sem er bil `" "` eða með því að bæta bil fyrir aftan fornafn `"Viktor "` eða fyrir frama eftrirnafn `" Hollanders"`.
Hérna er þatta sýnt með bill inn í streyng

```python
fornafn = "Viktor"
eftirnafn = "Hollanders"

print(fornafn + " " + eftirnafn)

ViktorHollanders
```
### Samskeyting á mismunandi týpum

**Athugið** að **ekki** er hægt að skeyta saman tveimur mismunandi týpum, t.d. int og streng.

```python
>>> nafn = "Paul"
>>> aldur = 16
>>> print (nafn + " er " + aldur + " ára")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Í þessu tilfelli þurfum við að að nota `str()` fallið sem breytir int í streng
```python
>>> print (nafn + " er " + str(aldur) + " ára")
Paul er 16 ára
```

Samskonar fall `int()` er í boði ef breyta skal streng yfir í int.
```python
>>> aldur = "16"
>>> aldurEftirTvoAr = aldur + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> aldurEftirTvoAr = int(aldur) + 2
>>> print(aldurEftirTvoAr)
18
```

### Villumeðhöndlun

Passa þarf upp á að **strengurinn sé örugglega tölustafur**.
```python
>>> aldurBókstafir = "sextán"
>>> aldurTölustafir = int(aldurBókstafir)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'bla'
```

Oft fær forritið inntak frá notanda og því ekki hægt að vera viss um að það sem slegið er inn sé það sem beðið er um. Þá er hægt að "grípa" villur sem gætu átt sér stað og annaðhvort beðið notandann um að reyna aftur, eða slökkva á keyrslunni "gracefully".

```python
print ("Sláðu inn aldur: ")
aldurInntak = input()
aldur = -1
while (aldur == -1):
 try:
     aldur = int(aldurInntak)
 except ValueError:
     print("Inntak verður að vera tölustafur")
```
Takið eftir að forritið hér fyrir ofan keyrir þangað til að tölustafur er sleginn inn.
**Aukaverkefni:** Bætið við forritið þannig að aðeins tölustafir á milli 0 og 100 eru leyfilegir.

### Escape Characters
Eins og þið hafið tekið eftir þá notum við suma stafi sem við myndum kanski vilja nota inn í strengi til dæmis gæsalappir. Við getum ekki bara gert set tvöfaldar gæsa lappir in í streng sem er með tvöfaldar gæsa lappir því þá fáum við villu.
`txt = "We are the so-called "Vikings" from the north."`  Þetta er gerir villu.
í staðin þurfum við að nota Escape Character sem er öfugt skástrik og svo stafurinn sem við viljum nota `\"`.
`txt = "We are the so-called "Vikings" from the north."`  Þetta er má.

# Booleans
Booleans getur annað hvort verið **True** eða **False.** 

# Aðgerðir
Python skyptir aðgerðir í eftirfarandi flokka:

- Reikniaðgerðir
- Gildisveitingaraðgerðir
- Samanburðaraðgerðir
- Hallaðgerðir

### Reyknisaðgerðir
Reikniaðgerðir kannast flestir við en það eru:

| Aðgerð	| Heiti			    | Dæmi			|
| ------- | ------------- | --------- |
| +				| Samlagning	  | x + y			|
| -				| Frádráttur	  | x - y			|
| *				| Margföldun	  | x * y			|
| /				| Deiling		    | x / y			|
| %				| Eftirstöðvun	| x % y			|
| **			| Veldissetning	| x ** y		|

### Gildisveitingaraðgerðir
Gildisaðgerðir eru aðgerðir sem setja eitthvað gildi jafnt og eitthvað. I bland við reykni aðgerðir er hægt að nota gildisaðgerðir sem styttingu þannig að í stað þess að gera `x = x + 3` þá getum við gert `x += 3`. Þetta er hægt að gera með allar reyknisaðgerðirnar.

| Aðgerð	| Stytting dæmi	| Dæmi	     |
| ------- | ------------- | ---------- |
| =				| x = 5	        | x = 5			 |
| +=			| x += 3	      | x = x + 3	 |
| -=			| x -= 3	      | x = x - 3	 |
| *=			| x *= 3		    | x = x * 3	 |
| /=			| x /= 3	      | x = x / 3	 |
| %=			| x %= 3	      | x = x % 3	 |
| **=			| x **= 3	      | x = x ** 3 |
| &=			| x &= 3		    | x = x & 3	 |
| |=			| x |= 3	      | x = x | 3	 |


### Samanburðaraðgerðir
Gildingaraðgerðir eru notaðar til að bera saman tvö gildi.

| Aðgerð    | Heiti			              | Dæmi			|
| --------- | -------------           | --------- |
| ==			  | Samasem	                | x == y	  |
| !=			  | Ekki samasem            | x != y		|
| >				  | Stæra en	              | x > y			|
| <				  | Minna en		            | x < y			|
| >=			  | Stæra en eða jafnt og	  | x >= y		|
| <=				| Minna en eða jafnt og		| x <= y		|

### Hallaðgerðir
Hallalausir aðgerðir eru notuð til að sameina skilyrðisbundna  

| Aðgerð    | Heiti			                                      | Dæmi			        |
| --------- | ----------------------------------------------- | ----------------- |
| and			  | Skilar True	ef báðar fullyrðingarnar eru sannar | x < 5 and  x < 10 |
| or			  | Skilar True	ef önnur fullyrðingin eru sönn      | x < 5 or x < 4		|
|not			  | Skilar ósatt ef útkoman er sönn, snýr niðurstöðuni við | not(x < 5 and x < 10) |
