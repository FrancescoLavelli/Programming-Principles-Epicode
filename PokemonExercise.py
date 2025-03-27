"""***Pokemon Exercise***
1.Create a Class Pokemon
2.Instance Attributes: Name, Health, Strenght
3.Add attack method
    must reduce opponent health
4.The Method print: ~"Pikachu strikes Charizard with {attack name} inflicting 15 Damage" 
5. Fight and print health to check
"""


# class Strength:
#     def __init__(self, physical=0, special=0, attack=0, defense=0):
#         self.physical = physical
#         self.special = special
#         self.attack = attack
#         self.defense = defense


class Pokemon:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, opponent, **kwargs):
        power = kwargs.get('power', 0)
        attack_type = kwargs.get('type', 'normal')

        print(f"{self.name.capitalize()} is attacking {opponent.name.capitalize()} using: {attack_type}, inflicting {power} Damage")

        health_left = opponent.health - power
        print(f"{opponent.name.capitalize()} {health_left} health")


""" prova a creare una instance fight cosi magari la health la dentro si modifica senza riazzerarsi
    in cui magari definisci un parametro fight.healt che va avantifino a che la healt self o dell'opponent e'  == 0
    prova a fare vulnerabilities & resistance, accuracy, defence
"""

# Usage
pikachu = Pokemon("pikachu", 330, 60)
charizard = Pokemon("charizard", 330, 60)

pikachu.attack(charizard, power=30, type='Electro Ball')
charizard.attack(pikachu, power=50, type='Claw Slash')
pikachu.attack(charizard, power=60, type='Thunderbolt')
charizard.attack(pikachu, power=70, type='Firebreath')
pikachu.attack(charizard, power=150, type='G-Max Volt Tackle')
charizard.attack(pikachu, power=210, type='G-Max Wildfire')
