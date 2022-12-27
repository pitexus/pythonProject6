from seleniumpagefactory.Pagefactory import PageFactory


class Locatie(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "acceptCookiesButton": ('ID', "onetrust-accept-btn-handler"),
        "alegelocatie": ('XPATH', "//input[@type='text']"),
        "submitlocatie": ('XPATH', "//input[@id='submit-searchmain']")
    }

    def click_accept_cookies(self):
        self.acceptCookiesButton.click()

    def click_alege_locatie(self):
        self.alegelocatie.set_text('beius')

    def click_submit_locatie(self):
        self.submitlocatie.click()
