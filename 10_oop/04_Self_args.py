class Chaicup:
    size = 150

    def describe(self):
        print(f"This chai cup is {self.size}ml")

chai_cup = Chaicup()
chai_cup.describe()
Chaicup.describe(chai_cup)

cup_two = Chaicup()
cup_two.size = 100
cup_two.describe()