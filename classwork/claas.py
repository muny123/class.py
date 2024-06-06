class Dog :
    number = 0
    #_protected = "i ama protected variable"
    
    def __init__(self, name):
        self.name = name
        Dog.number += 1
        self.__dognumber  = Dog.number
         
        
    # def get_dognumber():
        # return self.__dognumber
        
    @property
    def dognumber(self):
        return self.dognumber 
        
    def bark(self):  #method
        print(f"{self.name} say woof!")
    
    
bingo = Dog("bingo")
print(bingo.dognumber)
    