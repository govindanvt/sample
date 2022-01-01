class Car:
    def __init__(self,name):
        self.name=name
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Sportscar(Car):
    def drive(self):
        return 'Sportscar Driving smoothly'
    def stop(self):
        return 'Sportscar Applying power break'
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because they heavly loaded'
    def stop(self):
        return 'Truck breaking carefully'
cars=[Truck('Bananatruck '),Truck('Orangetruck '),Sportscar('Benz:S Class ')]
for c in cars:
    print(c.name+": "+c.drive()+": "+c.stop())