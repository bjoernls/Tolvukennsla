def prenta(hitastig_ar_samtals, manudir_i_ari):
    medalhiti = hitastig_ar_samtals / manudir_i_ari
    print ("mánuðir árið " + ar + " eru " + str(manudir_i_ari))
    print ("meðalhiti er " + str(medalhiti))
    print ("\n")

file = open("vedurgogn.csv", "r")

ar = None
hitastig_ar_samtals = 0
manudir_i_ari = 0

for line in file:
    gogn = line.split(',')

    if (gogn[0] == "ar"):
        continue

    if (ar is None):
        ar = gogn[0]

    if (gogn[0] != ar):
        prenta(hitastig_ar_samtals, manudir_i_ari)
        ar = gogn[0]
        hitastig_ar_samtals = 0
        manudir_i_ari = 0
    
    hitastig_ar_samtals += float(gogn[2])
    manudir_i_ari += 1

#prenta núverandi ár sem er ekki búið
if (manudir_i_ari > 0):
    prenta(hitastig_ar_samtals, manudir_i_ari)

