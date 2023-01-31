class archiviomusicale:
    def __init__(self):
        self.archivio=[]

    def nuovaCoppia(self,brano,id):
        coppia=[brano,id]
        self.archivio.append(coppia)

    def getCanzoneFromId(self,id):
        for i in range(0,len(self.archivio)):
            if self.archivio[i][1]==id:
                return self.archivio[i][0]
            else:
                return "non trovata"


class archiviomusicaleConImg(archiviomusicale):

    def __init__(self):
        archiviomusicale.__init__(self)
        self.immagine=""

    def nuovaCoppiaImmagine(self, brano, id ,immagine):
        coppia = [brano, id,immagine]
        self.archivio.append(coppia)

    def getCanzoni(self):
        for i in range(0,len(self.archivio)):
            print(self.archivio[i][0],self.archivio[i][1],self.archivio[i][2])




a1=archiviomusicaleConImg()
a1.nuovaCoppiaImmagine("canzone1",1,"immagine1")
a1.nuovaCoppiaImmagine("canzone2",2,"immagine2")
a1.nuovaCoppiaImmagine("canzone3",3,"immagine3")

print(a1.getCanzoni())
print(a1.getCanzoneFromId(1))
