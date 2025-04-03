# Pokemon Battle Simulation: Game Mechanics Documentation

This document explains how our Pokemon battle simulation replicates the mechanics of the real Pokemon games.

## Table of Contents

1. [Core Battle System](#core-battle-system)
2. [Pokemon Stats and Attributes](#pokemon-stats-and-attributes)
3. [Type System](#type-system)
4. [Moves and Damage Calculation](#moves-and-damage-calculation)
5. [Status Effects](#status-effects)
6. [Items and Their Effects](#items-and-their-effects)
7. [Evolution Mechanics](#evolution-mechanics)
8. [AI System](#ai-system)

## Core Battle System

Our battle system replicates the turn-based combat of the Pokemon games with the following features:

### Turn Order

- **Priority System**: Moves have priority values that determine execution order, just like in the real games.
- **Speed Stat**: When moves have the same priority, the Pokemon with the higher Speed stat goes first.
- **Speed Ties**: When Speed stats are equal, a random Pokemon goes first, just like in the real games.

### Battle Flow

1. Players select moves or actions (switch Pokemon, use items)
2. Turn order is determined based on priority and speed
3. Moves are executed in order
4. End-of-turn effects are applied (status damage, etc.)
5. Fainted Pokemon are checked and replaced if necessary

## Pokemon Stats and Attributes

### Base Stats

Each Pokemon has the following stats, matching the real games:

- **HP**: Determines how much damage a Pokemon can take
- **Attack**: Affects damage dealt by physical moves
- **Defense**: Reduces damage taken from physical moves
- **Special Attack**: Affects damage dealt by special moves
- **Special Defense**: Reduces damage taken from special moves
- **Speed**: Determines turn order and affects certain moves

### Stat Modifiers

- Stats can be modified in battle from -6 to +6 stages
- The formula for stat modification matches the games:
  - Positive modifiers: stat × (2 + modifier) / 2
  - Negative modifiers: stat × 2 / (2 - modifier)

### Abilities

Pokemon have unique abilities that provide passive effects or trigger under certain conditions, just like in the real games.

## Type System

Our type system fully implements the 18 Pokemon types and their interactions:

### Type Effectiveness

- **Super Effective** (2x damage): When a move is strong against the defending type
- **Not Very Effective** (0.5x damage): When a move is weak against the defending type
- **No Effect** (0x damage): When a move has no effect on the defending type

### Dual Types

Pokemon can have up to two types, and type effectiveness is calculated by multiplying the effectiveness against each type.

### STAB (Same Type Attack Bonus)

When a Pokemon uses a move that matches one of its types, the move gets a 1.5x damage boost, just like in the real games.

## Moves and Damage Calculation

### Move Categories

- **Physical**: Uses the attacker's Attack and defender's Defense stats
- **Special**: Uses the attacker's Special Attack and defender's Special Defense stats
- **Status**: Does not deal direct damage but causes status effects or stat changes

### Damage Formula

Our damage formula closely replicates the one used in the real games:

```
Damage = ((2 * Level / 5 + 2) * Power * Attack/Defense) / 50 + 2
```

This base damage is then modified by:

- STAB (Same Type Attack Bonus): 1.5x if move type matches Pokemon type
- Type effectiveness: 0x, 0.5x, 1x, or 2x based on type matchups
- Critical hits: 1.5x damage
- Random factor: 0.85 to 1.00 multiplier

### Critical Hits

Moves have a critical hit rate (usually 1/6 chance) that deals 1.5x damage when triggered.

## Status Effects

Our simulation implements the main status conditions from the Pokemon games:

### Primary Status Conditions

- **Burn**: Reduces Attack by 50% and deals damage each turn (1/16 of max HP)
- **Paralysis**: 25% chance to not move and reduces Speed by 50%
- **Poison**: Deals damage each turn (1/8 of max HP)
- **Sleep**: Cannot move for 1-3 turns
- **Freeze**: Cannot move until thawed (20% chance each turn)

### Status Move Effects

Status moves can cause stat changes, confusion, and other effects just like in the real games.

## Items and Their Effects

Our item system replicates the various items found in Pokemon games:

### Medicine Items

- **Potions**: Restore HP by fixed amounts or percentages
- **Status Healers**: Cure specific status conditions
- **Revives**: Restore fainted Pokemon

### Battle Items

- **X Items**: Boost stats during battle
- **Battle Enhancers**: Increase critical hit ratio or other battle effects

### Held Items

Pokemon can hold items that provide passive effects during battle:

- **Stat Boosters**: Increase specific stats
- **Type Enhancers**: Boost moves of a specific type
- **Berries**: Activate under certain conditions (low HP, status effects)
- **Battle Items**: Provide various effects during battle

## Evolution Mechanics

Our evolution system replicates the various ways Pokemon can evolve:

### Evolution Triggers

- **Level-based Evolution**: Pokemon evolve when reaching certain levels
- **Item-based Evolution**: Pokemon evolve when exposed to specific items (stones)
- **Trade Evolution**: Pokemon evolve when traded
- **Friendship Evolution**: Pokemon evolve with high friendship
- **Special Conditions**: Time of day, location, or other special requirements

### Evolution Effects

- Stat increases
- Possible type changes
- New move learning opportunities
- Ability changes

## AI System

Our AI system replicates the behavior of computer-controlled trainers in the Pokemon games:

### Difficulty Levels

- **Easy**: Makes suboptimal decisions frequently
- **Normal**: Makes generally good decisions with occasional mistakes
- **Hard**: Makes optimal decisions most of the time

### Decision Making

The AI considers multiple factors when selecting moves:

- Type effectiveness
- Move power and accuracy
- STAB bonus
- Status effects
- Current HP and stat conditions

### Switching Logic

The AI decides when to switch Pokemon based on:

- Type disadvantages
- Low HP
- Status conditions
- Better matchups with available Pokemon

---

This simulation aims to faithfully recreate the core mechanics of the Pokemon games while providing a simplified and educational implementation. While not every feature from the games is implemented (such as weather effects, terrain, or all abilities), the core battle system closely follows the rules and formulas used in the official Pokemon games.
