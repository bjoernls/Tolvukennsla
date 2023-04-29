file = open("vedurgogn.txt", "r")


ar = None
hitastig_ar_samtals = 0
manudir_i_ari = 0
for line in file:
    gogn = line.split(',')

    if (gogn[0] == "stod"):
        continue

    if (ar is None):
        ar = gogn[1]

    
    if (gogn[1] != ar):
        
        medaltal = hitastig_ar_samtals / manudir_i_ari
        print ("mánuðir árið " + ar + " eru " + str(manudir_i_ari))
        print ("meðaltal hitastigs er " + str(medaltal))
        print ("\n")
        ar = gogn[1]
        hitastig_ar_samtals = 0
        manudir_i_ari = 0
    
    hitastig_ar_samtals += float(gogn[3])
    manudir_i_ari += 1

medaltal = hitastig_ar_samtals / manudir_i_ari
print ("mánuðir árið " + ar + " eru " + str(manudir_i_ari))
print ("meðaltal hitastigs er " + str(medaltal))
print ("\n")