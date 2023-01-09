#Problema 1 Scrivere una funzione ricorsiva che, data una stringa s, restituisce una nuova stringa ottenuta da s aggiungendo 
# il carattere '.' dopo ogni carattere alfabetico o numerico.
# (Nota: il tipo di dato string in Python possiede gli operatori isalpha : string!boole isdigit : string!boolche,
# applicati a una stringa, verificano se essa è formata, rispettivamente, da soli caratteri alfabetici o numerici)

def add_period(s):
  if not s:
    return s
  if s[0].isalpha() or s[0].isdigit():
    return s[0] + "." + add_period(s[1:])
  return s[0] + add_period(s[1:])

print(add_period("acwegui-,h123ehrgoiò"))