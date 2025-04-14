import random
from typing import List, Dict, Any, Optional

# Import from our Pokemon modules
from PokemonEnhanced import Type, MoveCategory, StatusEffect, Move, Pokemon, Battle, Ability
from pokemon_items import Item, MedicineItem, BattleItem, HeldItem, create_common_items
from pokemon_ai import PokemonAI
from pokemon_evolution import PokemonWithLevel, create_sample_evolution_data
from pokemon_data import create_move_from_data, create_pokemon_from_data, POKEMON_DATA, MOVE_DATA


def create_demo_pokemon() -> List[PokemonWithLevel]:
    """Create a list of Pokemon for the demo"""
    # Create some moves
    thunderbolt = create_move_from_data("Thunderbolt")
    flamethrower = create_move_from_data("Flamethrower")
    hydro_pump = create_move_from_data("Hydro Pump")
    razor_leaf = create_move_from_data("Razor Leaf")
    quick_attack = create_move_from_data("Quick Attack")
    thunder_wave = create_move_from_data("Thunder Wave")
    ice_beam = create_move_from_data("Ice Beam")
    earthquake = create_move_from_data("Earthquake")

    # Create some abilities
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
                status_msg = attacker.apply_status_effect(
                    StatusEffect.PARALYSIS)
                if status_msg:
                    return True, 100, f"{defender.name}'s Static ability {status_msg}"
            return True, 100, ""

    # Create Pokemon with levels
    pikachu = PokemonWithLevel(
        name="Pikachu",
        types=[Type.ELECTRIC],
        health=274,
        attack=229,
        defense=174,
        sp_attack=218,
        sp_defense=196,
        speed=306,
        ability=Static(),
        moves=[thunderbolt, quick_attack, thunder_wave],
        level=25
    )

    charmander = PokemonWithLevel(
        name="Charmander",
        types=[Type.FIRE],
        health=270,
        attack=223,
        defense=203,
        sp_attack=240,
        sp_defense=218,
        speed=251,
        ability=Blaze(),
        moves=[flamethrower, quick_attack],
        level=15
    )

    squirtle = PokemonWithLevel(
        name="Squirtle",
        types=[Type.WATER],
        health=292,
        attack=214,
        defense=251,
        sp_attack=218,
        sp_defense=249,
        speed=203,
        moves=[hydro_pump, ice_beam],
        level=15
    )

    bulbasaur = PokemonWithLevel(
        name="Bulbasaur",
        types=[Type.GRASS, Type.POISON],
        health=294,
        attack=216,
        defense=216,
        sp_attack=251,
        sp_defense=251,
        speed=207,
        moves=[razor_leaf, earthquake],
        level=15
    )

    return [pikachu, charmander, squirtle, bulbasaur]


def demo_items():
    """Demonstrate the use of items"""
    print("\n===== ITEM SYSTEM DEMONSTRATION =====\n")

    # Create a Pokemon and some items
    pikachu = create_pokemon_from_data("Pikachu")
    pikachu.current_health = 20  # Set low health for demonstration

    items = create_common_items()
    potion = next(item for item in items if item.name == "Potion")
    super_potion = next(item for item in items if item.name == "Super Potion")
    x_attack = next(item for item in items if item.name == "X Attack")

    # Display initial state
    print(f"{pikachu.name} - HP: {pikachu.current_health}/{pikachu.max_health}")
    print(f"Attack stat: {pikachu.get_modified_stat('attack')}\n")

    # Use a Potion
    print("Using Potion...")
    success, message = potion.use(pikachu)
    print(message)
    print(f"{pikachu.name} - HP: {pikachu.current_health}/{pikachu.max_health}\n")

    # Use a Super Potion
    print("Using Super Potion...")
    success, message = super_potion.use(pikachu)
    print(message)
    print(f"{pikachu.name} - HP: {pikachu.current_health}/{pikachu.max_health}\n")

    # Use X Attack
    print("Using X Attack...")
    success, message = x_attack.use(pikachu)
    print(message)
    print(f"Attack stat: {pikachu.get_modified_stat('attack')}")


