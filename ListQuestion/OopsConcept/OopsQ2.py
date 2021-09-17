class Computer:

    def __init__(self,name,place):
        self.name = 'Akchat'
        self.place = 'Gurgoan'
        
    def update(self):
        self.name = "Anjali"
    


C1 = Computer()
C1.update()
C2 = Computer() #object are created and memory are assign according to size of vaiable. Who will assign memory that is "Constuctor"
C1.name = "Chauhan"
C1.place = "GGN"
C1.update()
print(C1.name,C1.place)