class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale , Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe_in(self):
        super().breathe()
        print("method can be inherited using super().method()")
        print("breathing underwater ")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe() # inheriting th method directly through 'super().__init__()'
nemo.breathe_in() # inheriting th method directly from another method in Fish class through 'super().method()'
