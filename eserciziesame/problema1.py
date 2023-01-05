 #Scrivere una funzione ricorsiva che, data una stringa s, 
 # restituisce vero se la stringa contiene la stessa quantità di cifre
 # numeriche e caratteri alfabetici, falso altrimenti. Nota:
 # ricordare i metodi isdigit() e isalpha() del tipo di dato strin Python.#

def ricorsionedigitalpha(s,d,a):
    if len(s)==0 and d==a:
        
        print("True ")
    elif len(s)==0 and d!=a: 
       
        print("False")
    else:
        if s[0].isdigit():
            
            ricorsionedigitalpha(s[1:],d+1,a)
            
        else:
            
            ricorsionedigitalpha(s[1:],d,a+1)

ricorsionedigitalpha("a1b2c34rògu310h",0,0)