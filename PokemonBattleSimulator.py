import random
from typing import List, Dict, Any, Optional, Tuple

# Import from our Pokemon modules
from PokemonEnhanced import Type, MoveCategory, StatusEffect, Move, Pokemon, Battle, Ability
from pokemon_items import Item, MedicineItem, BattleItem, HeldItem, create_common_items
from pokemon_ai import PokemonAI

# Define the missing Bite move and other moves that might be missing
BITE_MOVE = Move(
    name="Bite",
    type=Type.DARK,
    category=MoveCategory.PHYSICAL,
    power=60,
    accuracy=100,
    status_effect=StatusEffect.NONE,
    status_chance=0
)

SKULL_BASH_MOVE = Move(
    name="Skull Bash",
    type=Type.NORMAL,
    category=MoveCategory.PHYSICAL,
    power=130,
    accuracy=100,
    status_effect=StatusEffect.NONE,
    status_chance=0
)

# Dictionary of predefined Pokemon for the simulator
PREDEFINED_POKEMON = {
    "Pikachu": Pokemon(
        name="Pikachu",
        types=[Type.ELECTRIC],
        health=274,
        attack=229,
        defense=174,
        sp_attack=218,
        sp_defense=196,
        speed=306,
        moves=[
            Move("Thunder Shock", Type.ELECTRIC, MoveCategory.SPECIAL, 40,
                 100, status_effect=StatusEffect.PARALYSIS, status_chance=10),
            Move("Quick Attack", Type.NORMAL,
                 MoveCategory.PHYSICAL, 40, 100, priority=1),
            Move("Thunderbolt", Type.ELECTRIC, MoveCategory.SPECIAL, 90,
                 100, status_effect=StatusEffect.PARALYSIS, status_chance=10),
            Move("Thunder Wave", Type.ELECTRIC, MoveCategory.STATUS, 0,
                 90, status_effect=StatusEffect.PARALYSIS, status_chance=100)
        ]
    ),
    "Charizard": Pokemon(
        name="Charizard",
        types=[Type.FIRE, Type.FLYING],
        health=360,
        attack=267,
        defense=254,
        sp_attack=348,
        sp_defense=268,
        speed=299,
        moves=[
            Move("Flamethrower", Type.FIRE, MoveCategory.SPECIAL, 90,
                 100, status_effect=StatusEffect.BURN, status_chance=10),
            Move("Wing Attack", Type.FLYING, MoveCategory.PHYSICAL, 60, 100),
            Move("Fire Blast", Type.FIRE, MoveCategory.SPECIAL, 110,
                 85, status_effect=StatusEffect.BURN, status_chance=10),
            Move("Air Slash", Type.FLYING, MoveCategory.SPECIAL, 75, 95)
        ]
    ),
    "Blastoise": Pokemon(
        name="Blastoise",
        types=[Type.WATER],
        health=362,
        attack=264,
        defense=298,
        sp_attack=295,
        sp_defense=339,
        speed=254,
        moves=[
            Move("Water Gun", Type.WATER, MoveCategory.SPECIAL, 40, 100),
            Move("Hydro Pump", Type.WATER, MoveCategory.SPECIAL, 110, 80),
            BITE_MOVE,
            SKULL_BASH_MOVE
        ]
    ),
    "Venusaur": Pokemon(
        name="Venusaur",
        types=[Type.GRASS, Type.POISON],
        health=364,
        attack=262,
        defense=263,
        sp_attack=300,
        sp_defense=300,
        speed=260,
        moves=[
            Move("Razor Leaf", Type.GRASS,
                 MoveCategory.PHYSICAL, 55, 95, critical_rate=4),
            Move("Solar Beam", Type.GRASS, MoveCategory.SPECIAL, 120, 100),
            Move("Sleep Powder", Type.GRASS, MoveCategory.STATUS, 0, 75,
                 status_effect=StatusEffect.SLEEP, status_chance=100),
            Move("Poison Powder", Type.POISON, MoveCategory.STATUS, 0,
                 75, status_effect=StatusEffect.POISON, status_chance=100)
        ]
    ),
    "Jigglypuff": Pokemon(
        name="Jigglypuff",
        types=[Type.NORMAL, Type.FAIRY],
        health=340,
        attack=185,
        defense=120,
        sp_attack=185,
        sp_defense=125,
        speed=120,
        moves=[
            Move("Sing", Type.NORMAL, MoveCategory.STATUS, 0, 55,
                 status_effect=StatusEffect.SLEEP, status_chance=100),
            Move("Pound", Type.NORMAL, MoveCategory.PHYSICAL, 40, 100),
            Move("Body Slam", Type.NORMAL, MoveCategory.PHYSICAL, 85, 100,
                 status_effect=StatusEffect.PARALYSIS, status_chance=30),
            Move("Double Slap", Type.NORMAL, MoveCategory.PHYSICAL, 15, 85)
        ]
    ),
    "Gengar": Pokemon(
        name="Gengar",
        types=[Type.GHOST, Type.POISON],
        health=324,
        attack=251,
        defense=236,
        sp_attack=394,
        sp_defense=266,
        speed=350,
        moves=[
            Move("Shadow Ball", Type.GHOST, MoveCategory.SPECIAL, 80, 100),
            Move("Sludge Bomb", Type.POISON, MoveCategory.SPECIAL, 90,
                 100, status_effect=StatusEffect.POISON, status_chance=30),
            Move("Hypnosis", Type.PSYCHIC, MoveCategory.STATUS, 0, 60,
                 status_effect=StatusEffect.SLEEP, status_chance=100),
            Move("Dream Eater", Type.PSYCHIC, MoveCategory.SPECIAL, 100, 100)
        ]
    )
}


