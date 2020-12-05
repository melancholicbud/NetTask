from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import unittest


class TestMy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main(self):
        self.link = "https://netpeak.ua/"
        # Перейти по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
        self.driver.get(self.link)
        self.driver.implicitly_wait(5)

        # Перейдите на страницу "Работа в Netpeak", нажав на кнопку "Карьера"
        button1 = self.driver.find_element_by_css_selector("#main-menu > ul > li.blog > a")
        button1.click()
        # Перейдите на страницу заполнения анкеты, нажав на кнопку - "Я хочу работать в Netpeak"
        button2 = self.driver.find_element_by_css_selector(
            "body > div.container.employees-groups > div > div > div.vac-block-border > div > a")
        button2.click()

        # Загрузить файл с недопустимым форматом в блоке "Резюме", например png,
        # и проверить что на странице появилось сообщение, о том что формат изображения неверный
        x = self.driver.find_element_by_css_selector("input[type=file]")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'q.png')
        x.send_keys(file_path)
        time.sleep(2)
        t = self.driver.find_element_by_xpath('// *[ @ id = "up_file_name"] / label').text
        assert t == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

        # Заполнить случайными данными блок "3. Личные данные"
        input1 = self.driver.find_element_by_id("inputName")
        input1.send_keys("John")
        input2 = self.driver.find_element_by_id("inputLastname")
        input2.send_keys("Konnor")
        input3 = self.driver.find_element_by_id("inputEmail")
        input3.send_keys("terminator@gmail.com")
        select1 = Select(self.driver.find_element_by_name("by"))
        select1.select_by_value("1993")
        select2 = Select(self.driver.find_element_by_name("bm"))
        select2.select_by_value("02")
        select2 = Select(self.driver.find_element_by_name("bd"))
        select2.select_by_value("12")
        input4 = self.driver.find_element_by_id("inputPhone")
        input4.send_keys("+380000000")

        # Нажать на кнопку отправить резюме
        button3 = self.driver.find_element_by_css_selector("#submit")
        button3.click()

        # Проверить что сообщение на текущей странице - "Все поля являються обязательными
        # для заполнения" - подстветилось красным цветом
        warning = self.driver.find_element_by_css_selector("body > div:nth-child(4) > div > p")
        assert warning.value_of_css_property("color") == "rgba(255, 0, 0, 1)"

        # Нажать на логотип для перехода на главную страницу и убедиться что открылась нужная страница
        button4 = self.driver.find_element_by_css_selector(
            "#header > div.navbar-header.bg-for-white > div > div > div:nth-child(1) > div.logo-block > a")
        button4.click()
        time.sleep(2)
        assert self.driver.current_url == 'https://netpeak.ua/'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
