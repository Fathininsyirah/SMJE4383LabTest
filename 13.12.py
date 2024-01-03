#new class 13/12

class HotDrink:
    def __init__(self, type, temperature):
        self.type: type
        self.temperature = temperature

    def display_info(self):
        return f"type: {self.type}, temperature: {self.temperature}"


class Coffee(HotDrink):
    def __init__(self, name, temperature, coffeetype):
        super().__init__(name, temperature)
        self.coffeetype = coffeetype

    def describe(self):
        print(f"Coffee Type:\t {self.coffeetype}")
        super().describe()
        print("")


class Tea(HotDrink):
    def __init__(self, name, temperature, teatype):
        super().__init__(name, temperature)
        self.teatype = teatype

    def describe(self):
        print(f"Tea Type:\t {self.teatype}")
        super().describe()
        print("")

class HotChocolate(HotDrink):
    def __init__(self, name, temperature, chocolatetype):
        super().__init__(name, temperature)
        self.chocolatetype = chocolatetype

    def describe(self):
        print(f"Chocolate Type:\t {self.chocolatetype}")
        super().describe()
        print("")


# Create instances of each hot drink
coffee = Coffee("Coffee", "Hot", "Espresso")
tea = Tea("Tea", "Warm", "Green Tea")
hot_chocolate = HotChocolate("Hot Chocolate", "Very Hot", "Dark Chocolate")

# Demonstrate polymorphic behavior by calling the describe() method for each drink
coffee.describe()
tea.describe()
hot_chocolate.describe()