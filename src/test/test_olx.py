from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pytest

from src.pages import search_anunt1
from src.pages.adaugare_anunt import AdaugareAnunt
from src.pages.homepage import Homepage
from src.pages.locatie import Locatie
from src.pages.login import Login
from src.utilities.BaseClass import Baseclass
from src.pages.search_anunt1 import SearchAnunt
from src.pages.search_anunt2 import SearchAnunt2


@pytest.mark.usefixtures("setup")
class TestOne(Baseclass):
    def test_1(self, setup):
        log = self.getlogger()

        homepage = Homepage(self.driver)
        sleep(3)
        homepage.click_accept_cookies()
        log.info('Click on accepta cookies')
        homepage.click_myaccount()
        log.info('Click on Contul tau')

    def test_2(self, setup):
        log = self.getlogger()

        login = Login(self.driver)
        sleep(2)
        login.click_account()
        log.info('Click pe intra in cont')
        sleep(2)
        login.select_email()
        log.info('Click on adaugare adresa mail')
        login.select_password()
        log.info('Click on introducere parola')
        login.click_check()
        log.info('Click on bifeaza casuta')
        login.click_submitbutton()
        log.info('Click on submit')


class TestTwo(Baseclass):
    def test_1(self, setup):
        log = self.getlogger()

        search_anunt1 = SearchAnunt(self.driver)
        search_anunt1.click_accept_cookies()
        log.info('Click on accepta cookies')

    def test_2(self, setup):
        log = self.getlogger()

        search_anunt1 = SearchAnunt(self.driver)
        search_anunt1.click_automoto()
        log.info('Click on automoto')
        sleep(2)
        search_anunt1.click_autoturisme()
        log.info('Click on autoturisme')
        search_anunt1.click_categorie()
        log.info('Click on categorie')
        search_anunt1.click_model()
        log.info('Click on model')


class TestThree(Baseclass):
    def test_1(self, setup):
        log = self.getlogger()

        search_anunt2 = SearchAnunt2(self.driver)
        search_anunt2.click_accept_cookies()
        log.info('Click on accepta cookies')

    def test_2(self, setup):
        log = self.getlogger()

        search_anunt2 = SearchAnunt2(self.driver)
        search_anunt2.click_imobiliare()
        log.info('Click on imobiliare')
        sleep(2)
        search_anunt2.click_case_de_vanzare()
        log.info('Click on case de vanzare')
        sleep(2)
        search_anunt2.click_dropdown_camere()
        log.info('Click on dropdown camere')
        search_anunt2.click_nr_camere()
        log.info('Click on nr de camere')



class TestFour(Baseclass):
    def test_1(self, setup):
        log = self.getlogger()

        locatie = Locatie(self.driver)
        locatie.click_accept_cookies()
        log.info('Click on accepta cookies')

    def test_2(self, setup):
        log = self.getlogger()

        locatie = Locatie(self.driver)
        locatie.click_alege_locatie()
        log.info('Click on locatie')
        locatie.click_submit_locatie()
        log.info('Click on cauta')


class TestFive(Baseclass):
    def test_1(self, setup):
        log = self.getlogger()

        adaugare_anunt = AdaugareAnunt(self.driver)
        adaugare_anunt.click_accept_cookies()
        log.info('Click on accepta cookies')

    def test_2(self, setup):
        log = self.getlogger()

        adaugare_anunt = AdaugareAnunt(self.driver)
        adaugare_anunt.click_adaugare_anunt()
        log.info('Click on adaugare anunt nou')
        adaugare_anunt.select_email()
        log.info('Click on adaugare adresa mail')
        adaugare_anunt.select_password()
        log.info('Click on introducere parola')

        adaugare_anunt.click_submitbutton()
        log.info('Click on submit')
        sleep(3)
        adaugare_anunt.click_alege_categoria()
        log.info('click on alege categoria')
        sleep(3)
        adaugare_anunt.click_electronice()
        log.info('click on electronice')
        sleep(3)
        adaugare_anunt.click_telefoane()
        log.info('click on telefoane')
        sleep(3)
        adaugare_anunt.click_iphone()
        log.info('click on iphone')
        sleep(3)
        adaugare_anunt.set_descriere_iphone('apple iphone12 second')
        log.info('descriere iphone')
        adaugare_anunt.set_textarea('telefon in stare buna bateria tine 3 zile urme normale de uzura liber in orice retea')
        log.info('descriere telefon in stare buna')
        adaugare_anunt.set_pret_iphone('2000')
        log.info('pret iphone')
        adaugare_anunt.click_stare()
        log.info('click on stare')
        adaugare_anunt.click_previzualizare()
        log.info('click on previzualizare anunt')














