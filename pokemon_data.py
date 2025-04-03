from typing import Dict, List, Any
import random
from PokemonEnhanced import Type, MoveCategory, StatusEffect, Move, Pokemon

# Pokemon species data
# Format: {"species_name": {"types": [...], "base_stats": {...}, "possible_moves": [...], ...}}
POKEMON_DATA = {
    "Bulbasaur": {
        "types": [Type.GRASS, Type.POISON],
        "base_stats": {
            "health": 45,
            "attack": 49,
            "defense": 49,
            "sp_attack": 65,
            "sp_defense": 65,
            "speed": 45
        },
        "possible_moves": ["Tackle", "Growl", "Vine Whip", "Razor Leaf", "Solar Beam", "Sleep Powder", "Poison Powder"],
        "evolution": {"level": 16, "evolves_to": "Ivysaur"}
    },
    "Ivysaur": {
        "types": [Type.GRASS, Type.POISON],
        "base_stats": {
            "health": 60,
            "attack": 62,
            "defense": 63,
            "sp_attack": 80,
            "sp_defense": 80,
            "speed": 60
        },
        "possible_moves": ["Tackle", "Growl", "Vine Whip", "Razor Leaf", "Solar Beam", "Sleep Powder", "Poison Powder"],
        "evolution": {"level": 32, "evolves_to": "Venusaur"}
    },
    "Venusaur": {
        "types": [Type.GRASS, Type.POISON],
        "base_stats": {
            "health": 80,
            "attack": 82,
            "defense": 83,
            "sp_attack": 100,
            "sp_defense": 100,
            "speed": 80
        },
        "possible_moves": ["Tackle", "Growl", "Vine Whip", "Razor Leaf", "Solar Beam", "Sleep Powder", "Poison Powder", "Petal Dance", "Frenzy Plant"],
        "evolution": None
    },
    "Charmander": {
        "types": [Type.FIRE],
        "base_stats": {
            "health": 39,
            "attack": 52,
            "defense": 43,
            "sp_attack": 60,
            "sp_defense": 50,
            "speed": 65
        },
        "possible_moves": ["Scratch", "Growl", "Ember", "Flamethrower", "Fire Spin", "Dragon Rage", "Slash"],
        "evolution": {"level": 16, "evolves_to": "Charmeleon"}
    },
    "Charmeleon": {
        "types": [Type.FIRE],
        "base_stats": {
            "health": 58,
            "attack": 64,
            "defense": 58,
            "sp_attack": 80,
            "sp_defense": 65,
            "speed": 80
        },
        "possible_moves": ["Scratch", "Growl", "Ember", "Flamethrower", "Fire Spin", "Dragon Rage", "Slash"],
        "evolution": {"level": 36, "evolves_to": "Charizard"}
    },
    "Charizard": {
        "types": [Type.FIRE, Type.FLYING],
        "base_stats": {
            "health": 78,
            "attack": 84,
            "defense": 78,
            "sp_attack": 109,
            "sp_defense": 85,
            "speed": 100
        },
        "possible_moves": ["Scratch", "Growl", "Ember", "Flamethrower", "Fire Spin", "Dragon Rage", "Slash", "Fire Blast", "Wing Attack", "Air Slash", "Heat Wave", "Blast Burn"],
        "evolution": None
    },
    "Squirtle": {
        "types": [Type.WATER],
        "base_stats": {
            "health": 44,
            "attack": 48,
            "defense": 65,
            "sp_attack": 50,
            "sp_defense": 64,
            "speed": 43
        },
        "possible_moves": ["Tackle", "Tail Whip", "Water Gun", "Bubble", "Bite", "Hydro Pump", "Skull Bash"],
        "evolution": {"level": 16, "evolves_to": "Wartortle"}
    },
    "Wartortle": {
        "types": [Type.WATER],
        "base_stats": {
            "health": 59,
            "attack": 63,
            "defense": 80,
            "sp_attack": 65,
            "sp_defense": 80,
            "speed": 58
        },
        "possible_moves": ["Tackle", "Tail Whip", "Water Gun", "Bubble", "Bite", "Hydro Pump", "Skull Bash"],
        "evolution": {"level": 36, "evolves_to": "Blastoise"}
    },
    "Blastoise": {
        "types": [Type.WATER],
        "base_stats": {
            "health": 79,
            "attack": 83,
            "defense": 100,
            "sp_attack": 85,
            "sp_defense": 105,
            "speed": 78
        },
        "possible_moves": ["Tackle", "Tail Whip", "Water Gun", "Bubble", "Bite", "Hydro Pump", "Skull Bash", "Flash Cannon", "Hydro Cannon"],
        "evolution": None
    },
    "Pikachu": {
        "types": [Type.ELECTRIC],
        "base_stats": {
            "health": 35,
            "attack": 55,
            "defense": 40,
            "sp_attack": 50,
            "sp_defense": 50,
            "speed": 90
        },
        "possible_moves": ["Thunder Shock", "Growl", "Quick Attack", "Thunder Wave", "Thunderbolt", "Thunder", "Agility"],
        "evolution": {"item": "Thunder Stone", "evolves_to": "Raichu"}
    },
    "Raichu": {
        "types": [Type.ELECTRIC],
        "base_stats": {
            "health": 60,
            "attack": 90,
            "defense": 55,
            "sp_attack": 90,
            "sp_defense": 80,
            "speed": 110
        },
        "possible_moves": ["Thunder Shock", "Growl", "Quick Attack", "Thunder Wave", "Thunderbolt", "Thunder", "Agility", "Focus Blast"],
        "evolution": None
    },
    "Jigglypuff": {
        "types": [Type.NORMAL, Type.FAIRY],
        "base_stats": {
            "health": 115,
            "attack": 45,
            "defense": 20,
            "sp_attack": 45,
            "sp_defense": 25,
            "speed": 20
        },
        "possible_moves": ["Sing", "Pound", "Disable", "Defense Curl", "Double Slap", "Rest", "Body Slam", "Double-Edge"],
        "evolution": {"item": "Moon Stone", "evolves_to": "Wigglytuff"}
    },
    "Wigglytuff": {
        "types": [Type.NORMAL, Type.FAIRY],
        "base_stats": {
            "health": 140,
            "attack": 70,
            "defense": 45,
            "sp_attack": 85,
            "sp_defense": 50,
            "speed": 45
        },
        "possible_moves": ["Sing", "Pound", "Disable", "Defense Curl", "Double Slap", "Rest", "Body Slam", "Double-Edge", "Hyper Voice"],
        "evolution": None
    },
    "Geodude": {
        "types": [Type.ROCK, Type.GROUND],
        "base_stats": {
            "health": 40,
            "attack": 80,
            "defense": 100,
            "sp_attack": 30,
            "sp_defense": 30,
            "speed": 20
        },
        "possible_moves": ["Tackle", "Defense Curl", "Rock Throw", "Rock Slide", "Earthquake", "Explosion", "Rollout"],
        "evolution": {"level": 25, "evolves_to": "Graveler"}
    },
    "Graveler": {
        "types": [Type.ROCK, Type.GROUND],
        "base_stats": {
            "health": 55,
            "attack": 95,
            "defense": 115,
            "sp_attack": 45,
            "sp_defense": 45,
            "speed": 35
        },
        "possible_moves": ["Tackle", "Defense Curl", "Rock Throw", "Rock Slide", "Earthquake", "Explosion", "Rollout"],
        "evolution": {"trade": True, "evolves_to": "Golem"}
    },
    "Golem": {
        "types": [Type.ROCK, Type.GROUND],
        "base_stats": {
            "health": 80,
            "attack": 120,
            "defense": 130,
            "sp_attack": 55,
            "sp_defense": 65,
            "speed": 45
        },
        "possible_moves": ["Tackle", "Defense Curl", "Rock Throw", "Rock Slide", "Earthquake", "Explosion", "Rollout", "Stone Edge", "Heavy Slam"],
        "evolution": None
    },
    "Gastly": {
        "types": [Type.GHOST, Type.POISON],
        "base_stats": {
            "health": 30,
            "attack": 35,
            "defense": 30,
            "sp_attack": 100,
            "sp_defense": 35,
            "speed": 80
        },
        "possible_moves": ["Lick", "Confuse Ray", "Night Shade", "Hypnosis", "Dream Eater", "Destiny Bond", "Shadow Ball"],
        "evolution": {"level": 25, "evolves_to": "Haunter"}
    },
    "Haunter": {
        "types": [Type.GHOST, Type.POISON],
        "base_stats": {
            "health": 45,
            "attack": 50,
            "defense": 45,
            "sp_attack": 115,
            "sp_defense": 55,
            "speed": 95
        },
        "possible_moves": ["Lick", "Confuse Ray", "Night Shade", "Hypnosis", "Dream Eater", "Destiny Bond", "Shadow Ball"],
        "evolution": {"trade": True, "evolves_to": "Gengar"}
    },
    "Gengar": {
        "types": [Type.GHOST, Type.POISON],
        "base_stats": {
            "health": 60,
            "attack": 65,
            "defense": 60,
            "sp_attack": 130,
            "sp_defense": 75,
            "speed": 110
        },
        "possible_moves": ["Lick", "Confuse Ray", "Night Shade", "Hypnosis", "Dream Eater", "Destiny Bond", "Shadow Ball", "Sludge Bomb", "Dark Pulse"],
        "evolution": None
    },
    "Eevee": {
        "types": [Type.NORMAL],
        "base_stats": {
            "health": 55,
            "attack": 55,
            "defense": 50,
            "sp_attack": 45,
            "sp_defense": 65,
            "speed": 55
        },
        "possible_moves": ["Tackle", "Tail Whip", "Quick Attack", "Bite", "Swift", "Take Down", "Double-Edge"],
        "evolution": {
            "branches": [
                {"item": "Water Stone", "evolves_to": "Vaporeon"},
                {"item": "Thunder Stone", "evolves_to": "Jolteon"},
                {"item": "Fire Stone", "evolves_to": "Flareon"},
                {"friendship": True, "time": "day", "evolves_to": "Espeon"},
                {"friendship": True, "time": "night", "evolves_to": "Umbreon"}
            ]
        }
    },
    "Vaporeon": {
        "types": [Type.WATER],
        "base_stats": {
            "health": 130,
            "attack": 65,
            "defense": 60,
            "sp_attack": 110,
            "sp_defense": 95,
            "speed": 65
        },
        "possible_moves": ["Tackle", "Tail Whip", "Quick Attack", "Water Gun", "Hydro Pump", "Aurora Beam", "Acid Armor", "Haze"],
        "evolution": None
    },
    "Jolteon": {
        "types": [Type.ELECTRIC],
        "base_stats": {
            "health": 65,
            "attack": 65,
            "defense": 60,
            "sp_attack": 110,
            "sp_defense": 95,
            "speed": 130
        },
        "possible_moves": ["Tackle", "Tail Whip", "Quick Attack", "Thunder Shock", "Thunderbolt", "Thunder Wave", "Pin Missile", "Thunder"],
        "evolution": None
    },
    "Flareon": {
        "types": [Type.FIRE],
        "base_stats": {
            "health": 65,
            "attack": 130,
            "defense": 60,
            "sp_attack": 95,
            "sp_defense": 110,
            "speed": 65
        },
        "possible_moves": ["Tackle", "Tail Whip", "Quick Attack", "Ember", "Flamethrower", "Fire Spin", "Smog", "Fire Blast"],
        "evolution": None
    }
}

