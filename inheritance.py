class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("inhale,exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swim")


nemo = Fish()
print(nemo.breathe())