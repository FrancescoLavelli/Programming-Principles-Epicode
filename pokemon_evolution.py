from typing import Dict, List, Tuple, Optional, Callable, Union
from enum import Enum
from PokemonEnhanced import Pokemon, Type


class EvolutionTrigger(Enum):
    """Triggers that can cause a Pokemon to evolve"""
    LEVEL_UP = "Level Up"  # Evolution at a specific level
    ITEM = "Item"  # Evolution when exposed to an item
    TRADE = "Trade"  # Evolution when traded
    FRIENDSHIP = "Friendship"  # Evolution with high friendship
    SPECIAL = "Special"  # Special conditions (time of day, location, etc.)


class EvolutionRequirement:
    """Represents requirements for a Pokemon to evolve"""

    def __init__(self, trigger: EvolutionTrigger,
                 details: Dict[str, Union[int, str, bool]] = None):
        self.trigger = trigger
        self.details = details or {}

    def can_evolve(self, pokemon: 'PokemonWithLevel', **kwargs) -> bool:
        """Check if the Pokemon meets the requirements to evolve

        Args:
            pokemon: The Pokemon to check
            **kwargs: Additional arguments specific to the evolution trigger

        Returns:
            bool: Whether the Pokemon can evolve
        """
        if self.trigger == EvolutionTrigger.LEVEL_UP:
            required_level = self.details.get("min_level", 0)
            return pokemon.level >= required_level

        elif self.trigger == EvolutionTrigger.ITEM:
            item_name = kwargs.get("item_name")
            required_item = self.details.get("item_name")
            return item_name == required_item

        elif self.trigger == EvolutionTrigger.TRADE:
            is_trade = kwargs.get("is_trade", False)
            with_item = self.details.get("with_item")

            if with_item:
                held_item = kwargs.get("held_item")
                return is_trade and held_item == with_item
            return is_trade

        elif self.trigger == EvolutionTrigger.FRIENDSHIP:
            min_friendship = self.details.get("min_friendship", 220)
            friendship = kwargs.get("friendship", 0)

            time_of_day = self.details.get("time_of_day")
            current_time = kwargs.get("time_of_day")

            if time_of_day and current_time != time_of_day:
                return False

            return friendship >= min_friendship

        elif self.trigger == EvolutionTrigger.SPECIAL:
            # Special conditions would be checked with custom logic
            condition_met = self.details.get(
                "condition_check", lambda **kw: False)(**kwargs)
            return condition_met

        return False


class Evolution:
    """Represents an evolution for a Pokemon"""

    def __init__(self, from_species: str, to_species: str,
                 requirement: EvolutionRequirement,
                 stat_changes: Dict[str, float] = None):
        self.from_species = from_species
        self.to_species = to_species
        self.requirement = requirement
        # Multipliers for stats when evolving (e.g., {"attack": 1.2} increases attack by 20%)
        self.stat_changes = stat_changes or {}

    def evolve(self, pokemon: 'PokemonWithLevel', evolution_data: Dict[str, Dict]) -> Tuple[bool, str, Optional['PokemonWithLevel']]:
        """Evolve the Pokemon if requirements are met

        Args:
            pokemon: The Pokemon to evolve
            evolution_data: Dictionary containing evolution species data

        Returns:
            Tuple[bool, str, Optional[PokemonWithLevel]]: 
                (success, message, evolved_pokemon or None)
        """
        if pokemon.name != self.from_species:
            return False, f"This evolution is for {self.from_species}, not {pokemon.name}", None

        # Get the evolution species data
        if self.to_species not in evolution_data:
            return False, f"Evolution data for {self.to_species} not found", None

        evolved_species_data = evolution_data[self.to_species]

        # Create the evolved Pokemon
        evolved_pokemon = PokemonWithLevel(
            name=self.to_species,
            types=[Type[t.upper()]
                   for t in evolved_species_data.get("types", [])],
            health=int(pokemon.health * self.stat_changes.get("health", 1.1)),
            attack=int(pokemon.attack * self.stat_changes.get("attack", 1.1)),
            defense=int(pokemon.defense *
                        self.stat_changes.get("defense", 1.1)),
            sp_attack=int(pokemon.sp_attack *
                          self.stat_changes.get("sp_attack", 1.1)),
            sp_defense=int(pokemon.sp_defense *
                           self.stat_changes.get("sp_defense", 1.1)),
            speed=int(pokemon.speed * self.stat_changes.get("speed", 1.1)),
            ability=pokemon.ability,  # Keep the same ability or could change based on species
            moves=pokemon.moves,  # Keep the same moves
            level=pokemon.level,
            exp=pokemon.exp
        )

        # Transfer any learned moves or other properties

        return True, f"{pokemon.name} evolved into {evolved_pokemon.name}!", evolved_pokemon


