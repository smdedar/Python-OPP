class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def gender(self,gender):
        print(f'Person Name is {self.name}. Age {self.age} & Gender {gender}')

obj = Person("Dedar",20)

obj.gender("Female")