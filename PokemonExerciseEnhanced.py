"""***Pokemon Exercise***
1.Create a Class Pokemon
2.Instance Attributes: Name, Health, Strenght
3.Add attack method
    must reduce opponent health
4.The Method print: ~"Pikachu strikes Charizard with {attack name} inflicting 15 Damage" 
5. Fight and print health to check
"""


class Pokemon:
    def __init__(self, name, health, element_resistance, category_resistance, vulnerability):
        self.name = name
        self.health = health
        self.element_resistance = {
            element: resistance
            for element, resistance in element_resistance.items()
        }
        self.category_resistance = {
            category: resistance
            for category, resistance in category_resistance.items()
        }
        self.vulnerability = {
            vulnerability: weakness
            for vulnerability, weakness in vulnerability.items()
        }
        self.total_damage_taken = 0

    def attack(self, opponent, move):
        # Damage
        damage = move.power
        # Damage Reduction
        if move.element in self.element_resistance:
            element_resistance_value = self.element_resistance[move.element]
        else:
            element_resistance_value = 0

        if move.category in self.category_resistance:
            category_resistance_value = self.category_resistance[move.category]
        else:
            category_resistance_value = 0

        damage_reduction = element_resistance_value + category_resistance_value

        # Damage Enhancement
        if opponent.vulnerability != move.element:
            opponent.total_damage_taken = - damage + damage_reduction
            health_left = opponent.health + opponent.total_damage_taken
            print(f"{self.name.capitalize()} is attacking {opponent.name.capitalize()} using: {move.name}, inflicting {move.power} {move.element} Damage")

        else:
            health_left = opponent.health - damage*2 + damage_reduction
            print(f"{self.name.capitalize()} is attacking {opponent.name.capitalize()} using: {move.name}, inflicting {move.power*2} {move.element} Damage")

        print(
            f"{opponent.name.capitalize()} absorbs {element_resistance_value} {move.element} damage")
        print(
            f"{opponent.name.capitalize()} absorbs {category_resistance_value} {move.category} damage")
        print(f"{opponent.name.capitalize()} {health_left} Health")


""" prova a creare una instance fight cosi magari la health la dentro si modifica senza riazzerarsi
    in cui magari definisci un parametro fight.healt che va avantifino a che la healt self o dell'opponent e'  == 0
    prova a fare vulnerabilities & resistance, accuracy, defence
    capire come si fa a dare un valore a element_resistance e category resistance, se metti i nomi puoi hardcodare un valore fisso ma se tu volessi metterlo in base al pokemon come si fa?
"""

# Creating Pokemon
pikachu = Pokemon(
    name="Pikachu",
    health=330,
    element_resistance={
        "Electric": 50,
        "Fire": 25,
        "Ground": 0
    },
    category_resistance={
        "Special": 10,
        "Physical": 0,
    },
    vulnerability={
        "Water": 50,
    }
)
charizard = Pokemon(
    name="Charizard",
    health=330,
    element_resistance={
        "Fire": 50,
        "Ground": 20
    },
    category_resistance={
        "Special": 10,
        "Physical": 10,
    },
    vulnerability={
        "Fairy": 20
    }
)

# initialising attack moves


class Move:
    def __init__(self, name, element, category, power, accuracy):
        self.name = name
        self.element = element
        self.category = category
        self.power = power
        self.accuracy = accuracy


# creating attacks

electro_ball = Move("Electro Ball", "Electric", "Special", 100, 100)
water_pulse = Move("Water Pulse", "Water", "Special", 60, 100)
salt_cure = Move("Salt Cure", "Rock", "Physical", 40, 100)
grass_Pledge = Move("Grass Pledge", "Grass", "Special", 80, 100)
belch = Move("Belch", "Poison", "Special", 120, 90)
bone_club = Move("Bone Club", "Ground", "Physical", 65, 85)
bounce = Move("Bounce", "Flying", "Special", 85, 85)
close_combat = Move("Close Combat", "Fighting", "Physical", 120, 100)
dazzling_gleam = Move("Dazzling Gleam", "Fairy", "Special", 80, 100)
gmax_volt_tackle = Move("G-Max Volt Tackle", "Electric", "G-MAX", 150, 100)
gmax_wildfire = Move("G-MAX Wildfire", "Fire", "G-MAX", 210, 100)

# to print attributes
# print(bounce.__dict__)
# to loop through
for attr, value in pikachu.__dict__.items():
    print(f"{attr}: {value}")
# for attr, value in electro_ball.__dict__.items():
#     print(f"{attr}: {value}")

pikachu.attack(charizard, electro_ball)
charizard.attack(pikachu, water_pulse)
for attr, value in pikachu.__dict__.items():
    print(f"{attr}: {value}")
pikachu.attack(charizard, dazzling_gleam)
charizard.attack(pikachu, gmax_wildfire)

for attr, value in pikachu.__dict__.items():
    print(f"{attr}: {value}")
