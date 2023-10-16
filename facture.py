#Programme qui demande à l’utilisateur le nombre de photocopies effectuées et qui affiche la facture correspondante.
np=float(input("Entrer votre npmbre de photocopie : "))
f=0
if(np>=10):
    f=np*0.30
    print(f"La facture est {f}")
elif(np>10 and np<=30):
    f= 10*0.30 + (np-10)*0.25
    print(f"La facture est {f}")
else:
    f= 10*0.30 + 20*0.25 + (np-30)*0.20
    print(f"La facture est {f}")


