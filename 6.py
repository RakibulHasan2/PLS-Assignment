class Union:
    def __init__(self):
        self.i = None
        self.f = None
        self.s = None

    # Methods to set values for different types
    def set_int(self, value):
        self.i = value
        self.f = None
        self.s = None

    def set_float(self, value):
        self.f = value
        self.i = None
        self.s = None

    def set_string(self, value):
        self.s = value
        self.i = None
        self.f = None

    # Method to display the current value
    def display(self):
        if self.i is not None:
            print(f"Integer: {self.i}")
        elif self.f is not None:
            print(f"Float: {self.f}")
        elif self.s is not None:
            print(f"String: {self.s}")
        else:
            print("No value set.")

# Testing the union-like class
u = Union()
u.set_int(10)
u.display()

u.set_float(3.14)
u.display()

u.set_string("PLS Assignments")
u.display()
