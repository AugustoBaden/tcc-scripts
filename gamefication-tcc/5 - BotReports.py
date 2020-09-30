from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select, WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import os

import time
from datetime import datetime as dt


class forumTesteBot():
    """docstring for forumTesteBot"""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(
            options=options, executable_path=chromedriver)

    def timerPratice(self):
        time.sleep(3)

    def gotosite(self):
        self.driver.get("target URL")
        # USER
        ui.WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "username")))
        self.driver.find_element_by_id("username").send_keys('LOGIN DATA')

        # PASSWORD
        ui.WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "password")))
        self.driver.find_element_by_id("password").send_keys('PASSWORD DATA')
        time.sleep(3)

        # IDENTIFICAR O OBJETO BOTAO DE LOGIN E CLICAR
        ui.WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "btn-login")))
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)

    def gotoreport(self):
        self.driver.get("URL WITH CONTENT AFTER LOGIN")
        time.sleep(2)

    def setData(self):
        # entrar data e tipo de ação
        # as açoes necessarias para selecionar as informaçoes especificas na pagina

        # escolher a ação
        acao = Select(ui.WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "menumodaction"))))

        acao.select_by_value("c")

        # DIA - usar dia anterior
        dataDoTrem = Select(ui.WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "menudate"))))
        #diaLa = "1568602800"

        now = dt.now()
        dia = dt.date(now)
        stamp = time.mktime(dia.timetuple())
        afinal = stamp - 86400
        diaInt = int(afinal)
        diaLa = str(diaInt)

        dataDoTrem.select_by_value(diaLa)

        time.sleep(3)

        # botao: obter esses logs
        ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[4]/div/div/section/div/form/div/input[5]')))
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/section/div/form/div/input[5]").click()
        time.sleep(5)
        print("wait for it")

    def trazPraCasa(self):
        time.sleep(2)
        print("a espera acabou")

        # o botao para download era apenas <input type="submit" value="Download"> por isso .submit e nao .click
        ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[4]/div[1]/div[2]/section/div/form[2]')))

        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div[2]/section/div/form[2]/div/button').submit()
        # mudança no xpath do formulario de download
        #
        time.sleep(4)

    def teardowm(self):
        print("ta la")
        time.sleep(60)
        self.driver.close()


if __name__ == '__main__':
    obj = forumTesteBot()
    obj.timerPratice()
    obj.gotosite()
    obj.gotoreport()
    obj.setData()
    obj.trazPraCasa()
    obj.timerPratice()
    obj.teardowm()
