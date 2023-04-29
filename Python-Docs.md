# Print
Prenta  `print()` til að prenta hluti notum við   `print()`.

# Athugasemdir
Athugasemdir** **eru notaðar til þess að útskíra kóðann eða sem minnispunkta fyrir forritarann. Athugasmedir byrja á `#` og svo kemur athugasemdin t.d.

```python
# þetta er athugasemd!
```

# Breytur
Breytur** **eru notaða til að geyma gögn og þær verða til um leið og við setjum þær samasem þá gagna týpu sem við viljum geyma.
Í þessu dæmi er `nafn` breytan og `"Jane"` er það sem við viljum geyma í breytuni. 

```python
nafn = "Jane" 
```

Í Python þurfum við ekki að skilgreyna típuna sem við viljum geyma í breytuni.
Heiti á breytum geta verið stuttar ein og til dæmis x eða y eða lýsandi eins og nafn, aldur, meðaltal osf.

### Breytu nöfn
Breitur verða að:
	- Byrja á bókstaf a-z eða undirstriki _.
	- Breytur meiga bara innihalda stafi, tölustafi , undirstriki  (A-z, 0-9, and _ ).
	- Breytur eru hástafanæmar sem þíðir að *nafn, Nafn, og NAFN* eru þrjár mismunandi breytur.
	- Breyta má **EKKI** byrja á tölustaf.
	- Breyta má ekki vera eitt að Python lykilorðum (keywords) → sjá lista aftast.

Það er oft erfit að lesa breytur með fleyri en eitt orð en það er hægt að gera margt til að einfalda það.
Við getur notað undirstriki _ `fjöldi_sæta`. 
Við getum notað eitthvað sem heitir Camel Case 🐫 þar sem að hvert orð eftir fyrsta orðið byrjar á stórum staf f`jöldiSæta.` 
Við getur líka notað eittvað sem heitir snake case 🐍 en þá notum við undirstriki  f`jöldi_sæta_í_sal.` 

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
Í Python eru tv;r gerðir af tölum.
	- `int` 
	- `float`
Breytur meða tölu gagna gerðini eru búnar til .egar meður setur breytu samasem tölu.

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
Streingir eru umlyktir gæsalöppum sem eru annað hvort enfaldarar `'`  eða tvöfaldar `"`.
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

### Escape Characters
Eins og þið hafið tekið eftir þá notum við suma stafi sem við myndum kanski vilja nota inn í strengi til dæmis gæsalappir. Við getum ekki bara gert set tvöfaldar gæsa lappir in í streng sem er með tvöfaldar gæsa lappir því þá fáum við villu.
`txt = "We are the so-called "Vikings" from the north."`  Þetta er gerir villu.
í staðin þurfum við að nota Escape Character sem er backslash og svo stafurinn sem við viljum nota `\"`.
`txt = "We are the so-called "Vikings" from the north."`  Þetta er má.

# Booleans
Booleans getur annað hvort verið **Ture** eða **False.** 

# Aðgerðir
Python skyptir apgerðir í eftir frandi flokka:
	- Reykni aðgerðir
	- Gildings aðgerðir
	- Röksamanburðar aðgerðir
	- Röklegar aðgerðir
Reykni aðgerðir kannast flestir við en það eru:

| Tákn			| Heiti			| Dæmi			|
| ------------- | ------------- | ------------- |
| +				| Samlagning	| x + y			|
| -				| Frádráttur	| x - y			|
| *				| Margföldun	| x * y			|
| /				| Deiling		| x / y			|

