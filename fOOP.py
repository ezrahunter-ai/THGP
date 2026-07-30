class Year2030:
    a = "Welcome 2030!"
    b = "The future is here."
    c = "Let's embrace the changes."
    d = "bye bye 2026!"

    def greet_all(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)


class student:
    def __init__(self, name, grade, school):
        self.name = name
        self.grade = grade
        self.school = school

    def introduce(self):
        print(f"Hi, my name is {self.name}. I'm in {self.grade} grade at {self.school}.")


# Creating 4 students, each in a different grade and school
ezra = student("Ezra", "9th", "SLA")
hunter = student("Hunter", "10th", "Central")
alex = student("Alex", "11th", "Frankford")
tya = student("Tya", "12th", "Northeast")

# Test it out
ezra.introduce()
hunter.introduce()
alex.introduce()
tya.introduce()









            