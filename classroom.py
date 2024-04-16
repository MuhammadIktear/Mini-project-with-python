class level:
    def __init__(self,lvl) -> None:
        self.lvl=lvl
    
class student(level):
    def __init__(self, lvl , name, roll) -> None:
        self.name=name
        self.roll=roll
        super().__init__(lvl)
    def details(self):
        print(f"Roll: {self.roll}")
        print(f"Name: {self.name}")


lvl = int(input("Enter student level: "))
name = input("Enter student name: ")
roll = int(input("Enter student roll number: "))
student1 = student(lvl, name, roll)
print(f"level: {student1.lvl}")
student1.details()
