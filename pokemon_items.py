from typing import Optional, List, Tuple
from enum import Enum

# Import Pokemon class from the main file
from PokemonEnhanced import Pokemon, StatusEffect


class ItemCategory(Enum):
    """Categories of items in Pokemon games"""
    MEDICINE = "Medicine"  # Items that heal HP or status conditions
    BATTLE_ITEM = "Battle Item"  # Items that boost stats or have battle effects
    HELD_ITEM = "Held Item"  # Items that Pokemon can hold for passive effects
    EVOLUTION_ITEM = "Evolution Item"  # Items used to evolve Pokemon
    POKEBALL = "Pokeball"  # Items used to catch Pokemon
    KEY_ITEM = "Key Item"  # Important items for progression


class Item:
    """Represents an item in the Pokemon game"""

    def __init__(self, name: str, description: str, category: ItemCategory,
                 price: int = 0, is_consumable: bool = True):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.is_consumable = is_consumable  # Whether the item is consumed after use

    def use(self, target: Pokemon) -> Tuple[bool, str]:
        """Base method for using an item on a Pokemon

        Args:
            target: The Pokemon to use the item on

        Returns:
            Tuple[bool, str]: (was_successful, message)
        """
        return False, f"{self.name} had no effect."


class MedicineItem(Item):
    """Items that heal HP or cure status conditions"""

    def __init__(self, name: str, description: str, price: int = 0,
                 hp_restore: int = 0, hp_restore_percent: int = 0,
                 cure_status: List[StatusEffect] = None):
        super().__init__(name, description, ItemCategory.MEDICINE, price, True)
        self.hp_restore = hp_restore  # Fixed amount of HP to restore
        self.hp_restore_percent = hp_restore_percent  # Percentage of max HP to restore
        self.cure_status = cure_status or []  # Status conditions this item cures

    def use(self, target: Pokemon) -> Tuple[bool, str]:
        messages = []
        used = False

        # Heal HP if applicable
        if self.hp_restore > 0 or self.hp_restore_percent > 0:
            # Don't heal if already at max HP
            if target.current_health >= target.max_health:
                messages.append(f"{target.name}'s HP is already full!")
            else:
                # Calculate healing amount
                if self.hp_restore > 0:
                    heal_amount = self.hp_restore
                else:  # Use percentage
                    heal_amount = int(target.max_health *
                                      (self.hp_restore_percent / 100))

                # Apply healing
                old_hp = target.current_health
                target.current_health = min(
                    target.current_health + heal_amount, target.max_health)
                actual_heal = target.current_health - old_hp

                messages.append(f"{target.name} recovered {actual_heal} HP!")
                used = True

        # Cure status if applicable
        if self.cure_status and target.status_effect in self.cure_status:
            old_status = target.status_effect
            target.status_effect = StatusEffect.NONE
            target.status_counter = 0
            messages.append(f"{target.name} was cured of {old_status.value}!")
            used = True
        elif self.cure_status and StatusEffect.NONE not in self.cure_status and target.status_effect == StatusEffect.NONE:
            messages.append(
                f"{target.name} doesn't have any status condition to cure!")

        if not used:
            return False, "\n".join(messages)

        return True, "\n".join(messages)


class BattleItem(Item):
    """Items that have effects during battle"""

    def __init__(self, name: str, description: str, price: int = 0,
                 stat_boosts: dict = None, battle_effect: str = None):
        super().__init__(name, description, ItemCategory.BATTLE_ITEM, price, True)
        self.stat_boosts = stat_boosts or {}  # Dict of stat name to boost amount
        self.battle_effect = battle_effect  # Special effect description

    def use(self, target: Pokemon) -> Tuple[bool, str]:
        messages = []
        used = False

        # Apply stat boosts
        if self.stat_boosts:
            for stat, boost in self.stat_boosts.items():
                if stat in target.stat_modifiers:
                    # Check if stat can be boosted further
                    if target.stat_modifiers[stat] >= 6 and boost > 0:
                        messages.append(
                            f"{target.name}'s {stat} won't go any higher!")
                        continue
                    elif target.stat_modifiers[stat] <= -6 and boost < 0:
                        messages.append(
                            f"{target.name}'s {stat} won't go any lower!")
                        continue

                    # Apply boost, capped at -6/+6
                    old_mod = target.stat_modifiers[stat]
                    target.stat_modifiers[stat] = max(-6,
                                                      min(6, old_mod + boost))
                    actual_boost = target.stat_modifiers[stat] - old_mod

                    if actual_boost > 0:
                        messages.append(f"{target.name}'s {stat} rose!")
                    elif actual_boost < 0:
                        messages.append(f"{target.name}'s {stat} fell!")

                    used = True

        # Special battle effects would be implemented in subclasses

        if not used and self.battle_effect:
            messages.append(f"{self.battle_effect}")
            used = True

        if not used:
            return False, "\n".join(messages)

        return True, "\n".join(messages)


