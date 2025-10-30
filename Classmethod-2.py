class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "corn"])

    def __str__(self):
        return f"Pizza with {' and '.join(self.ingredients)}"

p1 = Pizza.margherita()
print(p1)
