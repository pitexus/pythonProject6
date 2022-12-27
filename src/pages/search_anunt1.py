from seleniumpagefactory.Pagefactory import PageFactory


class SearchAnunt(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "acceptCookiesButton": ('ID', "onetrust-accept-btn-handler"),
        "auto": ('XPATH', "//a[@href='https://www.olx.ro/auto-masini-moto-ambarcatiuni/']"),
        "autoturisme": ('XPATH', "//a[@href='https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/']"),
        "categorie": ('XPATH', "//div[@class='css-12snx2d']"),
        "model": ('XPATH', "//div[@class='css-1a9sj2a']")

    }

    def click_accept_cookies(self):
        self.acceptCookiesButton.click()

    def click_automoto(self):
        self.auto.click()

    def click_autoturisme(self):
        self.autoturisme.click()

    def click_categorie(self):
        self.categorie.click()

    def click_model(self):
        self.model.click()
