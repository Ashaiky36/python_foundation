class Dog:
    def __init__(dog, name, breed):
        dog.name = name
        dog.breed = breed

    def bark(dog):
        print("This is my dog, its name is " + dog.name + " and its breed is " + dog.breed)    

d1 = Dog("whisker", "Labrador Retriever") 
d1.bark()