def demo_ai():
    """Demonstrate the AI system"""
    print("\n===== AI SYSTEM DEMONSTRATION =====\n")

    # Create Pokemon for the demonstration
    player_pokemon = create_pokemon_from_data("Charizard")
    ai_pokemon = create_pokemon_from_data("Blastoise")

    # Create AI with different difficulty levels
    easy_ai = PokemonAI("easy")
    normal_ai = PokemonAI("normal")
    hard_ai = PokemonAI("hard")

    print(
        f"Player's {player_pokemon.name} (Fire/Flying) vs AI's {ai_pokemon.name} (Water)\n")

    # Demonstrate move selection at different difficulties
    print("Easy AI move selection:")
    for _ in range(3):
        move = easy_ai.select_move(ai_pokemon, player_pokemon)
        print(
            f"Selected {move.name} - Type: {move.type.value}, Power: {move.power}")

    print("\nNormal AI move selection:")
    for _ in range(3):
        move = normal_ai.select_move(ai_pokemon, player_pokemon)
        print(
            f"Selected {move.name} - Type: {move.type.value}, Power: {move.power}")

    print("\nHard AI move selection:")
    for _ in range(3):
        move = hard_ai.select_move(ai_pokemon, player_pokemon)
        print(
            f"Selected {move.name} - Type: {move.type.value}, Power: {move.power}")

    # Demonstrate switching logic
    print("\nAI switching logic:")
    ai_team = [ai_pokemon, create_pokemon_from_data(
        "Venusaur"), create_pokemon_from_data("Pikachu")]

    should_switch, switch_to = normal_ai.should_switch_pokemon(
        ai_pokemon, player_pokemon, ai_team)
    if should_switch:
        print(
            f"AI decided to switch from {ai_pokemon.name} to {ai_team[switch_to].name}")
    else:
        print(f"AI decided to stay with {ai_pokemon.name}")


def demo_evolution():
    """Demonstrate the evolution system"""
    print("\n===== EVOLUTION SYSTEM DEMONSTRATION =====\n")

    # Get evolution data
    evolution_chains, evolution_data = create_sample_evolution_data()

    # Create a Pokemon that can evolve by level
    charmander = PokemonWithLevel(
        name="Charmander",
        types=[Type.FIRE],
        health=270,
        attack=223,
        defense=203,
        sp_attack=240,
        sp_defense=218,
        speed=251,
        moves=[create_move_from_data(
            "Flamethrower"), create_move_from_data("Quick Attack")],
        level=15
    )

    print(f"{charmander.name} (Level {charmander.level})")
    print(
        f"HP: {charmander.health}, Attack: {charmander.attack}, Defense: {charmander.defense}")
    print(
        f"Sp. Attack: {charmander.sp_attack}, Sp. Defense: {charmander.sp_defense}, Speed: {charmander.speed}\n")

    # Level up to evolution
    print("Gaining experience...")
    levels_gained, _ = charmander.gain_exp(100)  # Not enough to evolve
    print(f"Gained {levels_gained} level(s)")
    print(f"{charmander.name} is now level {charmander.level}\n")

    # Check evolution (should not evolve yet)
    success, message, evolved = charmander.check_evolution(
        evolution_chains, evolution_data)
    print(message)

    # Gain more experience to reach evolution level
    print("\nGaining more experience...")
    # Should be enough to reach level 16
    levels_gained, _ = charmander.gain_exp(500)
    print(f"Gained {levels_gained} level(s)")
    print(f"{charmander.name} is now level {charmander.level}\n")

    # Check evolution again (should evolve now)
    success, message, evolved = charmander.check_evolution(
        evolution_chains, evolution_data)
    print(message)

    if evolved:
        print(f"\n{evolved.name} (Level {evolved.level})")
        print(
            f"HP: {evolved.health}, Attack: {evolved.attack}, Defense: {evolved.defense}")
        print(
            f"Sp. Attack: {evolved.sp_attack}, Sp. Defense: {evolved.sp_defense}, Speed: {evolved.speed}")

    # Demonstrate item-based evolution
    print("\n--- Item-based Evolution ---\n")

    # Create Pikachu
    pikachu = PokemonWithLevel(
        name="Pikachu",
        types=[Type.ELECTRIC],
        health=274,
        attack=229,
        defense=174,
        sp_attack=218,
        sp_defense=196,
        speed=306,
        moves=[create_move_from_data(
            "Thunderbolt"), create_move_from_data("Quick Attack")],
        level=30
    )

    print(f"{pikachu.name} (Level {pikachu.level})")
    print(
        f"HP: {pikachu.health}, Attack: {pikachu.attack}, Defense: {pikachu.defense}")
    print(
        f"Sp. Attack: {pikachu.sp_attack}, Sp. Defense: {pikachu.sp_defense}, Speed: {pikachu.speed}\n")

    # Try to evolve without the right item
    success, message, evolved = pikachu.check_evolution(
        evolution_chains, evolution_data, item_name="Fire Stone")
    print(message)

    # Evolve with the right item
    print("\nUsing Thunder Stone...")
    success, message, evolved = pikachu.check_evolution(
        evolution_chains, evolution_data, item_name="Thunder Stone")
    print(message)

    if evolved:
        print(f"\n{evolved.name} (Level {evolved.level})")
        print(
            f"HP: {evolved.health}, Attack: {evolved.attack}, Defense: {evolved.defense}")
        print(
            f"Sp. Attack: {evolved.sp_attack}, Sp. Defense: {evolved.sp_defense}, Speed: {evolved.speed}")


