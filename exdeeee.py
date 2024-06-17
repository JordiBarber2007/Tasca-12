class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return f'{self.brand} {self.model}'

    def start_engine(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def description(self):
        return f'{self.brand} {self.model}, {self.doors} doors'

    def start_engine(self):
        return f'{self.description()} engine started with a key'

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def description(self):
        return f'{self.brand} {self.model}, {self.capacity} tons capacity'

    def start_engine(self):
        return f'{self.description()} engine started with a button'

def pex4():

    # Creación de instancias de vehículos
    car1 = Car('Toyota', 'Corolla', 4)
    truck1 = Truck('Volvo', 'FH16', 25)

    # Listado de vehículos
    vehicles = ["car1", "truck1"]

    # Usando polimorfismo para iniciar motores de vehículos
    for e in vehicles:
        e.start_engine()