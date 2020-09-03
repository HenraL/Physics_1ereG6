from time import sleep
import math
# def delta:
#     print ("∆")
main=input("(cc)calculer des charges; (dfftn) distinguer fission, fusion, transformation nucléaire; (ppem) principaux éléments chimiques qui constituent la matière organique des êtres vivants; (rdp) remonter dans le passé; (cd) calculer la demi-vie; (Lr) le rayonnement Solaire")
if main=="cc":
    Z=int(input("cc\nA\n X\nZ\nentrez le numéro atomique Z:"))
    A=int(input("Entrez le nombre de nucléons A:"))
    X=input("Entrez le symbole de l'élément X (exemple: H, He, ...):")
    print (" L'atome {}, a {} protons, {}-{}={} neutrons, {} électrons.".format(X, Z, A, Z, A-Z, Z))
elif main=="dfftn":
    print ("dfftn\n")
print ("(f) formules")
sleep (5)