# In the real world, apdapter can be seen in various forms.
# Ex: Plugs with 3 legs and 2 legs, however, we only have two pronged outlet
# Which means we need some kind of "adapter" to make it compatible with our outlet.

# Adapter pattern means the same thing. 
# There are various type of objects and we need to unify them to fit into and endpoint
# This pattern will convert there methods to a single form.

class Translator: 
    """Adapter class"""
    def __init__(self, object, **adapter_method) -> None:
        self._object = object
        self.__dict__.update(adapter_method) # Add method which need to be adapted to the translator

    def __getattr__(self, __name: str):
        """
        Addtion: Get attribute from original object instead of translator
        """
        return getattr(self._object, __name)

class Vietnamese:
    def __init__(self) -> None:
        self.region = 'Vietnam'

    def vietnamese_hello(self):
        print('Xin chào')


class English:
    def __init__(self) -> None:
        self.language_rank = 1

    def english_hello(self):
        print('Hi')


if __name__ == '__main__':
    vietnam = Vietnamese()
    english = English()

    vietnam_translator = Translator(vietnam, hello=vietnam.vietnamese_hello)
    english_translator = Translator(english, hello=english.english_hello)

    # Now every translator should use only a endpoint method 
    vietnam_translator.hello() # Xin chào
    english_translator.hello() # Hi 

    # Get attribute from translator
    print(vietnam_translator.region) # Vietnam
    print(english_translator.language_rank) # 1
