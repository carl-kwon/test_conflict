class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_person(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

a = person("John", 30, "New York")