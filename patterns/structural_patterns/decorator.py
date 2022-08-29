# When need to extends a function/class but not through inheritance
# Decorator pattern could be a good choice for you.

# Some of you may think of middleware is an implementation of Decorator pattern
# since they can both help you to make changes before and after a function actual execution.
# However they are somewhat different,
# a fairly good explaination for this can be found here: https://stackoverflow.com/questions/48696631/are-middlewares-an-implementation-of-the-decorator-pattern

# Boiler code: a function receive a call back and execute it
# def decorator_name(func_to_be_decorated):
#     def decorator():
#         do_something_before()

#         func_to_be_decorated()

#         do_something_after()
#         return some_value_if_neccessary

#     return decorator

def upper_text_decorator(func):
    def decorator():
        text = func()
        upper_text = text.upper()
        return upper_text

    return decorator


@upper_text_decorator
def say_hello():
    return 'hello world'


if __name__ == '__main__':
    print(say_hello()) # HELLO WORLD
    