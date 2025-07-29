class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        # Add the x and y components of two vectors
        return self.x + other.x
    
    def __mul__(self, value):
        # Add the x and y components of two vectors
        return self.x * value.x


    def __repr__(self):
        return f"Vector({self.x})"

# Create two vectors
v1 = Vector( 2)
v2 = Vector( 4)

# Add the vectors
v3 = v1 + v2
print(v3) 
v4=v1*v2
print(v4)