class Shape():
    def __init__(self, shape):
        self.shape = shape

    def get_area_info(self):
        print(f"I am generic {self.shape}")

class Circle(Shape):
    def __init__(self, shape, radius):
        super().__init__(shape)
        self.radius = radius

    def get_area_info(self):
        print(f"I am a {self.shape} with a {self.radius}")    





S1 = Shape("shape")
S1.get_area_info()

S2 = Circle("circle", "radius")
S2.get_area_info()