#Problema 1. Scrivere una funzione ricorsiva che, data una stringa s, restituisce come risultato una stringa formata da tutti 
# i caratteri di s separati tra loro da uno spazio bianco.Esempio: data la stringa "abcd", la funzione deve restituire la stringa
# "a b c d"

def ricorsione (s):
  if not s: 
    return s
  
  return s[0]+" "+ricorsione(s[1:])

print(ricorsione("abcd"))