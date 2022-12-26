class date:
    def __init__(self):
        self.day=1
        self.month=1
        self.year=0
    
    #getter
    def printDate(self):
        print (self.day,"/",self.month,"/",self.year)
    #setter
    def setDate(self,day,month,year):
        if day>=1 and day<=31 and month>=1 and month<=12 and year>0:
           
            self.day=day
            self.month=month
            self.year=year
        else:
            print ("Date not valid")
            
    #compare     
         