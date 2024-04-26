class Superhero:
    def __init__(self, name, secret_identity, points, health):
        self.name = name
        self.secret_identity = secret_identity
        self.points = points
        self.health = health
    
    def is_attacked(self):
        self.health -= 1
        return self.health

    def heal(self):
        self.health += 2
        return self.health

    def gain_points(self):
        self.points += 1
        return self.points

batman = Superhero("Batman", "Bruce Wayne", 3, 5)
