class Vehicle:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
        print("move!@#!#!#!@#")

class Car(Vehicle): 
    #Here we can actually override certain functions in the superclass while inheriting the other characteristics
    def __init__(self, brand, model,wheels) -> None: #If we want to add another characteristics, we make another init funciton
        super().__init__(brand, model)
        self.wheels = wheels
    def move(self):
        print("Driving")
        print("I have this many wheels: " +str(self.wheels))

car1 = Car("ford","f150",4)
car1.move()