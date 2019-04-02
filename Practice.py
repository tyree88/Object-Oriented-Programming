#Practice

class Dog():

    def __init__(self,name,breed,fur):
        self.name = name
        self.breed = breed
        self.fur = fur

    def show(self):
        fur = self.fur
        if fur is True:
            print("I am a dope poodle")
        else:
            print("I am some other dog")

    
    def __str__(self):
        return "this is your str method and you are a "+ self.breed


class FemaleDog(Dog):

    def __init__(self):
        pass
    
    


def main():
    tyree = Dog('Tyree','poodly',False)
    print(tyree)
    tyree.show()
    print(Dog.show(tyree))
    

main()
