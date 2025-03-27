class Pokemon:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def print_stats(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


# Creating an instance with arbitrary attributes
pikachu = Pokemon(name="Pikachu", health=10, element_resistance=10,
                  category_resistance=10, vulnerability="Water")

pikachu.print_stats()


class Pokemon:
    def __init__(self, name, health, element_resistance, category_resistance, vulnerability):
        self.name = name
        self.health = health
        # Store element resistances as a dictionary with element and resistance value
        self.element_resistance = {
            element: resistance
            for element, resistance in element_resistance.items()
        }
        self.category_resistance = category_resistance
        self.vulnerability = vulnerability

    def check_element_resistance(self, move):
        # Check if the move's element has a resistance in the Pokemon's resistances
        if move.element in self.element_resistance:
            # Get the resistance value for this element
            resistance_value = self.element_resistance[move.element]

            # Calculate damage reduction or multiplier
            # Lower values mean more resistance, higher values mean less resistance
            damage_multiplier = 1 - (resistance_value / 100)

            print(f"{self.name}'s resistance to {move.element}: {resistance_value}%")
            return damage_multiplier
        else:
            print(f"No specific resistance to {move.element}")
            return 1  # Full damage if no specific resistance


class Move:
    def __init__(self, name, element, category, power, accuracy):
        self.name = name
        self.element = element
        self.category = category
        self.power = power
        self.accuracy = accuracy


# Example usage
# Create a Pokemon with element resistances
pikachu = Pokemon(
    name="Pikachu",
    health=100,
    element_resistance={
        "Electric": 50,  # 50% resistance to Electric
        "Water": 25,     # 25% resistance to Water
        "Ground": 0      # No resistance to Ground
    },
    category_resistance={},
    vulnerability=[]
)

# Create some moves
thunder_move = Move("Thunder", "Electric", "Special", 110, 70)
water_gun = Move("Water Gun", "Water", "Special", 40, 100)
earthquake = Move("Earthquake", "Ground", "Physical", 100, 100)

# Check resistances
print("\nChecking Thunder Move:")
thunder_damage_multiplier = pikachu.check_element_resistance(thunder_move)

print("\nChecking Water Gun Move:")
water_gun_damage_multiplier = pikachu.check_element_resistance(water_gun)

print("\nChecking Earthquake Move:")
earthquake_damage_multiplier = pikachu.check_element_resistance(earthquake)
