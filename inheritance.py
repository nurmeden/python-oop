class Geom:
    name = "Geom"

class Line(Geom):
    def draw(self):
        print("Рисование линии")
    
    def set_coord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

g = Geom()
l = Line()
print(l.name)