def select_pokemon_team(available_pokemon_count: int = 6) -> List[Pokemon]:
    """Allow the player to select their Pokemon team

    Args:
        available_pokemon_count: Number of Pokemon to choose from

    Returns:
        List[Pokemon]: The selected team of Pokemon
    """
    # Get a list of available Pokemon species from the data
    available_species = list(POKEMON_DATA.keys())

    # Select a random subset if there are too many
    if len(available_species) > available_pokemon_count:
        available_species = random.sample(
            available_species, available_pokemon_count)

    print("\n===== TEAM SELECTION =====\n")
    print("Select your Pokemon team (2-3 Pokemon):")

    # Get player's selection
    selected_team = []
    max_team_size = 3
    remaining_species = available_species.copy()  # Create a copy to modify

    while len(selected_team) < 2:  # Minimum 2 Pokemon
        # Display currently available Pokemon
        print("\nAvailable Pokemon:")
        for i, species in enumerate(remaining_species, 1):
            pokemon_info = POKEMON_DATA[species]
            types_str = "/".join([t.value for t in pokemon_info["types"]])
            print(f"{i}. {species} ({types_str})")

        try:
            selection = input(
                f"\nSelect Pokemon #{len(selected_team) + 1} (1-{len(remaining_species)}): ")
            # Strip any whitespace that might be causing issues
            selection = selection.strip()

            # Try to convert to integer directly
            try:
                index = int(selection) - 1
            except ValueError:
                print("Please enter a valid number.")
                continue

            if 0 <= index < len(remaining_species):
                species = remaining_species[index]
                pokemon = create_pokemon_from_data(species)
                selected_team.append(pokemon)
                print(f"Added {species} to your team!")

                # Show moves
                print(
                    f"  Moves: {', '.join(move.name for move in pokemon.moves)}")

                # Remove the selected species from the remaining options
                remaining_species.pop(index)

                # Ask if they want to add more (if not at max)
                if len(selected_team) >= 2 and len(selected_team) < max_team_size and remaining_species:
                    add_more = input("Add another Pokemon? (y/n): ").lower()
                    if add_more != 'y':
                        break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nYour team: {', '.join(p.name for p in selected_team)}")
    return selected_team


