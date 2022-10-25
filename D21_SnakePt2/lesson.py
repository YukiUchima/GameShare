class Animal:
    def __init__(self):
        self.num_eyes = 2

    def intel(self):
        self.intelligence = "high"
        print(f"Intel level: {self.intelligence}")

    def breathe(self):
        print("Inhale, Exhale...")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        # super().breathe()
        print("breathing underwater.")

    def intel(self):
        self.intelligence = "Unmeasured"
        print(self.intelligence)

    def swim(self):
        print("moving in water...")


nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.intel()
