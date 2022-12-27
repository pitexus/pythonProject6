from seleniumpagefactory.Pagefactory import PageFactory

class Login(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "account": ('XPATH', "//div[@class='css-1mzzuk6']"),
        "email": ('XPATH', "//input[@name='username']"),
        "password": ('XPATH', "//input[@type='password']"),
        "checkbutton": ('CSS', ".css-hr42fx"),
        "submit": ('XPATH', "//button[@type='submit']")
    }

    def click_account(self):
        self.account.click()

    def select_email(self):
        self.email.set_text('pitutcristian@gmail.com')

    def select_password(self):
        self.password.set_text('Passat2003')

    def click_check(self):
        self.checkbutton.click()

    def click_submitbutton(self):
        self.submit.click()







