class SportPerson:
    def __init__(self,spname,nm):
        self.spname=spname
        self.nm=nm
    def display(self):
        print(self.spname,self.nm)

class Actor:
    def __init__(self,nm,na):
        self.nm=nm
        self.na=na
    def display(self):
        print(self.nm,self.na)


class Personal(Actor,SportPerson):
    def __init__(self,name,nm,na,spname,nms):
        super().__init__(nm,na)
        SportPerson.__init__(self,spname,nms)
        self.name=name
    def display(self):
        super().display()
        SportPerson.display(self)
        print(self.name)

p1=Personal("deepika",100,5,"cricket",120)
p1.display()


