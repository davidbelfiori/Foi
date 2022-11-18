s="hello mr John"
tfs="mr" 

def A (s,tfs): 
#@param s: string 
#@param tfs: string
  for i in range(0,len(s)):
   for j in range(0,len(tfs)):
     if s[i]==tfs[j]:
      print " corrispondenza trovata"
      print s[i],tfs[j]
     else : 
       print "nessuna corrsipondenza"
      
      
def  B(s,tfs): 
#@param s: string 
#@param tfs: string
  for i in range(0,len(s)):
   for j in range(0,len(tfs)):
     if s[i]==tfs[j]:
      print " corrispondenza trovata"
      print i 
      print s[i],tfs[j]

A(s,tfs)
#B(s,tfs)



                               