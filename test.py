class A:
    def __init__(self, n='Rahul'):
        self.name = n

class B(A):
    def __init__(self, roll, n='Rahul'):  # Corrected parameter order
        self.roll = roll
        super().__init__(n)

object = B(23)
print(object.name)
print(object.roll)

