def prenta(hitastig_ar_samtals, manudir_i_ari, max_hitastig, min_hitastig):
    medalhiti = hitastig_ar_samtals / manudir_i_ari
    print ("mánuðir árið " + ar + " eru " + str(manudir_i_ari))
    print ("meðalhiti er " + str(medalhiti))
    print("hámarkshitastig er " + str(max_hitastig))
    print("lágmarkshitastig er " + str(min_hitastig))
    print ("\n")

file = open("vedurgogn.csv", "r")

ar = None
hitastig_ar_samtals = 0
manudir_i_ari = 0
max_hitastig = -100
min_hitastig = 100

for line in file:
    gogn = line.split(',')

    if (gogn[0] == "ar"):
        continue

    if (ar is None):
        ar = gogn[0]

    if (gogn[0] != ar):
        prenta(hitastig_ar_samtals, manudir_i_ari, max_hitastig, min_hitastig)
        ar = gogn[0]
        hitastig_ar_samtals = 0
        manudir_i_ari = 0
        max_hitastig = -100
        min_hitastig = 100
    
    hitastig = float(gogn[2])
    hitastig_ar_samtals += hitastig
    manudir_i_ari += 1

    if (hitastig > max_hitastig):
        max_hitastig = hitastig
    if (hitastig < min_hitastig):
        min_hitastig = hitastig


#prenta núverandi ár sem er ekki búið
if (manudir_i_ari > 0):
    prenta(hitastig_ar_samtals, manudir_i_ari, max_hitastig, min_hitastig)

