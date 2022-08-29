# Decoupling abstraction from implementation to grow them independently

from abc import abstractmethod


class Theme:
    @abstractmethod
    def get_theme_color(self):
        return NotImplementedError('Not implemented')


class DarkTheme(Theme):
    def get_theme_color(self):
        return 'Black'


class LightTheme(Theme):
    def get_theme_color(self):
        return 'White'


class HomePage:
    def __init__(self, theme) -> None:
        self.color = theme.get_theme_color()
        
    def content(self):
        return '<h1>Home page in {} color</h1>'.format(self.color)


class AboutPage:
    def __init__(self, theme) -> None:
        self.color = theme.get_theme_color()

    def content(self):
        return '<h1>About page in {} color</h1>'.format(self.color)


class Website:
    def __init__(self, theme) -> None:
        self.home_page = HomePage(theme)
        self.about_page = AboutPage(theme)

    def get_about_content(self):
        return self.about_page.content()

    def get_home_content(self):
        return self.home_page.content()


if __name__ == '__main__':
    dark_theme = DarkTheme()
    dark_website = Website(dark_theme)

    print(dark_website.get_home_content())  # <h1>Home page in Black color</h1>
    print(dark_website.get_about_content()) # <h1>About page in Black color</h1>

    light_theme = LightTheme()
    light_website = Website(light_theme)

    print(light_website.get_home_content())  # <h1>Home page in White color</h1>
    print(light_website.get_about_content()) # <h1>About page in White color</h1>