def get_integer_input(prompt: str, min_value: int, max_value: int) -> int:
    """
    Get an integer input from the user with validation.

    Args:
        prompt: The prompt to display to the user
        min_value: The minimum acceptable value
        max_value: The maximum acceptable value

    Returns:
        int: The validated integer input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            value = int(user_input)

            if min_value <= value <= max_value:
                return value
            else:
                print(
                    f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_yes_no_input(prompt: str) -> bool:
    """
    Get a yes/no input from the user.

    Args:
        prompt: The prompt to display to the user

    Returns:
        bool: True for yes, False for no
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")


def select_pokemon_team() -> List[Pokemon]:
    """
    Allow the player to select their Pokemon team.

    Returns:
        List[Pokemon]: The selected team of Pokemon
    """
    # Get a list of available Pokemon species
    available_pokemon = list(PREDEFINED_POKEMON.keys())

    print("\n===== TEAM SELECTION =====\n")
    print("Select your Pokemon team (2-3 Pokemon):")

    # Get player's selection
    selected_team = []
    max_team_size = 3
    remaining_pokemon = available_pokemon.copy()  # Create a copy to modify

    # Keep selecting Pokemon until we have at least 2 and at most max_team_size
    while len(selected_team) < max_team_size:
        # Display currently available Pokemon
        print("\nAvailable Pokemon:")
        for i, species in enumerate(remaining_pokemon, 1):
            pokemon = PREDEFINED_POKEMON[species]
            types_str = "/".join([t.value for t in pokemon.types])
            print(f"{i}. {species} ({types_str})")

        # Get user selection with proper validation
        index = get_integer_input(f"\nSelect Pokemon #{len(selected_team) + 1} (1-{len(remaining_pokemon)}): ",
                                  1, len(remaining_pokemon)) - 1

        species = remaining_pokemon[index]
        pokemon = PREDEFINED_POKEMON[species]
        selected_team.append(pokemon)
        print(f"Added {species} to your team!")

        # Show moves
        print(f"  Moves: {', '.join(move.name for move in pokemon.moves)}")

        # Remove the selected species from the remaining options
        remaining_pokemon.pop(index)

        # Ask if they want to add more (if not at max)
        if len(selected_team) >= 2 and len(selected_team) < max_team_size and remaining_pokemon:
            add_more = get_yes_no_input("Add another Pokemon? (y/n): ")
            if not add_more:
                break
            # If user wants to add another Pokemon, continue the loop
            # The loop will automatically continue to select the next Pokemon

    print(f"\nYour team: {', '.join(p.name for p in selected_team)}")
    return selected_team


def select_difficulty() -> str:
    """
    Allow the player to select the AI difficulty level.

    Returns:
        str: The selected difficulty level
    """
    print("\n===== DIFFICULTY SELECTION =====\n")
    print("Select AI difficulty:")
    print("1. Easy - AI makes suboptimal decisions 50% of the time")
    print("2. Normal - AI makes suboptimal decisions 20% of the time")
    print("3. Hard - AI makes suboptimal decisions 5% of the time")

    selection = get_integer_input("\nSelect difficulty (1-3): ", 1, 3)

    if selection == 1:
        return "easy"
    elif selection == 2:
        return "normal"
    else:  # selection == 3
        return "hard"


