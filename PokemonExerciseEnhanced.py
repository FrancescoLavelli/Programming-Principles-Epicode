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
        self.damage_history = []
        self.total_damage_taken = 0

    def attack(self, opponent, move):

        # Damage Reduction
        if move.element in opponent.element_resistance:
            element_resistance_value = opponent.element_resistance[move.element]
        else:
            element_resistance_value = 0

        if move.category in opponent.category_resistance:
            category_resistance_value = opponent.category_resistance[move.category]
        else:
            category_resistance_value = 0

        damage_reduction = element_resistance_value + category_resistance_value

        # Total Damage
        damage = move.power - damage_reduction

        # Dealing Damage

        if move.element in opponent.vulnerability:
            weakness = opponent.vulnerability[move.element]
            health_left = opponent.health - \
                opponent.total_damage_taken - damage - weakness

            if health_left <= 0:
                print(f"{opponent.name} has been defeted!")
                opponent.damage_history.clear()
                opponent.total_damage_taken = 0
                return
            else:
                print(
                    f"{self.name.capitalize()} is attacking {opponent.name.capitalize()} using: {move.name}")
                print(
                    f"{opponent.name.capitalize()} is vulnerable to {move.element}.")
                print(
                    f"{self.name.capitalize()} inflicting {(move.power+weakness)} Damage")

        else:
            health_left = opponent.health - opponent.total_damage_taken - damage

            if health_left <= 0:
                print(f"{opponent.name} has been defeted!")
                opponent.damage_history.clear()
                opponent.total_damage_taken = 0
                return
            else:
                print(f"{self.name.capitalize()} is attacking {opponent.name.capitalize()} using: {move.name}, inflicting {move.power} {move.element} Damage")

        # Damage update
        opponent.damage_history.append(damage)
        opponent.total_damage_taken += damage

        print(
            f"{opponent.name.capitalize()} absorbs {element_resistance_value} {move.element} damage")
        print(
            f"{opponent.name.capitalize()} absorbs {category_resistance_value} {move.category} damage")
        print(f"{opponent.name.capitalize()} {health_left} Health")
        print(
            f"***********************************{opponent.damage_history}")
        print(
            f"***********************************{opponent.total_damage_taken}")
        print(f"@@@@@@@@@@@{damage}")
        print(f"@@@@@@@{damage_reduction}")


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
        "Physical": 30,
    },
    vulnerability={
        "Water": -50,
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
# for attr, value in pikachu.__dict__.items():
#     print(f"{attr}: {value}")
# for attr, value in electro_ball.__dict__.items():
#     print(f"{attr}: {value}")

# pikachu.attack(charizard, electro_ball)
pikachu.attack(charizard, bone_club)
charizard.attack(pikachu, water_pulse)
pikachu.attack(charizard, dazzling_gleam)
charizard.attack(pikachu, salt_cure)
pikachu.attack(charizard, belch)
charizard.attack(pikachu, gmax_wildfire)
pikachu.attack(charizard, gmax_volt_tackle)
charizard.attack(pikachu, close_combat)
pikachu.attack(charizard, grass_Pledge)
charizard.attack(pikachu, electro_ball)
