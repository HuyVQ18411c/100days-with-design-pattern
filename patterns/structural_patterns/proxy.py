# Proxy pattern is used to prevent unccessary mass initiation of instances or running an expensive operation.
# There will only an decent number of instance will be created, and operation will only execute when needed.

class View:
    def very_expensive_ops(self):
        print('Executed expensive ops')
        return True


class SecuredView:
    def __init__(self, view) -> None:
        self.view = view
        self.is_authenicated = False

    def authenticate(self, password):
        if password == 'string':
            print('You are authenticated')
            self.is_authenicated = True

    def access(self):
        if self.is_authenicated:
            self.view.very_expensive_ops()
        else:
            print('You are not authenticated')
    

if __name__ == '__main__':
    secure_view = SecuredView(View())
    secure_view.authenticate('falsy_password')
    secure_view.access() # You are not authenticated

    secure_view.authenticate('string')
    secure_view.access()  # You are authenticated & executed expensive ops
