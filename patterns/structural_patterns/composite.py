# A software is form from many modules. A React app is form from many components.
# Each component has their own role however they could share many properties.
# The idea of composite pattern is to treat those objects as a single instance. 

class Component:
    def __init__(self, name) -> None:
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)

    def show(self):
        print('Showing {} elements:'.format(self.name), self.elements)


class HomeComponent(Component):
    pass


class AboutComponent(Component):
    pass


class Website:
    def __init__(self) -> None:
        self.components = []

    def add_component(self ,component):
        self.components.append(component)

    def show_components(self):
        for comp in self.components:
            comp.show()


if __name__ == '__main__':
    home_component = HomeComponent('home')
    home_component.add_element('<h1>Home</h1>')

    about_component = AboutComponent('about')
    about_component.add_element('<h1>About</h1>')


    website = Website()
    website.add_component(home_component)
    website.add_component(about_component)

    website.show_components()

