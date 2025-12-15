class Circle():
    def draw(self):
        return "Drawing a circle"
    
class Sqaure():
    def draw(self):
        return "Drawing a sqaure"
    
def render(shape):
    return shape.draw()  


S1 = Circle()
S2 = Sqaure()

print(render(S1))
print(render(S2))

