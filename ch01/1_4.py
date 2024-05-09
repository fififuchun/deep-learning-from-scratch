class Man:
    def __init__(self, name):
        self.name= name
        print("Init")

    def hello(self):
        print("Hello" + self.name + "!")

    def goodbye(self):
        print("GoodBye" + self.name + "!")

m= Man("World")
m.hello()
m.goodbye()
