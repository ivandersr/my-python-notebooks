from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as err:
            print('Erro ao clicar em Sign in: ', err)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            btn_perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header '
                '> div.Header-item.position-relative.mr-0.d-none.d-md-flex > details'
            )
            btn_perfil.click()
        except Exception as err:
            print('Erro ao clicar no perfil:', err)

    def maximize(self):
        self.chrome.maximize_window()

    def realiza_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('catsui.san@gmail.com')
            input_password.send_keys('catsuisui123')
            sleep(2)
            btn_login.click()
        except Exception as err:
            print('Erro ao realizar o login:', err)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def realiza_logout(self):
        try:
            btn_logout = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > '
                'div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button'
            )
            btn_logout.click()
        except Exception as err:
            print('Erro ao realizar logout:', err)


chrome = ChromeAuto()
chrome.acessa('https://github.com')
chrome.maximize()
chrome.clica_sign_in()
chrome.realiza_login()
chrome.clica_perfil()
chrome.verifica_usuario('catsui')
sleep(3)
chrome.realiza_logout()
sleep(1)
chrome.sair()
