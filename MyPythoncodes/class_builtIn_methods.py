class Colors:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __eq__(self, value: object) -> bool:
        pass
    def __add__(self):
        pass
    def __len__(self):
        pass
# iter,next,ietItem,call


class InfiniteEvenNumbers:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 2
        return self.number
        

# Using the infinite iterator
even_numbers = InfiniteEvenNumbers()
for num in even_numbers:
    if num > 10:  # Breaking condition
        break
    print(num)


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create a callable object
double = Multiplier(2)
triple = Multiplier(3)

# Use it like a function
print(double(10))  # Outputs 20 (10 * 2)
print(triple(10))  # Outputs 30 (10 * 3)
