#Problema 12. 
# Scrivere una funzione ricorsivache, 
# data una stringa s, verifica se la stringa è formata da due metà uguali
# tra loro (ovvero verifica se s== s1+s2, con s1==s2).
# Se la lunghezza della stringa è dispari, 
# il carattere centrale va escluso dal confronto.
# Nota:nel definire la funzione,l'operatore Python di uguaglianza == può essere applicato
# solo a stringhe di lunghezza ≤1 . 

def probl(s,s1,s2):
    if  s1==s2:
        return True
    elif s1!=s2:
        return False
    else:
        if len(s)%2==0:
            
            probl(s,s[len(s)/2+1:len(s)/2],s[len(s)/2:len(s)/2+1])
        #else:
         #   probl(s,s[:len(s)//2],s[len(s)//2:])



def is_half_palindrome(s):
  # Caso base: se la stringa è vuota o ha un solo carattere, è un palindromo
    if len(s) <= 1:
        return True
  
  # Se la stringa ha una lunghezza dispari, escludi il carattere centrale dal confronto
    
  
  # Verifica se la prima metà della stringa è uguale alla seconda
    return s[:len(s)//2] == s[len(s)//2:]
    

print(is_half_palindrome("assoasso"))

