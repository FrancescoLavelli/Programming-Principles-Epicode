from typing import List, Tuple, Optional
import random
from PokemonEnhanced import Pokemon, Move, Type, TYPE_CHART, StatusEffect, MoveCategory


class PokemonAI:
    """AI system for controlling opponent Pokemon in battles"""

    def __init__(self, difficulty: str = "normal"):
        """Initialize the AI with a difficulty level

        Args:
            difficulty: The AI difficulty level ("easy", "normal", or "hard")
        """
        self.difficulty = difficulty.lower()
        # Chance of making optimal decisions based on difficulty
        self.optimal_chance = {
            "easy": 0.5,    # 50% chance to make optimal move
            "normal": 0.8,  # 80% chance to make optimal move
            "hard": 0.95    # 95% chance to make optimal move
        }.get(self.difficulty, 0.8)

    def select_move(self, attacker: Pokemon, defender: Pokemon) -> Move:
        """Select the best move for the AI-controlled Pokemon

        Args:
            attacker: The AI-controlled Pokemon
            defender: The player's Pokemon

        Returns:
            Move: The selected move
        """
        # If no moves available, return None
        if not attacker.moves:
            return None

        # Random chance to make a suboptimal move based on difficulty
        if random.random() > self.optimal_chance:
            return random.choice(attacker.moves)

        # Calculate effectiveness and expected damage for each move
        move_scores = []
        for move in attacker.moves:
            score = self._evaluate_move(move, attacker, defender)
            move_scores.append((move, score))

        # Sort moves by score (highest first)
        move_scores.sort(key=lambda x: x[1], reverse=True)

        # Return the highest-scoring move
        return move_scores[0][0]

    def _evaluate_move(self, move: Move, attacker: Pokemon, defender: Pokemon) -> float:
        """Evaluate a move's effectiveness

        Args:
            move: The move to evaluate
            attacker: The AI-controlled Pokemon
            defender: The player's Pokemon

        Returns:
            float: A score representing the move's effectiveness
        """
        score = 0.0

        # Base score on move power
        score += move.power

        # Adjust for accuracy
        score *= move.accuracy / 100

        # Adjust for STAB (Same Type Attack Bonus)
        if move.type in attacker.types:
            score *= 1.5

        # Adjust for type effectiveness
        type_multiplier = 1.0
        for defender_type in defender.types:
            if move.type in TYPE_CHART and defender_type in TYPE_CHART[move.type]:
                type_multiplier *= TYPE_CHART[move.type][defender_type]
        score *= type_multiplier

        # Prioritize super effective moves
        if type_multiplier > 1.0:
            score *= 1.2

        # Prioritize status moves if opponent doesn't have a status condition
        if move.category == MoveCategory.STATUS and defender.status_effect == StatusEffect.NONE:
            # Status moves get a base score since they have 0 power
            base_status_score = 60  # Equivalent to a medium-power attack

            # Adjust based on the specific status effect
            if move.status_effect == StatusEffect.PARALYSIS:
                # Paralysis is very valuable for speed reduction
                score = base_status_score * 1.3
            elif move.status_effect == StatusEffect.BURN and move.category == MoveCategory.PHYSICAL:
                # Burn is great against physical attackers
                score = base_status_score * 1.4
            elif move.status_effect == StatusEffect.POISON:
                # Poison for damage over time
                score = base_status_score * 1.2
            elif move.status_effect == StatusEffect.SLEEP:
                # Sleep prevents actions
                score = base_status_score * 1.5
            elif move.status_effect == StatusEffect.FREEZE:
                # Freeze is powerful but unreliable
                score = base_status_score * 1.3
            else:
                score = base_status_score

            # Adjust by status chance
            score *= move.status_chance / 100

        # Prioritize high-priority moves when low on health
        if attacker.current_health < attacker.max_health * 0.3 and move.priority > 0:
            score *= 1.3

        # Add a small random factor to avoid predictability
        score *= random.uniform(0.95, 1.05)

        return score

    def should_switch_pokemon(self, current: Pokemon, opponent: Pokemon,
                              available_pokemon: List[Pokemon]) -> Tuple[bool, Optional[int]]:
        """Decide whether the AI should switch Pokemon

        Args:
            current: The current AI-controlled Pokemon
            opponent: The player's Pokemon
            available_pokemon: List of available Pokemon to switch to

        Returns:
            Tuple[bool, Optional[int]]: (should_switch, index_to_switch_to)
        """
        # Don't switch if no other Pokemon available
        valid_switches = [i for i, p in enumerate(available_pokemon)
                          if p.current_health > 0 and p != current]
        if not valid_switches:
            return False, None

        # Calculate current matchup score
        current_matchup_score = self._evaluate_matchup(current, opponent)

        # Switch if current Pokemon is at a severe disadvantage or low health
        disadvantage_threshold = -0.5  # Negative means disadvantage
        low_health_threshold = 0.25    # 25% of max health

        is_disadvantaged = current_matchup_score < disadvantage_threshold
        is_low_health = current.current_health < current.max_health * low_health_threshold

        # Random chance to make suboptimal switching decision based on difficulty
        if random.random() > self.optimal_chance:
            # Easy/Normal AI might not switch even when advantageous
            if self.difficulty == "easy":
                return random.random() < 0.3, random.choice(valid_switches) if random.random() < 0.3 else None
            elif self.difficulty == "normal":
                return (is_disadvantaged or is_low_health) and random.random() < 0.7, \
                    random.choice(valid_switches) if (
                        is_disadvantaged or is_low_health) and random.random() < 0.7 else None

        # If current Pokemon is at a disadvantage or low health, consider switching
        if is_disadvantaged or is_low_health:
            # Find the best matchup among available Pokemon
            best_matchup_score = current_matchup_score
            best_switch_index = None

            for idx in valid_switches:
                potential_switch = available_pokemon[idx]
                matchup_score = self._evaluate_matchup(
                    potential_switch, opponent)

                # Only switch if the new matchup is better
                if matchup_score > best_matchup_score:
                    best_matchup_score = matchup_score
                    best_switch_index = idx

            # If we found a better matchup, switch to it
            if best_switch_index is not None:
                return True, best_switch_index

        return False, None

    def _evaluate_matchup(self, pokemon: Pokemon, opponent: Pokemon) -> float:
        """Evaluate how well a Pokemon matches up against an opponent

        Args:
            pokemon: The Pokemon to evaluate
            opponent: The opponent Pokemon

        Returns:
            float: A score representing the matchup (-1 to 1, higher is better)
        """
        score = 0.0

        # Evaluate type effectiveness in both directions
        # How effective are my attacks against opponent?
        attack_effectiveness = 1.0
        for move in pokemon.moves:
            if move.category != MoveCategory.STATUS:
                move_effectiveness = 1.0
                for opponent_type in opponent.types:
                    if move.type in TYPE_CHART and opponent_type in TYPE_CHART[move.type]:
                        move_effectiveness *= TYPE_CHART[move.type][opponent_type]
                attack_effectiveness = max(
                    attack_effectiveness, move_effectiveness)

        # How effective are opponent's attacks against me?
        defense_vulnerability = 1.0
        for move in opponent.moves:
            if move.category != MoveCategory.STATUS:
                move_vulnerability = 1.0
                for my_type in pokemon.types:
                    if move.type in TYPE_CHART and my_type in TYPE_CHART[move.type]:
                        move_vulnerability *= TYPE_CHART[move.type][my_type]
                defense_vulnerability = max(
                    defense_vulnerability, move_vulnerability)

        # Combine attack effectiveness and defense vulnerability
        # Higher attack effectiveness is good, higher defense vulnerability is bad
        score += (attack_effectiveness - 1.0) * 0.5  # Range: -0.5 to 1.0
        score -= (defense_vulnerability - 1.0) * 0.5  # Range: -1.0 to 0.5

        # Consider speed advantage
        if pokemon.get_modified_speed() > opponent.get_modified_speed():
            score += 0.2
        else:
            score -= 0.1

        # Consider health percentage
        pokemon_health_percent = pokemon.current_health / pokemon.max_health
        score += (pokemon_health_percent - 0.5) * 0.4  # Range: -0.2 to 0.2

        return score