def select_difficulty() -> str:
    """Allow the player to select the AI difficulty level

    Returns:
        str: The selected difficulty level
    """
    print("\n===== DIFFICULTY SELECTION =====\n")
    print("Select AI difficulty:")
    print("1. Easy - AI makes suboptimal decisions 50% of the time")
    print("2. Normal - AI makes suboptimal decisions 20% of the time")
    print("3. Hard - AI makes suboptimal decisions 5% of the time")

    while True:
        try:
            selection = input("\nSelect difficulty (1-3): ")
            index = int(selection)

            if index == 1:
                return "easy"
            elif index == 2:
                return "normal"
            elif index == 3:
                return "hard"
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def demo_battle_with_ai(player_team: List[Pokemon] = None, difficulty: str = None):
    """Demonstrate a battle with the AI system

    Args:
        player_team: The player's Pokemon team (if None, will prompt for selection)
        difficulty: The AI difficulty level (if None, will prompt for selection)
    """
    print("\n===== BATTLE WITH AI DEMONSTRATION =====\n")

    # Get player team if not provided
    if player_team is None:
        player_team = select_pokemon_team()

    # Get difficulty if not provided
    if difficulty is None:
        difficulty = select_difficulty()

    # Create AI Pokemon team (different from player's choices)
    available_species = [species for species in POKEMON_DATA.keys()
                         if species not in [p.name for p in player_team]]
    ai_species = random.sample(available_species, len(player_team))
    ai_team = [create_pokemon_from_data(species) for species in ai_species]

    # Create battle
    battle = Battle(player_team, ai_team)

    # Create AI with selected difficulty
    ai = PokemonAI(difficulty)

    print(f"Player's team: {', '.join(p.name for p in player_team)}")
    print(
        f"AI's team ({difficulty.capitalize()} difficulty): {', '.join(p.name for p in ai_team)}\n")

    print(
        f"Battle begins! {battle.active_player_pokemon.name} vs {battle.active_opponent_pokemon.name}\n")

    # Battle until one team is defeated
    turn = 1
    while True:
        print(f"\n----- Turn {turn} -----")

        # Display current Pokemon and their HP
        player_pokemon = battle.active_player_pokemon
        opponent_pokemon = battle.active_opponent_pokemon
        print(
            f"Your {player_pokemon.name}: {player_pokemon.current_health}/{player_pokemon.max_health} HP")
        print(
            f"AI's {opponent_pokemon.name}: {opponent_pokemon.current_health}/{opponent_pokemon.max_health} HP\n")

        # Player selects a move
        print("Select your move:")
        for i, move in enumerate(player_pokemon.moves, 1):
            print(
                f"{i}. {move.name} (Type: {move.type.value}, Power: {move.power}, Accuracy: {move.accuracy})")

        # Get player's move selection
        player_move = None
        while player_move is None:
            try:
                selection = input(
                    f"Select move (1-{len(player_pokemon.moves)}): ")
                index = int(selection) - 1

                if 0 <= index < len(player_pokemon.moves):
                    player_move = player_pokemon.moves[index]
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        print(f"You selected {player_move.name}")

        # AI selects a move
        ai_move = ai.select_move(opponent_pokemon, player_pokemon)
        print(f"AI selected {ai_move.name}")

        # Execute turn
        messages = battle.execute_turn(player_move, ai_move)
        for msg in messages:
            print(msg)

        # Check if battle is over
        is_over, winner_message = battle.is_battle_over()
        if is_over:
            print(f"\n{winner_message}")
            break

        # Check if player wants to switch Pokemon
        valid_switches = [i for i, p in enumerate(battle.player_pokemon)
                          if p.current_health > 0 and p != battle.active_player_pokemon]

        if valid_switches:
            switch = input("\nDo you want to switch Pokemon? (y/n): ").lower()
            if switch == 'y':
                print("\nSelect Pokemon to switch to:")
                for i, idx in enumerate(valid_switches, 1):
                    pokemon = battle.player_pokemon[idx]
                    print(
                        f"{i}. {pokemon.name} - HP: {pokemon.current_health}/{pokemon.max_health}")

                switch_to = None
                while switch_to is None:
                    try:
                        selection = input(
                            f"Select Pokemon (1-{len(valid_switches)}): ")
                        index = int(selection) - 1

                        if 0 <= index < len(valid_switches):
                            switch_to = valid_switches[index]
                            messages = battle.switch_pokemon(
                                is_player=True, index=switch_to)
                            for msg in messages:
                                print(msg)
                        else:
                            print("Invalid selection. Please try again.")
                    except ValueError:
                        print("Please enter a valid number.")

        # AI might decide to switch Pokemon
        should_switch, switch_to = ai.should_switch_pokemon(
            battle.active_opponent_pokemon,
            battle.active_player_pokemon,
            battle.opponent_pokemon
        )

        if should_switch:
            messages = battle.switch_pokemon(is_player=False, index=switch_to)
            for msg in messages:
                print(msg)

        turn += 1


def main():
    """Main function to run the demo"""
    print("===== POKEMON ENHANCED DEMO =====\n")
    print("This demo showcases the enhanced features of our Pokemon battle simulation:")
    print("1. Team Selection - Choose your Pokemon team")
    print("2. Difficulty Selection - Set the AI difficulty level")
    print("3. Complete Battle - Battle continues until one team is defeated")

    # Ask user which demo to run
    print("\nSelect a demo to run:")
    print("1. Full Battle (Team Selection + Battle)")
    print("2. Item System Demo")
    print("3. AI System Demo")
    print("4. Evolution System Demo")

    while True:
        try:
            selection = input("\nSelect demo (1-4): ")
            choice = int(selection)

            if choice == 1:
                # Run the enhanced battle demo
                demo_battle_with_ai()
                break
            elif choice == 2:
                demo_items()
                break
            elif choice == 3:
                demo_ai()
                break
            elif choice == 4:
                demo_evolution()
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    print("\n===== DEMO COMPLETE =====")
    print("Check out the documentation and data files for more information on the implementation.")


if __name__ == "__main__":
    main()
