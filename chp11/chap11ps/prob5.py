class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = self.x + other.x,  self.y + other.y, self.z + other.z
        return result

    def __mul__(self, other):
        result = self.x * other.x, self.y * other.y, self.z * other.z
        return result

    def __str__(self):
        return f"vector({self.x}, {self.y},  {self.z})"
    
#Test the impletation
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v2 = vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v2)

print(v1 * v2)
