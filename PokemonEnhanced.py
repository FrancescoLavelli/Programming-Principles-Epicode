import random
from typing import Dict, Any, Optional, List, Tuple
from enum import Enum


class Type(Enum):
    """Pokemon types enum"""
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"


class MoveCategory(Enum):
    """Move categories enum"""
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"


class StatusEffect(Enum):
    """Status effects enum"""
    NONE = "None"
    BURN = "Burn"  # Reduces attack by 50% and deals damage each turn
    PARALYSIS = "Paralysis"  # 25% chance to not move and reduces speed by 50%
    POISON = "Poison"  # Deals damage each turn
    SLEEP = "Sleep"  # Cannot move for 1-3 turns
    FREEZE = "Freeze"  # Cannot move until thawed (20% chance each turn)


# Type effectiveness chart (multiplier for damage)
# Format: {attacking_type: {defending_type: multiplier}}
TYPE_CHART = {
    Type.NORMAL: {
        Type.ROCK: 0.5,
        Type.GHOST: 0,
        Type.STEEL: 0.5
    },
    Type.FIRE: {
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.GRASS: 2,
        Type.ICE: 2,
        Type.BUG: 2,
        Type.ROCK: 0.5,
        Type.DRAGON: 0.5,
        Type.STEEL: 2
    },
    Type.WATER: {
        Type.FIRE: 2,
        Type.WATER: 0.5,
        Type.GRASS: 0.5,
        Type.GROUND: 2,
        Type.ROCK: 2,
        Type.DRAGON: 0.5
    },
    Type.ELECTRIC: {
        Type.WATER: 2,
        Type.ELECTRIC: 0.5,
        Type.GRASS: 0.5,
        Type.GROUND: 0,
        Type.FLYING: 2,
        Type.DRAGON: 0.5
    },
    Type.GRASS: {
        Type.FIRE: 0.5,
        Type.WATER: 2,
        Type.GRASS: 0.5,
        Type.POISON: 0.5,
        Type.GROUND: 2,
        Type.FLYING: 0.5,
        Type.BUG: 0.5,
        Type.ROCK: 2,
        Type.DRAGON: 0.5,
        Type.STEEL: 0.5
    },
    Type.ICE: {
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.GRASS: 2,
        Type.ICE: 0.5,
        Type.GROUND: 2,
        Type.FLYING: 2,
        Type.DRAGON: 2,
        Type.STEEL: 0.5
    },
    Type.FIGHTING: {
        Type.NORMAL: 2,
        Type.ICE: 2,
        Type.POISON: 0.5,
        Type.FLYING: 0.5,
        Type.PSYCHIC: 0.5,
        Type.BUG: 0.5,
        Type.ROCK: 2,
        Type.GHOST: 0,
        Type.DARK: 2,
        Type.STEEL: 2,
        Type.FAIRY: 0.5
    },
    Type.POISON: {
        Type.GRASS: 2,
        Type.POISON: 0.5,
        Type.GROUND: 0.5,
        Type.ROCK: 0.5,
        Type.GHOST: 0.5,
        Type.STEEL: 0,
        Type.FAIRY: 2
    },
    Type.GROUND: {
        Type.FIRE: 2,
        Type.ELECTRIC: 2,
        Type.GRASS: 0.5,
        Type.POISON: 2,
        Type.FLYING: 0,
        Type.BUG: 0.5,
        Type.ROCK: 2,
        Type.STEEL: 2
    },
    Type.FLYING: {
        Type.ELECTRIC: 0.5,
        Type.GRASS: 2,
        Type.FIGHTING: 2,
        Type.BUG: 2,
        Type.ROCK: 0.5,
        Type.STEEL: 0.5
    },
    Type.PSYCHIC: {
        Type.FIGHTING: 2,
        Type.POISON: 2,
        Type.PSYCHIC: 0.5,
        Type.DARK: 0,
        Type.STEEL: 0.5
    },
    Type.BUG: {
        Type.FIRE: 0.5,
        Type.GRASS: 2,
        Type.FIGHTING: 0.5,
        Type.POISON: 0.5,
        Type.FLYING: 0.5,
        Type.PSYCHIC: 2,
        Type.GHOST: 0.5,
        Type.DARK: 2,
        Type.STEEL: 0.5,
        Type.FAIRY: 0.5
    },
    Type.ROCK: {
        Type.FIRE: 2,
        Type.ICE: 2,
        Type.FIGHTING: 0.5,
        Type.GROUND: 0.5,
        Type.FLYING: 2,
        Type.BUG: 2,
        Type.STEEL: 0.5
    },
    Type.GHOST: {
        Type.NORMAL: 0,
        Type.PSYCHIC: 2,
        Type.GHOST: 2,
        Type.DARK: 0.5
    },
    Type.DRAGON: {
        Type.DRAGON: 2,
        Type.STEEL: 0.5,
        Type.FAIRY: 0
    },
    Type.DARK: {
        Type.FIGHTING: 0.5,
        Type.PSYCHIC: 2,
        Type.GHOST: 2,
        Type.DARK: 0.5,
        Type.FAIRY: 0.5
    },
    Type.STEEL: {
        Type.FIRE: 0.5,
        Type.WATER: 0.5,
        Type.ELECTRIC: 0.5,
        Type.ICE: 2,
        Type.ROCK: 2,
        Type.STEEL: 0.5,
        Type.FAIRY: 2
    },
    Type.FAIRY: {
        Type.FIGHTING: 2,
        Type.POISON: 0.5,
        Type.DRAGON: 2,
        Type.DARK: 2,
        Type.STEEL: 0.5
    }
}