# Move data
# Format: {"move_name": {"type": Type.X, "category": MoveCategory.Y, "power": Z, ...}}
MOVE_DATA = {
    "Tackle": {
        "type": Type.NORMAL,
        "category": MoveCategory.PHYSICAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Scratch": {
        "type": Type.NORMAL,
        "category": MoveCategory.PHYSICAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Growl": {
        "type": Type.NORMAL,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6,
        "stat_changes": {"attack": -1}
    },
    "Tail Whip": {
        "type": Type.NORMAL,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6,
        "stat_changes": {"defense": -1}
    },
    "Quick Attack": {
        "type": Type.NORMAL,
        "category": MoveCategory.PHYSICAL,
        "power": 40,
        "accuracy": 100,
        "priority": 1,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Vine Whip": {
        "type": Type.GRASS,
        "category": MoveCategory.PHYSICAL,
        "power": 45,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Razor Leaf": {
        "type": Type.GRASS,
        "category": MoveCategory.PHYSICAL,
        "power": 55,
        "accuracy": 95,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 4  # Higher critical hit ratio
    },
    "Solar Beam": {
        "type": Type.GRASS,
        "category": MoveCategory.SPECIAL,
        "power": 120,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Sleep Powder": {
        "type": Type.GRASS,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 75,
        "priority": 0,
        "status_effect": StatusEffect.SLEEP,
        "status_chance": 100,
        "critical_rate": 6
    },
    "Poison Powder": {
        "type": Type.POISON,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 75,
        "priority": 0,
        "status_effect": StatusEffect.POISON,
        "status_chance": 100,
        "critical_rate": 6
    },
    "Ember": {
        "type": Type.FIRE,
        "category": MoveCategory.SPECIAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.BURN,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Flamethrower": {
        "type": Type.FIRE,
        "category": MoveCategory.SPECIAL,
        "power": 90,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.BURN,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Fire Spin": {
        "type": Type.FIRE,
        "category": MoveCategory.SPECIAL,
        "power": 35,
        "accuracy": 85,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Fire Blast": {
        "type": Type.FIRE,
        "category": MoveCategory.SPECIAL,
        "power": 110,
        "accuracy": 85,
        "priority": 0,
        "status_effect": StatusEffect.BURN,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Water Gun": {
        "type": Type.WATER,
        "category": MoveCategory.SPECIAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Bubble": {
        "type": Type.WATER,
        "category": MoveCategory.SPECIAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6,
        "stat_changes": {"speed": -1}
    },
    "Hydro Pump": {
        "type": Type.WATER,
        "category": MoveCategory.SPECIAL,
        "power": 110,
        "accuracy": 80,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Thunder Shock": {
        "type": Type.ELECTRIC,
        "category": MoveCategory.SPECIAL,
        "power": 40,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.PARALYSIS,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Thunderbolt": {
        "type": Type.ELECTRIC,
        "category": MoveCategory.SPECIAL,
        "power": 90,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.PARALYSIS,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Thunder Wave": {
        "type": Type.ELECTRIC,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 90,
        "priority": 0,
        "status_effect": StatusEffect.PARALYSIS,
        "status_chance": 100,
        "critical_rate": 6
    },
    "Thunder": {
        "type": Type.ELECTRIC,
        "category": MoveCategory.SPECIAL,
        "power": 110,
        "accuracy": 70,
        "priority": 0,
        "status_effect": StatusEffect.PARALYSIS,
        "status_chance": 30,
        "critical_rate": 6
    },
    "Rock Throw": {
        "type": Type.ROCK,
        "category": MoveCategory.PHYSICAL,
        "power": 50,
        "accuracy": 90,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Rock Slide": {
        "type": Type.ROCK,
        "category": MoveCategory.PHYSICAL,
        "power": 75,
        "accuracy": 90,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Earthquake": {
        "type": Type.GROUND,
        "category": MoveCategory.PHYSICAL,
        "power": 100,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Lick": {
        "type": Type.GHOST,
        "category": MoveCategory.PHYSICAL,
        "power": 30,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.PARALYSIS,
        "status_chance": 30,
        "critical_rate": 6
    },
    "Shadow Ball": {
        "type": Type.GHOST,
        "category": MoveCategory.SPECIAL,
        "power": 80,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6,
        "stat_changes": {"sp_defense": -1}
    },
    "Hypnosis": {
        "type": Type.PSYCHIC,
        "category": MoveCategory.STATUS,
        "power": 0,
        "accuracy": 60,
        "priority": 0,
        "status_effect": StatusEffect.SLEEP,
        "status_chance": 100,
        "critical_rate": 6
    },
    "Psychic": {
        "type": Type.PSYCHIC,
        "category": MoveCategory.SPECIAL,
        "power": 90,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6,
        "stat_changes": {"sp_defense": -1}
    },
    "Confusion": {
        "type": Type.PSYCHIC,
        "category": MoveCategory.SPECIAL,
        "power": 50,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.NONE,
        "status_chance": 0,
        "critical_rate": 6
    },
    "Ice Beam": {
        "type": Type.ICE,
        "category": MoveCategory.SPECIAL,
        "power": 90,
        "accuracy": 100,
        "priority": 0,
        "status_effect": StatusEffect.FREEZE,
        "status_chance": 10,
        "critical_rate": 6
    },
    "Blizzard": {
        "type": Type.ICE,
        "category": MoveCategory.SPECIAL,
        "power": 110,
        "accuracy": 70,
        "priority": 0,
        "status_effect": StatusEffect.FREEZE,
        "status_chance": 10,
        "critical_rate": 6
    }
}


