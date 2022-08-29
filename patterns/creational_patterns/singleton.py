# When you want to allow only one instance can be initiated from a class. 
# When you want to share states from an instance in various objects/places (Ex: Cache object)
# When you want a global variable in an OOP way :)
# Singleton pattern is a good way to consider.

class SingletonQueue:
    _current_queue = {
        'key': {}
    }
    def __init__(self) -> None:
        self.queue = self._current_queue


if __name__ == '__main__':
    queue_one = SingletonQueue().queue
    queue_two = SingletonQueue().queue

    print(queue_one) # {'key': {}}
    print(queue_two) # {'key': {}}

    queue_one.update({'key': {1: 'key_1', 2: 'key_2'}})

    print(queue_two) # {'key': {1: 'key_1', 2: 'key_2'}}
