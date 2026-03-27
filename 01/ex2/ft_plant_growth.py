class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
    
    def age_up(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(plant.get_info())
    
    initial_height = plant.height

    for _ in range(6):
        plant.grow()
        plant.age_up()

    print("=== Day 7 ===")
    print(plant.get_info())
    
    growth = plant.height - initial_height
    print(f"Growth this week: +{growth}cm")
