class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all=[]

    def __init__(self, name, pet_type="dog", owner=None):
        self.name = name
        self.pet_type = self.valid_pet_type(pet_type)
        self.owner = owner
        self.all.append(self)

    def valid_pet_type(self,pet_type):
        if pet_type in self.PET_TYPES:
            return pet_type
        else:
            raise Exception("Try again!")
        
    


class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception("Try again")       
    
    def get_sorted_pets(self):
        # self.pets().sort(key=lambda e: e.name)
        return sorted(self.pets(), key=lambda e: e.name)

