class Rabbit:
    tail = "fluffy"
    ears = "long"

    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("hop")
    
    def speak(self):
        print("My name is {}".format(self.name))
    
print(Rabbit.tail)
print(Rabbit.ears)

bugs = Rabbit("Bugs")
print(bugs.name)

thumper = Rabbit("Thumper")
print(thumper.name)

thumper.run()