def battle_with_ai(player_team: List[Pokemon] = None, difficulty: str = None):
    """
    Run a battle with the AI system.

    Args:
        player_team: The player's Pokemon team (if None, will prompt for selection)
        difficulty: The AI difficulty level (if None, will prompt for selection)
    """
    print("\n===== POKEMON BATTLE SIMULATOR =====\n")

    # Get player team if not provided
    if player_team is None:
        player_team = select_pokemon_team()

    # Get difficulty if not provided
    if difficulty is None:
        difficulty = select_difficulty()

    # Create AI Pokemon team (different from player's choices)
    available_pokemon = [name for name in PREDEFINED_POKEMON.keys()
                         if name not in [p.name for p in player_team]]
    ai_pokemon_names = random.sample(available_pokemon, len(player_team))
    ai_team = [PREDEFINED_POKEMON[name] for name in ai_pokemon_names]

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

        # Get player's move selection with validation
        move_index = get_integer_input(f"Select move (1-{len(player_pokemon.moves)}): ",
                                       1, len(player_pokemon.moves)) - 1
        player_move = player_pokemon.moves[move_index]

        print(f"You selected {player_move.name}")

        # AI selects a move
        ai_move = ai.select_move(opponent_pokemon, player_pokemon)
        print(f"AI selected {ai_move.name}")

        # Execute turn
        messages = battle.execute_turn(player_move, ai_move)
        for msg in messages:
            print(msg)

        # Check if player's active Pokemon has fainted
        if battle.active_player_pokemon.current_health <= 0:
            # Find valid Pokemon to switch to
            valid_switches = [i for i, p in enumerate(battle.player_pokemon)
                              if p.current_health > 0]

            if valid_switches:
                print(
                    "\nYour active Pokemon has fainted! You must switch to another Pokemon.")
                print("\nSelect Pokemon to switch to:")
                for i, idx in enumerate(valid_switches, 1):
                    pokemon = battle.player_pokemon[idx]
                    print(
                        f"{i}. {pokemon.name} - HP: {pokemon.current_health}/{pokemon.max_health}")

                switch_index = get_integer_input(f"Select Pokemon (1-{len(valid_switches)}): ",
                                                 1, len(valid_switches)) - 1
                switch_to = valid_switches[switch_index]
                messages = battle.switch_pokemon(
                    is_player=True, index=switch_to)
                for msg in messages:
                    print(msg)

        # Check if AI's active Pokemon has fainted
        if battle.active_opponent_pokemon.current_health <= 0:
            # Find valid Pokemon for AI to switch to
            valid_switches = [i for i, p in enumerate(battle.opponent_pokemon)
                              if p.current_health > 0 and p != battle.active_opponent_pokemon]

            if valid_switches:
                # AI automatically switches to the first available Pokemon
                switch_to = valid_switches[0]
                messages = battle.switch_pokemon(
                    is_player=False, index=switch_to)
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
            switch = get_yes_no_input(
                "\nDo you want to switch Pokemon? (y/n): ")
            if switch:
                print("\nSelect Pokemon to switch to:")
                for i, idx in enumerate(valid_switches, 1):
                    pokemon = battle.player_pokemon[idx]
                    print(
                        f"{i}. {pokemon.name} - HP: {pokemon.current_health}/{pokemon.max_health}")

                switch_index = get_integer_input(f"Select Pokemon (1-{len(valid_switches)}): ",
                                                 1, len(valid_switches)) - 1
                switch_to = valid_switches[switch_index]
                messages = battle.switch_pokemon(
                    is_player=True, index=switch_to)
                for msg in messages:
                    print(msg)

        # AI might decide to switch Pokemon if its active Pokemon hasn't fainted
        if battle.active_opponent_pokemon.current_health > 0:
            should_switch, switch_to = ai.should_switch_pokemon(
                battle.active_opponent_pokemon,
                battle.active_player_pokemon,
                battle.opponent_pokemon
            )

            if should_switch:
                messages = battle.switch_pokemon(
                    is_player=False, index=switch_to)
                for msg in messages:
                    print(msg)

        turn += 1


def demo_items():
    """
    Demonstrate the use of items.
    """
    print("\n===== ITEM SYSTEM DEMONSTRATION =====\n")

    # Create a Pokemon and some items
    pikachu = PREDEFINED_POKEMON["Pikachu"]
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
    """
    Demonstrate the AI system.
    """
    print("\n===== AI SYSTEM DEMONSTRATION =====\n")

    # Create Pokemon for the demonstration
    player_pokemon = PREDEFINED_POKEMON["Charizard"]
    ai_pokemon = PREDEFINED_POKEMON["Blastoise"]

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
    ai_team = [ai_pokemon, PREDEFINED_POKEMON["Venusaur"],
               PREDEFINED_POKEMON["Pikachu"]]

    should_switch, switch_to = normal_ai.should_switch_pokemon(
        ai_pokemon, player_pokemon, ai_team)
    if should_switch:
        print(
            f"AI decided to switch from {ai_pokemon.name} to {ai_team[switch_to].name}")
    else:
        print(f"AI decided to stay with {ai_pokemon.name}")


def main():
    """
    Main function to run the Pokemon Battle Simulator.
    """
    print("===== POKEMON BATTLE SIMULATOR =====\n")
    print("Welcome to the Pokemon Battle Simulator!")
    print("This program allows you to battle against an AI opponent with your chosen Pokemon team.")

    # Ask user which demo to run
    print("\nSelect an option:")
    print("1. Full Battle (Team Selection + Battle)")
    print("2. Item System Demo")
    print("3. AI System Demo")

    selection = get_integer_input("\nSelect option (1-3): ", 1, 3)

    if selection == 1:
        battle_with_ai()
    elif selection == 2:
        demo_items()
    else:  # selection == 3
        demo_ai()

    print("\n===== SIMULATION COMPLETE =====")


if __name__ == "__main__":
    main()
