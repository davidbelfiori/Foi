class car:
    def __init__(self,efficiency):
        self.efficiency = efficiency
        self.fuel=0

    def addFuel(self,qta):
        self.fuel+=qta
    
    def getFuel(self):
        return self.fuel
    
    def drive(self,km):
        self.fuel-=self.efficiency
        if self.fuel<0:
            self.fuel=0
            print("ndo vai che non ce sta la benza")