class PokemonWithLevel(Pokemon):
    """Extended Pokemon class with level and experience"""

    def __init__(self, name: str, types: List[Type], health: int, attack: int, defense: int,
                 sp_attack: int, sp_defense: int, speed: int, ability=None,
                 moves=None, level: int = 5, exp: int = 0):
        super().__init__(name, types, health, attack, defense,
                         sp_attack, sp_defense, speed, ability, moves)
        self.level = level
        self.exp = exp
        self.friendship = 0  # Base friendship value
        self.held_item = None  # Item the Pokemon is holding

    def gain_exp(self, amount: int) -> Tuple[int, bool]:
        """Add experience points and level up if necessary

        Args:
            amount: Amount of experience to add

        Returns:
            Tuple[int, bool]: (levels gained, whether leveled up)
        """
        self.exp += amount

        # Simple level-up formula: each level requires level*100 exp
        exp_for_next_level = self.level * 100

        levels_gained = 0
        leveled_up = False

        while self.exp >= exp_for_next_level:
            self.exp -= exp_for_next_level
            self.level += 1
            levels_gained += 1
            leveled_up = True

            # Recalculate exp needed for next level
            exp_for_next_level = self.level * 100

            # Increase stats on level up (simplified)
            self.health = int(self.health * 1.02)
            self.max_health = self.health
            self.attack = int(self.attack * 1.02)
            self.defense = int(self.defense * 1.02)
            self.sp_attack = int(self.sp_attack * 1.02)
            self.sp_defense = int(self.sp_defense * 1.02)
            self.speed = int(self.speed * 1.02)

        return levels_gained, leveled_up

    def increase_friendship(self, amount: int) -> int:
        """Increase the Pokemon's friendship value

        Args:
            amount: Amount to increase friendship by

        Returns:
            int: New friendship value
        """
        self.friendship = min(255, self.friendship +
                              amount)  # Max friendship is 255
        return self.friendship

    def check_evolution(self, evolution_chain: List[Evolution],
                        evolution_data: Dict[str, Dict], **kwargs) -> Tuple[bool, str, Optional['PokemonWithLevel']]:
        """Check if the Pokemon can evolve and evolve it if possible

        Args:
            evolution_chain: List of possible evolutions for this Pokemon
            evolution_data: Dictionary containing evolution species data
            **kwargs: Additional arguments for evolution requirements

        Returns:
            Tuple[bool, str, Optional[PokemonWithLevel]]:
                (success, message, evolved_pokemon or None)
        """
        # Find applicable evolutions for this Pokemon
        possible_evolutions = [
            e for e in evolution_chain if e.from_species == self.name]

        for evolution in possible_evolutions:
            # Check if requirements are met
            if evolution.requirement.can_evolve(self, **kwargs):
                return evolution.evolve(self, evolution_data)

        return False, f"{self.name} cannot evolve right now.", None


