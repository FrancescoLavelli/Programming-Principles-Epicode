import random
from PokemonEnhanced import (
    Type, MoveCategory, StatusEffect, Move, Pokemon, Battle, Ability, Intimidate
)

# Define some additional abilities


class Blaze(Ability):
    def __init__(self):
        super().__init__("Blaze", "Powers up Fire-type moves when HP is below 1/3")

    def on_attack(self, attacker, defender, move):
        if attacker.current_health <= attacker.max_health / 3 and move.type == Type.FIRE:
            return True, 150, f"{attacker.name}'s Blaze ability powered up its Fire-type move!"
        return True, 100, ""


class Static(Ability):
    def __init__(self):
        super().__init__("Static", "May paralyze on contact")

    def on_defend(self, attacker, defender, move):
        # Only physical moves trigger Static
        if move.category == MoveCategory.PHYSICAL and random.randint(1, 100) <= 30:
            status_msg = attacker.apply_status_effect(StatusEffect.PARALYSIS)
            if status_msg:
                return True, 100, f"{defender.name}'s Static ability {status_msg}"
        return True, 100, ""


# Create moves
thunderbolt = Move(
    name="Thunderbolt",
    type=Type.ELECTRIC,
    category=MoveCategory.SPECIAL,
    power=90,
    accuracy=100,
    status_effect=StatusEffect.PARALYSIS,
    status_chance=10
)

flamethrower = Move(
    name="Flamethrower",
    type=Type.FIRE,
    category=MoveCategory.SPECIAL,
    power=90,
    accuracy=100,
    status_effect=StatusEffect.BURN,
    status_chance=10
)

hydro_pump = Move(
    name="Hydro Pump",
    type=Type.WATER,
    category=MoveCategory.SPECIAL,
    power=110,
    accuracy=80
)

leaf_blade = Move(
    name="Leaf Blade",
    type=Type.GRASS,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=100,
    critical_rate=4  # Higher critical hit ratio
)

quick_attack = Move(
    name="Quick Attack",
    type=Type.NORMAL,
    category=MoveCategory.PHYSICAL,
    power=40,
    accuracy=100,
    priority=1  # Priority move, goes first
)

thunder_wave = Move(
    name="Thunder Wave",
    type=Type.ELECTRIC,
    category=MoveCategory.STATUS,
    power=0,
    accuracy=90,
    status_effect=StatusEffect.PARALYSIS,
    status_chance=100
)

# Create Pokemon
pikachu = Pokemon(
    name="Pikachu",
    types=[Type.ELECTRIC],
    health=274,
    attack=229,
    defense=174,
    sp_attack=218,
    sp_defense=196,
    speed=306,
    ability=Static(),
    moves=[thunderbolt, quick_attack, thunder_wave]
)

charizard = Pokemon(
    name="Charizard",
    types=[Type.FIRE, Type.FLYING],
    health=360,
    attack=267,
    defense=254,
    sp_attack=348,
    sp_defense=268,
    speed=299,
    ability=Blaze(),
    moves=[flamethrower, quick_attack]
)

blastoise = Pokemon(
    name="Blastoise",
    types=[Type.WATER],
    health=362,
    attack=264,
    defense=298,
    sp_attack=295,
    sp_defense=339,
    speed=254,
    moves=[hydro_pump, quick_attack]
)

sceptile = Pokemon(
    name="Sceptile",
    types=[Type.GRASS],
    health=342,
    attack=275,
    defense=251,
    sp_attack=347,
    sp_defense=251,
    speed=351,
    moves=[leaf_blade, quick_attack]
)

# Create teams
player_team = [pikachu, blastoise]
opponent_team = [charizard, sceptile]

# Create battle
battle = Battle(player_team, opponent_team)

# Simulate a battle
print("===== POKEMON BATTLE SIMULATION =====\n")
print(f"Player's team: {', '.join(p.name for p in player_team)}")
print(f"Opponent's team: {', '.join(p.name for p in opponent_team)}\n")

print(
    f"Battle begins! {battle.active_player_pokemon.name} vs {battle.active_opponent_pokemon.name}\n")

# Turn 1
print("\n----- Player selects Thunderbolt, Opponent selects Flamethrower -----")
messages = battle.execute_turn(thunderbolt, flamethrower)
for msg in messages:
    print(msg)

# Turn 2
print("\n----- Player selects Quick Attack, Opponent selects Quick Attack -----")
messages = battle.execute_turn(quick_attack, quick_attack)
for msg in messages:
    print(msg)

# Turn 3
print("\n----- Player selects Thunder Wave, Opponent selects Flamethrower -----")
messages = battle.execute_turn(thunder_wave, flamethrower)
for msg in messages:
    print(msg)

# Turn 4
print("\n----- Player switches to Blastoise -----")
messages = battle.switch_pokemon(is_player=True, index=1)
for msg in messages:
    print(msg)

# Turn 5
print("\n----- Player selects Hydro Pump, Opponent selects Flamethrower -----")
messages = battle.execute_turn(hydro_pump, flamethrower)
for msg in messages:
    print(msg)

# Check if battle is over
is_over, winner_message = battle.is_battle_over()
if is_over:
    print(f"\n{winner_message}")
else:
    print("\nThe battle continues...")

print("\n===== ENHANCED FEATURES DEMONSTRATED =====")
print("1. Type effectiveness (Water > Fire, Electric > Water)")
print("2. Status effects (Paralysis, Burn)")
print("3. Critical hits (Leaf Blade has higher critical hit ratio)")
print("4. Turn-based battle system with initiative based on Speed and move Priority")
print("5. Pokemon abilities (Static, Blaze)")
print("6. Team battles with switching")
print("7. STAB (Same Type Attack Bonus)")
