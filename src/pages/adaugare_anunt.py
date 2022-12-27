from seleniumpagefactory.Pagefactory import PageFactory


class AdaugareAnunt(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "acceptCookiesButton": ('ID', "onetrust-accept-btn-handler"),
        "adaugareanunt": ('XPATH', "//a[@href='https://www.olx.ro/d/adauga-anunt/?bs=homepage_adding']"),
        "email": ('XPATH', "//input[@name='username']"),
        "password": ('XPATH', "//input[@type='password']"),

        "submit": ('XPATH', "//button[@type='submit']"),
        "alegecategoria": ('XPATH', "//div[@class='css-5pblnn']"),
        "electronice": ('XPATH', "//button[@to='/electronice-si-electrocasnice/']"),
        "telefoane": ('XPATH', "//li[@data-categoryid='101']"),
        "iphone": ('XPATH', "//li[@data-categoryid='948']"),
        "clickdescriereiphone": ('XPATH', "//div/textarea[@name='title']"),
        "textarea": ('XPATH', "//div/textarea[@name='description']"),
        "pretiphone": ('XPATH', "//div/input[@type='text']"),
        "stare": ('XPATH', "//div[@title='Utilizat']"),
        "previzualizare": ('XPATH', "//div/button[@class='css-1ydyj3h-BaseStyles']")


    }

    def click_accept_cookies(self):
        self.acceptCookiesButton.click()

    def click_adaugare_anunt(self):
        self.adaugareanunt.click()

    def select_email(self):
        self.email.set_text('pitutcristian@gmail.com')

    def select_password(self):
        self.password.set_text('Passat2003')

    def click_submitbutton(self):
        self.submit.click()

    def click_alege_categoria(self):
        self.alegecategoria.click()

    def click_electronice(self):
        self.electronice.click()

    def click_telefoane(self):
        self.telefoane.click()

    def click_iphone(self):
        self.iphone.click()

    def set_descriere_iphone(self, descriere):
        self.clickdescriereiphone.set_text(descriere)

    def set_textarea(self, textar):
        self.textarea.set_text(textar)

    def set_pret_iphone(self, pret):
        self.pretiphone.set_text(pret)

    def click_stare(self):
        self.stare.click()

    def click_previzualizare(self):
        self.previzualizare.click()


