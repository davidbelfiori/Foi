
#------ PROBLEMA 11 ------#
def contaCar(S):  
# @param s: string
# @return int
  n = 0
  for i in range(0, len(s)):
    if not(s[i].isdigit()):
      n+=1
  return n

#print contaCar(s)



      