class Ability:
    """Represents a Pokemon ability"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def on_attack(self, attacker: 'Pokemon', defender: 'Pokemon', move: 'Move') -> Tuple[bool, int, str]:
        """Called when the Pokemon with this ability attacks

        Returns:
            Tuple[bool, int, str]: (should_continue, damage_modifier, message)
        """
        return True, 100, ""

    def on_defend(self, attacker: 'Pokemon', defender: 'Pokemon', move: 'Move') -> Tuple[bool, int, str]:
        """Called when the Pokemon with this ability is attacked

        Returns:
            Tuple[bool, int, str]: (should_continue, damage_modifier_percent, message)
        """
        return True, 100, ""

    def on_turn_start(self, pokemon: 'Pokemon') -> str:
        """Called at the start of the Pokemon's turn

        Returns:
            str: Message to display
        """
        return ""

    def on_turn_end(self, pokemon: 'Pokemon') -> str:
        """Called at the end of the Pokemon's turn

        Returns:
            str: Message to display
        """
        return ""


class Move:
    """Represents a Pokemon move with its properties."""

    def __init__(self, name: str, type: Type, category: MoveCategory, power: int, accuracy: int,
                 priority: int = 0, status_effect: StatusEffect = StatusEffect.NONE,
                 status_chance: int = 0, critical_rate: int = 6):
        self.validate_move_parameters(
            name, power, accuracy, status_chance, critical_rate)
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.priority = priority  # Higher priority moves go first
        self.status_effect = status_effect
        # Chance to apply status effect (0-100)
        self.status_chance = status_chance
        # 1/critical_rate chance (e.g., 6 means 1/6 chance)
        self.critical_rate = critical_rate

    def validate_move_parameters(self, name: str, power: int, accuracy: int,
                                 status_chance: int, critical_rate: int):
        """Validate the parameters of a move."""
        if not name or not isinstance(name, str):
            raise ValueError("Move name must be a non-empty string")
        if not isinstance(power, int) or power < 0:
            raise ValueError("Power must be a non-negative integer")
        if not isinstance(accuracy, int) or accuracy < 0 or accuracy > 100:
            raise ValueError("Accuracy must be an integer between 0 and 100")
        if not isinstance(status_chance, int) or status_chance < 0 or status_chance > 100:
            raise ValueError(
                "Status chance must be an integer between 0 and 100")
        if not isinstance(critical_rate, int) or critical_rate < 1:
            raise ValueError("Critical rate must be a positive integer")

    def is_critical_hit(self) -> bool:
        """Determine if the move results in a critical hit."""
        return random.randint(1, self.critical_rate) == 1

    def apply_status_effect(self) -> bool:
        """Determine if the status effect should be applied."""
        return self.status_effect != StatusEffect.NONE and random.randint(1, 100) <= self.status_chance


class Pokemon:
    """Represents a Pokemon with its attributes and battle capabilities."""

    def __init__(self, name: str, types: List[Type], health: int, attack: int, defense: int,
                 sp_attack: int, sp_defense: int, speed: int, ability: Optional[Ability] = None,
                 moves: Optional[List[Move]] = None):
        self.validate_pokemon_parameters(
            name, health, attack, defense, sp_attack, sp_defense, speed)

        self.name = name
        self.types = types
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.ability = ability
        self.moves = moves or []

        # Battle state
        self.current_health = health
        self.status_effect = StatusEffect.NONE
        self.status_counter = 0  # For sleep/freeze duration
        self.stat_modifiers = {  # -6 to +6 range for stat modifiers
            "attack": 0,
            "defense": 0,
            "sp_attack": 0,
            "sp_defense": 0,
            "speed": 0,
            "accuracy": 0,
            "evasion": 0
        }

    def validate_pokemon_parameters(self, name: str, health: int, attack: int,
                                    defense: int, sp_attack: int, sp_defense: int, speed: int):
        """Validate the parameters of a Pokemon."""
        if not name or not isinstance(name, str):
            raise ValueError("Pokemon name must be a non-empty string")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a non-negative integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a non-negative integer")
        if not isinstance(sp_attack, int) or sp_attack < 0:
            raise ValueError("Special Attack must be a non-negative integer")
        if not isinstance(sp_defense, int) or sp_defense < 0:
            raise ValueError("Special Defense must be a non-negative integer")
        if not isinstance(speed, int) or speed < 0:
            raise ValueError("Speed must be a non-negative integer")

    def get_modified_stat(self, stat: str) -> int:
        """Get a stat value after applying stat modifiers."""
        base_stat = getattr(self, stat, 0)
        modifier = self.stat_modifiers.get(stat, 0)

        # Apply stat modifier formula (same as in the games)
        if modifier >= 0:
            multiplier = (2 + modifier) / 2
        else:
            multiplier = 2 / (2 - modifier)

        return int(base_stat * multiplier)

    def get_modified_speed(self) -> int:
        """Get the speed stat after applying modifiers and status effects."""
        modified_speed = self.get_modified_stat("speed")

        # Apply paralysis speed reduction
        if self.status_effect == StatusEffect.PARALYSIS:
            modified_speed = modified_speed // 2

        return modified_speed

    def can_move(self) -> Tuple[bool, str]:
        """Check if the Pokemon can move this turn based on status effects."""
        if self.status_effect == StatusEffect.PARALYSIS:
            # 25% chance to be fully paralyzed each turn
            if random.randint(1, 4) == 1:
                return False, f"{self.name} is paralyzed and can't move!"
            return True, ""

        elif self.status_effect == StatusEffect.SLEEP:
            if self.status_counter > 0:
                self.status_counter -= 1
                if self.status_counter == 0:
                    self.status_effect = StatusEffect.NONE
                    return True, f"{self.name} woke up!"
                return False, f"{self.name} is fast asleep!"
            else:
                self.status_effect = StatusEffect.NONE
                return True, f"{self.name} woke up!"

        elif self.status_effect == StatusEffect.FREEZE:
            if random.randint(1, 5) == 1:  # 20% chance to thaw
                self.status_effect = StatusEffect.NONE
                return True, f"{self.name} thawed out!"
            return False, f"{self.name} is frozen solid!"

        return True, ""

    def apply_status_effect(self, effect: StatusEffect) -> str:
        """Apply a status effect to the Pokemon."""
        # Can't apply a status if already has one
        if self.status_effect != StatusEffect.NONE:
            return f"{self.name} already has {self.status_effect.value}!"

        self.status_effect = effect

        if effect == StatusEffect.SLEEP:
            self.status_counter = random.randint(1, 3)  # Sleep for 1-3 turns
            return f"{self.name} fell asleep!"
        elif effect == StatusEffect.PARALYSIS:
            self.status_counter = random.randint(
                1, 2)  # Paralyzed for 1-2 turns
            return f"{self.name} is paralyzed! It may be unable to move!"
        elif effect == StatusEffect.BURN:
            return f"{self.name} was burned!"
        elif effect == StatusEffect.POISON:
            return f"{self.name} was poisoned!"
        elif effect == StatusEffect.FREEZE:
            return f"{self.name} was frozen solid!"

        return ""

    def apply_end_turn_status_effects(self) -> Tuple[int, str]:
        """Apply end-of-turn effects from status conditions.

        Returns:
            Tuple[int, str]: (damage_taken, message)
        """
        if self.status_effect == StatusEffect.BURN:
            damage = max(1, self.max_health // 16)  # 1/16 of max HP
            self.current_health = max(0, self.current_health - damage)
            return damage, f"{self.name} was hurt by its burn!"

        elif self.status_effect == StatusEffect.POISON:
            damage = max(1, self.max_health // 8)  # 1/8 of max HP
            self.current_health = max(0, self.current_health - damage)
            return damage, f"{self.name} was hurt by poison!"

        return 0, ""

    def calculate_type_effectiveness(self, move: Move) -> float:
        """Calculate type effectiveness multiplier."""
        multiplier = 1.0

        # Get effectiveness for each of the defender's types
        for defender_type in self.types:
            if move.type in TYPE_CHART and defender_type in TYPE_CHART[move.type]:
                multiplier *= TYPE_CHART[move.type][defender_type]

        return multiplier

    def is_attack_successful(self, move: Move) -> bool:
        """Determine if the attack hits based on move accuracy."""
        return random.randint(1, 100) <= move.accuracy

    def calculate_damage(self, attacker: 'Pokemon', move: Move, is_critical: bool = False) -> Tuple[int, float, bool]:
        """Calculate damage for an attack.

        Returns:
            Tuple[int, float, bool]: (damage, type_effectiveness, is_critical)
        """
        # Status moves don't deal damage
        if move.category == MoveCategory.STATUS:
            return 0, 1.0, False

        # Get the appropriate attack and defense stats based on move category
        if move.category == MoveCategory.PHYSICAL:
            attack_stat = attacker.get_modified_stat("attack")
            defense_stat = self.get_modified_stat("defense")
        else:  # SPECIAL
            attack_stat = attacker.get_modified_stat("sp_attack")
            defense_stat = self.get_modified_stat("sp_defense")

        # Apply burn attack reduction
        if attacker.status_effect == StatusEffect.BURN and move.category == MoveCategory.PHYSICAL:
            attack_stat = attack_stat // 2

        # Calculate base damage (similar to actual Pokemon formula)
        level = 50  # Assume level 50 for simplicity
        base_damage = ((2 * level / 5 + 2) * move.power *
                       attack_stat / defense_stat) / 50 + 2

        # Apply STAB (Same Type Attack Bonus)
        stab = 1.5 if move.type in attacker.types else 1.0

        # Apply type effectiveness
        type_effectiveness = self.calculate_type_effectiveness(move)

        # Apply critical hit (1.5x damage and ignore negative stat changes)
        critical_multiplier = 1.5 if is_critical else 1.0

        # Apply random factor (0.85-1.00)
        random_factor = random.randint(85, 100) / 100

        # Calculate final damage
        damage = int(base_damage * stab * type_effectiveness *
                     critical_multiplier * random_factor)

        return max(1, damage), type_effectiveness, is_critical

    def take_damage(self, attacker: 'Pokemon', move: Move) -> Tuple[bool, List[str]]:
        """Process damage taken from an attack.

        Returns:
            Tuple[bool, List[str]]: (is_fainted, messages)
        """
        messages = []

        # Check if attack hits
        if not self.is_attack_successful(move):
            messages.append(
                f"{attacker.name}'s {move.name} missed {self.name}!")
            return False, messages

        # Check for ability effects before attack
        if attacker.ability:
            should_continue, _, msg = attacker.ability.on_attack(
                attacker, self, move)
            if msg:
                messages.append(msg)
            if not should_continue:
                return False, messages

        if self.ability:
            should_continue, _, msg = self.ability.on_defend(
                attacker, self, move)
            if msg:
                messages.append(msg)
            if not should_continue:
                return False, messages

        # Check for critical hit
        is_critical = move.is_critical_hit()

        # Calculate damage
        damage, type_effectiveness, _ = self.calculate_damage(
            attacker, move, is_critical)

        # Apply damage
        self.current_health = max(0, self.current_health - damage)

        # Build attack message
        messages.append(f"{attacker.name} used {move.name} on {self.name}!")

        if is_critical:
            messages.append("A critical hit!")

        # Type effectiveness messages
        if type_effectiveness > 1:
            messages.append("It's super effective!")
        elif type_effectiveness < 1 and type_effectiveness > 0:
            messages.append("It's not very effective...")
        elif type_effectiveness == 0:
            messages.append(f"It doesn't affect {self.name}...")
            return False, messages

        if damage > 0:
            messages.append(f"Dealt {damage} damage!")

        # Apply status effect if applicable
        if move.apply_status_effect():
            status_msg = self.apply_status_effect(move.status_effect)
            if status_msg:
                messages.append(status_msg)

        # Check if Pokemon fainted
        if self.current_health <= 0:
            messages.append(f"{self.name} fainted!")
            return True, messages

        messages.append(
            f"{self.name}'s HP: {self.current_health}/{self.max_health}")
        return False, messages


class Battle:
    """Manages a Pokemon battle."""

    def __init__(self, player_pokemon: List[Pokemon], opponent_pokemon: List[Pokemon]):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        self.active_player_pokemon = player_pokemon[0] if player_pokemon else None
        self.active_opponent_pokemon = opponent_pokemon[0] if opponent_pokemon else None
        self.turn_count = 0

    def get_action_order(self, player_move: Move, opponent_move: Move) -> List[Tuple['Pokemon', 'Pokemon', Move]]:
        """Determine the order of actions based on move priority and Pokemon speed.

        Returns:
            List[Tuple[Pokemon, Pokemon, Move]]: List of (attacker, defender, move) tuples
        """
        player = self.active_player_pokemon
        opponent = self.active_opponent_pokemon

        # First check move priority
        if player_move.priority > opponent_move.priority:
            return [(player, opponent, player_move), (opponent, player, opponent_move)]
        elif opponent_move.priority > player_move.priority:
            return [(opponent, player, opponent_move), (player, opponent, player_move)]

        # If same priority, check speed
        player_speed = player.get_modified_speed()
        opponent_speed = opponent.get_modified_speed()

        if player_speed > opponent_speed:
            return [(player, opponent, player_move), (opponent, player, opponent_move)]
        elif opponent_speed > player_speed:
            return [(opponent, player, opponent_move), (player, opponent, player_move)]

        # If speed tie, randomize
        if random.choice([True, False]):
            return [(player, opponent, player_move), (opponent, player, opponent_move)]
        else:
            return [(opponent, player, opponent_move), (player, opponent, player_move)]

    def execute_turn(self, player_move: Move, opponent_move: Move) -> List[str]:
        """Execute a full turn of battle.

        Returns:
            List[str]: Battle messages
        """
        self.turn_count += 1
        messages = [f"===== Turn {self.turn_count} ====="]

        # Get action order
        action_order = self.get_action_order(player_move, opponent_move)

        # Execute moves in order
        for attacker, defender, move in action_order:
            # Skip if attacker has fainted
            if attacker.current_health <= 0:
                continue

            # Check if Pokemon can move (status effects)
            can_move, status_msg = attacker.can_move()
            if status_msg:
                messages.append(status_msg)
            if not can_move:
                continue

            # Execute the move
            fainted, move_messages = defender.take_damage(attacker, move)
            messages.extend(move_messages)

            # If defender fainted, end the turn
            if fainted:
                break

        # Apply end-of-turn effects
        for pokemon in [self.active_player_pokemon, self.active_opponent_pokemon]:
            if pokemon.current_health > 0:
                damage, status_msg = pokemon.apply_end_turn_status_effects()
                if status_msg:
                    messages.append(status_msg)
                if damage > 0 and pokemon.current_health <= 0:
                    messages.append(f"{pokemon.name} fainted!")

        return messages

    def is_battle_over(self) -> Tuple[bool, str]:
        """Check if the battle is over.

        Returns:
            Tuple[bool, str]: (is_over, winner_message)
        """
        # Check if all player Pokemon have fainted
        all_player_fainted = all(
            p.current_health <= 0 for p in self.player_pokemon)
        if all_player_fainted:
            return True, "Opponent wins the battle!"

        # Check if all opponent Pokemon have fainted
        all_opponent_fainted = all(
            p.current_health <= 0 for p in self.opponent_pokemon)
        if all_opponent_fainted:
            return True, "Player wins the battle!"

        return False, ""

    def switch_pokemon(self, is_player: bool, index: int) -> List[str]:
        """Switch the active Pokemon.

        Returns:
            List[str]: Switch messages
        """
        messages = []

        if is_player:
            if 0 <= index < len(self.player_pokemon):
                new_pokemon = self.player_pokemon[index]
                if new_pokemon.current_health <= 0:
                    return [f"{new_pokemon.name} has fainted and cannot battle!"]
                if new_pokemon == self.active_player_pokemon:
                    return [f"{new_pokemon.name} is already in battle!"]

                old_pokemon = self.active_player_pokemon
                self.active_player_pokemon = new_pokemon
                messages.append(
                    f"Player withdrew {old_pokemon.name} and sent out {new_pokemon.name}!")
        else:
            if 0 <= index < len(self.opponent_pokemon):
                new_pokemon = self.opponent_pokemon[index]
                if new_pokemon.current_health <= 0:
                    return [f"{new_pokemon.name} has fainted and cannot battle!"]
                if new_pokemon == self.active_opponent_pokemon:
                    return [f"{new_pokemon.name} is already in battle!"]

                old_pokemon = self.active_opponent_pokemon
                self.active_opponent_pokemon = new_pokemon
                messages.append(
                    f"Opponent withdrew {old_pokemon.name} and sent out {new_pokemon.name}!")

        return messages


# Example abilities
class Intimidate(Ability):
    def __init__(self):
        super().__init__("Intimidate", "Lowers the opponent's Attack when entering battle")

    def on_turn_start(self, pokemon: 'Pokemon') -> str:
        # This would be called when the Pokemon enters battle
        # In a real implementation, we would find the opponent and lower their attack
        return f"{pokemon.name}'s Intimidate lowered the opponent's Attack!"
