class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"My name is {self.name}")

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print(f"Rodger is a {Rodger.attr1}")
print(f"Tommy is also a {Tommy.attr1}")

# Accessing instance attributes
Rodger.speak()
Tommy.speak()
