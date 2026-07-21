#display text 
print("THis is python")
print("hello world")
class Myself:
    def __init__(self, age, name):
        self._age = age
        self.name = name
        self._capacity = None

    @property
    def age(self):
        return self._age

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
        if value < 17:
            raise ValueError("Student should be older")
        if value < 17:
            raise ValueError("Student should be older")
        self._capacity = value

student = [
    Myself(18, "martin"),
    Myself(16, "amara"),
]