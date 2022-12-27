from seleniumpagefactory.Pagefactory import PageFactory

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "acceptCookiesButton": ('ID', "onetrust-accept-btn-handler"),
        "myaccount":('XPATH',"//a[@href='https://www.olx.ro/myaccount/']")
    }

    def click_accept_cookies(self):
        self.acceptCookiesButton.click()

    def click_myaccount(self):
        self.myaccount.click()


