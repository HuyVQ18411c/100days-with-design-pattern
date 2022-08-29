# This pattern may come in handy for objects 
# that relatively have common attributes, and method. 
# Scenario: Users expect multiple objects from a family of objects. 
# Consult below example:

from abc import abstractmethod


class Door:
    def __init__(self, meterial:str) -> None:
        self._meterial = meterial

    @abstractmethod
    def make_door(self):
        raise NotImplementedError('Method has not been implemented')


class WoodDoor(Door):
    """Concrete class"""
    def __init__(self) -> None:
        super().__init__('wood')

    def make_door(self):
        if not self._meterial:
            raise ValueError('Meterial has not been specified')

        print('{} door is being made'.format(self._meterial))

    
class MetalDoor(Door):
    """Concrete class"""
    def __init__(self) -> None:
        super().__init__('metal')

    def make_door(self):
        if not self._meterial:
            raise ValueError('Meterial has not been specified')

        print('{} door is being made'.format(self._meterial))


class DoorFactory:
    door_types = dict(wood=WoodDoor(), metal=MetalDoor())

    def produce_a_door(self, meterial:str='wood'):
        if meterial:
            door = self.door_types[meterial]

        return door
        

if __name__ == '__main__':
    factory = DoorFactory()

    wood_door = DoorFactory().produce_a_door()
    metal_door = DoorFactory().produce_a_door('metal')

    print(wood_door.make_door()) # Wood door is being made
    print(metal_door.make_door()) # Metal door is being made
