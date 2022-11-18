#Problema 8
#Scrivere una funzione Python che, data una stringa s,
#restituisce una nuova stringa formata da tanti caratteri * quanti sono i caratteri alfabetici presenti in s.
#Nota: in Python, data una qualunque stringa x, l'operatore x.isalpha() del tipo di dato str restituisce 
#True se la stringa x e' formata solo da caratteri alfabetici, False altrimenti.
#-------------------------------------------------------------------------------------------------------------------------#

str="BLFDDJ03R10H501Z"
s=""
for i in range (0,len(str)):
  if str[i].isalpha():
    s+="*"
  
    

