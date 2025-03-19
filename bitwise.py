""" **Bitwise Operators Explained**

Bitwise operators work on the individual bits of binary numbers. They're commonly used in low-level programming, network protocols, embedded systems, and performance-critical code.

## Basic Bitwise Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | Sets each bit to 1 if both corresponding bits are 1 |
| `\|` | OR | Sets each bit to 1 if at least one corresponding bit is 1 |
| `^` | XOR (Exclusive OR) | Sets each bit to 1 if only one corresponding bit is 1 |
| `~` | NOT | Inverts all bits (turns 1 to 0 and 0 to 1) |
| `<<` | Left Shift | Shifts bits left by a specified number of positions |
| `>>` | Right Shift | Shifts bits right by a specified number of positions |

"""
bit1 = 0b1011
bit2 = 0b0101
bit3 = bit1 ^ bit2
print(bin(bit3))

