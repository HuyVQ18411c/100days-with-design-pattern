# Telescoping Constructor (anti-pattern)
# A single class hold the responsibilty for creating many instances which are parts of a big/complex object.
# Builder pattern will help to solve this problem by spliting logics into multiple classes/methods.

from abc import abstractmethod


class Car:
    def __init__(self) -> None:
        self.tires = None
        self.model = None
        self.engine = None


class CarFactory:
    def __init__(self, builder) -> None:
        self._builder = builder

    def produce(self):
        self._builder.create_new_car()
        self._builder.add_tires()
        self._builder.add_model()
        self._builder.add_engine()

    def get_car(self):
        if self._builder.car:
            return self._builder.car
        else:
            print('No car has been produced')
            return

class CarBuilder:
    """Abstract builder"""
    def __init__(self) -> None:
        self.car = None
    
    def create_new_car(self):
        self.car = Car()
        return self.car

    @abstractmethod
    def add_tires(self):
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def add_model(self):
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def add_engine(self):
        raise NotImplementedError('Not implemented')


class TeslaBuilder(CarBuilder):
    """Concreate Builder"""
    def add_tires(self):
        self.car.tires = 'Modern tires'

    def add_model(self):
        self.car.model = 'Tesla X3000'
    
    def add_engine(self):
        self.car.engine = 'VX3000'

# The more car model you have, you can easily add more Builder for that Car.


if __name__ == '__main__':
    tesla_builder = TeslaBuilder()
    factory = CarFactory(builder=tesla_builder)
    factory.produce()
    car = factory.get_car()

    print('Car model: {}, Type of tires: {}, Engine: {}'.format(
            car.model, car.tires, car.engine
        )
    ) # Car model: Tesla X3000, Type of tires: Modern tires, Engine: VX3000
