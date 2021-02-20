""" 
Single Reposibility Principle (SRP)

class should have only one reason to change it
"""

# Ex
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def save(self, animal: Animal):
        pass

""" 
The animal class violate the SRP

Animal class has two responsibility
1. Animal property management
2. Animal database management

"""