class HeldItem(Item):
    """Items that Pokemon can hold for passive effects"""

    def __init__(self, name: str, description: str, price: int = 0,
                 passive_effect: str = None):
        super().__init__(name, description, ItemCategory.HELD_ITEM, price, False)
        self.passive_effect = passive_effect  # Description of passive effect

    def on_attack(self, holder: Pokemon, defender: Pokemon) -> Tuple[bool, int, str]:
        """Called when the Pokemon holding this item attacks

        Returns:
            Tuple[bool, int, str]: (should_continue, damage_modifier_percent, message)
        """
        return True, 100, ""

    def on_defend(self, attacker: Pokemon, holder: Pokemon) -> Tuple[bool, int, str]:
        """Called when the Pokemon holding this item is attacked

        Returns:
            Tuple[bool, int, str]: (should_continue, damage_modifier_percent, message)
        """
        return True, 100, ""

    def on_turn_start(self, holder: Pokemon) -> str:
        """Called at the start of the Pokemon's turn

        Returns:
            str: Message to display
        """
        return ""

    def on_turn_end(self, holder: Pokemon) -> str:
        """Called at the end of the Pokemon's turn

        Returns:
            str: Message to display
        """
        return ""


class EvolutionItem(Item):
    """Items used to evolve Pokemon"""

    def __init__(self, name: str, description: str, price: int = 0):
        super().__init__(name, description, ItemCategory.EVOLUTION_ITEM, price, True)

    def can_evolve(self, pokemon: Pokemon, evolution_name: str) -> bool:
        """Check if this item can evolve the given Pokemon

        Args:
            pokemon: The Pokemon to check
            evolution_name: The name of the evolution

        Returns:
            bool: Whether this item can evolve the Pokemon
        """
        # This would be implemented with specific evolution logic
        # For now, return False as a placeholder
        return False


# Example item instances
def create_common_items() -> List[Item]:
    """Create a list of common items from the Pokemon games"""
    items = [
        # Medicine items
        MedicineItem("Potion", "Restores 20 HP", price=300, hp_restore=20),
        MedicineItem("Super Potion", "Restores 50 HP",
                     price=700, hp_restore=50),
        MedicineItem("Hyper Potion", "Restores 200 HP",
                     price=1200, hp_restore=200),
        MedicineItem("Max Potion", "Fully restores HP",
                     price=2500, hp_restore_percent=100),
        MedicineItem("Full Restore", "Fully restores HP and cures all status conditions",
                     price=3000, hp_restore_percent=100,
                     cure_status=[s for s in StatusEffect if s != StatusEffect.NONE]),
        MedicineItem("Antidote", "Cures poison", price=100,
                     cure_status=[StatusEffect.POISON]),
        MedicineItem("Burn Heal", "Cures burns", price=250,
                     cure_status=[StatusEffect.BURN]),
        MedicineItem("Ice Heal", "Cures freezing", price=250,
                     cure_status=[StatusEffect.FREEZE]),
        MedicineItem("Awakening", "Cures sleep", price=250,
                     cure_status=[StatusEffect.SLEEP]),
        MedicineItem("Paralyze Heal", "Cures paralysis", price=200,
                     cure_status=[StatusEffect.PARALYSIS]),

        # Battle items
        BattleItem("X Attack", "Raises Attack", price=500,
                   stat_boosts={"attack": 1}),
        BattleItem("X Defense", "Raises Defense", price=550,
                   stat_boosts={"defense": 1}),
        BattleItem("X Speed", "Raises Speed", price=350,
                   stat_boosts={"speed": 1}),
        BattleItem("X Accuracy", "Raises accuracy", price=950,
                   stat_boosts={"accuracy": 1}),
        BattleItem("Dire Hit", "Increases critical hit ratio", price=650,
                   battle_effect="Increased the critical hit ratio!"),

        # Held items
        HeldItem("Leftovers", "Holder restores a little HP each turn", price=4000,
                 passive_effect="Restores HP each turn"),
        HeldItem("Choice Band", "Holder's Attack is 1.5x, but can only use first selected move",
                 price=4000, passive_effect="Boosts Attack but restricts to one move"),
        HeldItem("Focus Sash", "Holder survives one hit that would cause fainting if at full HP",
                 price=4000, passive_effect="Survives one hit with 1 HP if at full HP"),

        # Evolution items
        EvolutionItem("Fire Stone", "Evolves certain Pokemon", price=2100),
        EvolutionItem("Water Stone", "Evolves certain Pokemon", price=2100),
        EvolutionItem("Thunder Stone", "Evolves certain Pokemon", price=2100),
        EvolutionItem("Leaf Stone", "Evolves certain Pokemon", price=2100),
        EvolutionItem("Moon Stone", "Evolves certain Pokemon", price=2100),
    ]

    return items