def create_move_from_data(move_name: str) -> Move:
    """Create a Move object from the move data dictionary

    Args:
        move_name: The name of the move to create

    Returns:
        Move: The created Move object
    """
    if move_name not in MOVE_DATA:
        raise ValueError(f"Move '{move_name}' not found in move data")

    move_info = MOVE_DATA[move_name]

    return Move(
        name=move_name,
        type=move_info["type"],
        category=move_info["category"],
        power=move_info["power"],
        accuracy=move_info["accuracy"],
        priority=move_info.get("priority", 0),
        status_effect=move_info.get("status_effect", StatusEffect.NONE),
        status_chance=move_info.get("status_chance", 0),
        critical_rate=move_info.get("critical_rate", 6)
    )


def create_pokemon_from_data(species_name: str, level: int = 50) -> Pokemon:
    """Create a Pokemon object from the Pokemon data dictionary

    Args:
        species_name: The name of the Pokemon species to create
        level: The level of the Pokemon (affects stats)

    Returns:
        Pokemon: The created Pokemon object
    """
    if species_name not in POKEMON_DATA:
        raise ValueError(
            f"Pokemon species '{species_name}' not found in Pokemon data")

    pokemon_info = POKEMON_DATA[species_name]

    # Get base stats and scale them based on level
    base_stats = pokemon_info["base_stats"]
    level_multiplier = 0.7 + (level / 50) * 0.6  # Simple level scaling formula

    # Create a list of moves (up to 4) from the possible moves
    possible_moves = pokemon_info["possible_moves"]
    num_moves = min(4, len(possible_moves))
    selected_move_names = random.sample(possible_moves, num_moves)
    moves = [create_move_from_data(move_name)
             for move_name in selected_move_names]

    return Pokemon(
        name=species_name,
        types=pokemon_info["types"],
        health=int(base_stats["health"] * level_multiplier),
        attack=int(base_stats["attack"] * level_multiplier),
        defense=int(base_stats["defense"] * level_multiplier),
        sp_attack=int(base_stats["sp_attack"] * level_multiplier),
        sp_defense=int(base_stats["sp_defense"] * level_multiplier),
        speed=int(base_stats["speed"] * level_multiplier),
        ability=None,  # Would need to implement abilities
        moves=moves
    )