# Example evolution chains
def create_sample_evolution_data():
    """Create sample evolution data for demonstration"""
    # Evolution chains
    evolution_chains = [
        # Pikachu -> Raichu (Thunder Stone)
        Evolution(
            from_species="Pikachu",
            to_species="Raichu",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.ITEM,
                details={"item_name": "Thunder Stone"}
            ),
            stat_changes={
                "health": 1.1,
                "attack": 1.2,
                "defense": 1.1,
                "sp_attack": 1.3,
                "sp_defense": 1.2,
                "speed": 1.2
            }
        ),

        # Charmander -> Charmeleon (Level 16)
        Evolution(
            from_species="Charmander",
            to_species="Charmeleon",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.LEVEL_UP,
                details={"min_level": 16}
            ),
            stat_changes={
                "health": 1.2,
                "attack": 1.2,
                "defense": 1.2,
                "sp_attack": 1.3,
                "sp_defense": 1.2,
                "speed": 1.2
            }
        ),

        # Charmeleon -> Charizard (Level 36)
        Evolution(
            from_species="Charmeleon",
            to_species="Charizard",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.LEVEL_UP,
                details={"min_level": 36}
            ),
            stat_changes={
                "health": 1.3,
                "attack": 1.3,
                "defense": 1.2,
                "sp_attack": 1.4,
                "sp_defense": 1.3,
                "speed": 1.3
            }
        ),

        # Squirtle -> Wartortle (Level 16)
        Evolution(
            from_species="Squirtle",
            to_species="Wartortle",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.LEVEL_UP,
                details={"min_level": 16}
            ),
            stat_changes={
                "health": 1.2,
                "attack": 1.2,
                "defense": 1.3,
                "sp_attack": 1.2,
                "sp_defense": 1.3,
                "speed": 1.1
            }
        ),

        # Wartortle -> Blastoise (Level 36)
        Evolution(
            from_species="Wartortle",
            to_species="Blastoise",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.LEVEL_UP,
                details={"min_level": 36}
            ),
            stat_changes={
                "health": 1.3,
                "attack": 1.2,
                "defense": 1.4,
                "sp_attack": 1.3,
                "sp_defense": 1.4,
                "speed": 1.1
            }
        ),

        # Eevee -> Vaporeon (Water Stone)
        Evolution(
            from_species="Eevee",
            to_species="Vaporeon",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.ITEM,
                details={"item_name": "Water Stone"}
            ),
            stat_changes={
                "health": 1.4,
                "attack": 1.1,
                "defense": 1.2,
                "sp_attack": 1.4,
                "sp_defense": 1.3,
                "speed": 1.1
            }
        ),

        # Eevee -> Jolteon (Thunder Stone)
        Evolution(
            from_species="Eevee",
            to_species="Jolteon",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.ITEM,
                details={"item_name": "Thunder Stone"}
            ),
            stat_changes={
                "health": 1.1,
                "attack": 1.1,
                "defense": 1.1,
                "sp_attack": 1.4,
                "sp_defense": 1.3,
                "speed": 1.5
            }
        ),

        # Eevee -> Flareon (Fire Stone)
        Evolution(
            from_species="Eevee",
            to_species="Flareon",
            requirement=EvolutionRequirement(
                trigger=EvolutionTrigger.ITEM,
                details={"item_name": "Fire Stone"}
            ),
            stat_changes={
                "health": 1.1,
                "attack": 1.5,
                "defense": 1.2,
                "sp_attack": 1.3,
                "sp_defense": 1.4,
                "speed": 1.1
            }
        ),
    ]

    # Evolution species data
    evolution_data = {
        "Pikachu": {
            "types": ["electric"],
            "base_stats": {"health": 35, "attack": 55, "defense": 40, "sp_attack": 50, "sp_defense": 50, "speed": 90}
        },
        "Raichu": {
            "types": ["electric"],
            "base_stats": {"health": 60, "attack": 90, "defense": 55, "sp_attack": 90, "sp_defense": 80, "speed": 110}
        },
        "Charmander": {
            "types": ["fire"],
            "base_stats": {"health": 39, "attack": 52, "defense": 43, "sp_attack": 60, "sp_defense": 50, "speed": 65}
        },
        "Charmeleon": {
            "types": ["fire"],
            "base_stats": {"health": 58, "attack": 64, "defense": 58, "sp_attack": 80, "sp_defense": 65, "speed": 80}
        },
        "Charizard": {
            "types": ["fire", "flying"],
            "base_stats": {"health": 78, "attack": 84, "defense": 78, "sp_attack": 109, "sp_defense": 85, "speed": 100}
        },
        "Squirtle": {
            "types": ["water"],
            "base_stats": {"health": 44, "attack": 48, "defense": 65, "sp_attack": 50, "sp_defense": 64, "speed": 43}
        },
        "Wartortle": {
            "types": ["water"],
            "base_stats": {"health": 59, "attack": 63, "defense": 80, "sp_attack": 65, "sp_defense": 80, "speed": 58}
        },
        "Blastoise": {
            "types": ["water"],
            "base_stats": {"health": 79, "attack": 83, "defense": 100, "sp_attack": 85, "sp_defense": 105, "speed": 78}
        },
        "Eevee": {
            "types": ["normal"],
            "base_stats": {"health": 55, "attack": 55, "defense": 50, "sp_attack": 45, "sp_defense": 65, "speed": 55}
        },
        "Vaporeon": {
            "types": ["water"],
            "base_stats": {"health": 130, "attack": 65, "defense": 60, "sp_attack": 110, "sp_defense": 95, "speed": 65}
        },
        "Jolteon": {
            "types": ["electric"],
            "base_stats": {"health": 65, "attack": 65, "defense": 60, "sp_attack": 110, "sp_defense": 95, "speed": 130}
        },
        "Flareon": {
            "types": ["fire"],
            "base_stats": {"health": 65, "attack": 130, "defense": 60, "sp_attack": 95, "sp_defense": 110, "speed": 65}
        },
    }

    return evolution_chains, evolution_data
