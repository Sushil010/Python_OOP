from animals import Animals

class dog(Animals):
    def speak(self):
        print("WOOF")


class cat(Animals):
     def speak(self):
        print("MEOW")


Dog=dog("Green")
Cat=cat("Tom")

print(Dog.name)
print(Dog.alive)
Dog.Eat()
Dog.speak()



print(Cat.name)
print(Cat.alive)
Cat.walking()
Cat.speak()

