from seleniumpagefactory.Pagefactory import PageFactory


class SearchAnunt2(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "acceptCookiesButton": ('ID', "onetrust-accept-btn-handler"),
        "imobiliare": ('XPATH', "//a[@href='https://www.olx.ro/imobiliare/']"),
        "case": ('XPATH', "//a[@href='https://www.olx.ro/imobiliare/case-de-vanzare/']"),
        "dropdowncamere": ('XPATH', "//div[@data-testid='dropdown-head']"),
        "nrcamere": ('XPATH', "//div/label[@class='checkbox-selected css-18tv77n']")




    }

    def click_accept_cookies(self):
        self.acceptCookiesButton.click()

    def click_imobiliare(self):
        self.imobiliare.click()

    def click_case_de_vanzare(self):
        self.case.click()

    def click_dropdown_camere(self):
        self.dropdowncamere.click()

    def click_nr_camere(self):
        self.nrcamere.click()


