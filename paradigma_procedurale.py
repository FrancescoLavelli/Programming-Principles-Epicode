"""Paradigma
Procedurale
ad Oggetti
Funzionale
we use it when we need a code that is releiable, predictable, performant, easy to test. TO do that it uses pure function. A pure function is a function that given the same input will always return the same output. And thst does not have side effects. So she does not modify the outside world, outside scope. It does not modify variables, we use recursions instead of loops.
"""

# *paradigma procedurale*


def get_even_numbers(numbers):
    # return [number for number in numbers if number % 2 == 0]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            print(f"Found even number: {number}")
            even_numbers.append(number)
    numbers.clear()
    numbers.extend(even_numbers)
    print(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_even_numbers(numbers)

# *paradigma object*


class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_even_numbers(self):
        even_numbers = []
        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
            self.numbers = even_numbers


processor = NumberProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
processor.get_even_numbers()
print(processor)


# *paradigma funzionale*

def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # tuple not list
print(get_even_numbers(numbers))
