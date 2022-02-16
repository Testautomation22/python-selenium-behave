from pages.base_page import Page


class HomePage(Page):

    def open(self):
        self.open_page('https://www.gettop.us/')