#Scrivere una funzione ricorsiva che, data una stringa s, restituisce come risultato una stringa ottenuta elimanando
# da s tutti i caratteri ripetuti consecutivamente, tranne il primo (Es.: se s = "aaabbcccc" la funzione deve restituire "abc";
# se s = "ababcc" la funzione deve restituire "ababc"

def elimina_ripetizioni(s):
  if len(s) == 0:
    return ""
  if len(s) == 1:
    return s
  if s[0] == s[1]:
    return elimina_ripetizioni(s[1:])
  return s[0] + elimina_ripetizioni(s[1:])

    
    
    
print(elimina_ripetizioni("ababcc"))