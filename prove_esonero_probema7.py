#Scrivere una funzione Python che, data una stringa s, 
#restituisce una nuova stringa formata dai soli caratteri 
#di s che si trovano in posizione pari.

a="BLFDDJ03R10H501Z"
s=""
for i in range (0,len(a),2):
  
  s+=a[i]