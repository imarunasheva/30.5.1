from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from settings import email, password

class TestPetFriends:
    def test_all_have_name_breed_ages(self):
        """проверяем, что у всех питомцев есть имя, возраст и порода"""
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # открываем страницу авторизации
        driver.get("https://petfriends.skillfactory.ru/")

        # нажимаем кнопку зарегистрироваться
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

        # выбираем у меня уже есть аккаунт
        driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # явное ожидание
        WDW(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'email')))

        # указываем email
        driver.find_element(By.ID, 'email').send_keys(email)

        # указываем пароль
        driver.find_element(By.ID, 'pass').send_keys(password)

        # нажимаем кнопку Войти
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

        # явные ожидания
        WDW(driver, 5).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

        # заходим на страницу Мои питомцы
        driver.find_element(By.XPATH, '/html/body/nav/button').click()
        driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()

        # проверяем, что находимся на нужной странице
        if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
            driver.save_screenshot('result_petfriends.png')
        else:
            raise Exception("login error")

        # неявные ожидания
        driver.implicitly_wait(10)

        # получаем элементы после 10 сек
        names = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')
        breeds = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[2]')
        ages = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[3]')

        for i in range(len(names)):
            assert names[i].text != ''
            assert breeds[i].text != ''
            assert ages[i].text != ''

        driver.quit()

    def test_all_pets_are_in_list(self):
        """проверяем, что присутствуют все питомцы"""

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # открываем страницу авторизации
        driver.get("https://petfriends.skillfactory.ru/")

        # нажимаем кнопку зарегистрироваться
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

        # выбираем у меня уже есть аккаунт
        driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # явное ожидание
        WDW(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'email')))

        # указываем email
        driver.find_element(By.ID, 'email').send_keys(email)

        # указываем пароль
        driver.find_element(By.ID, 'pass').send_keys(password)

        # нажимаем кнопку Войти
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

        # явные ожидания
        WDW(driver, 5).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

        # заходим на страницу Мои питомцы
        driver.find_element(By.XPATH, '/html/body/nav/button').click()
        driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()

        # проверяем, что находимся на нужной странице
        if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
            driver.save_screenshot('result_petfriends.png')
        else:
            raise Exception("login error")

        # неявные ожидания
        driver.implicitly_wait(10)

        # получаем элементы после 10 сек
        names = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')

        all_mypets = len(names)
        number_mypets = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
        parts = number_mypets.text.split("\n")
        quantity = list(parts[1].split())

        assert str(all_mypets) in quantity

        driver.quit()

    def test_pets_have_photo(self):
        """проверяем, что хотя бы у половины питомцев есть фото"""

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # открываем страницу авторизации
        driver.get("https://petfriends.skillfactory.ru/")

        # нажимаем кнопку зарегистрироваться
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

        # выбираем у меня уже есть аккаунт
        driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # явное ожидание
        WDW(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'email')))

        # указываем email
        driver.find_element(By.ID, 'email').send_keys(email)

        # указываем пароль
        driver.find_element(By.ID, 'pass').send_keys(password)

        # нажимаем кнопку Войти
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

        # явные ожидания
        WDW(driver, 5).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

        # заходим на страницу Мои питомцы
        driver.find_element(By.XPATH, '/html/body/nav/button').click()
        driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()

        # проверяем, что находимся на нужной странице
        if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
            driver.save_screenshot('result_petfriends.png')
        else:
            raise Exception("login error")

        # неявные ожидания
        driver.implicitly_wait(10)

        # получаем элементы после 10 сек
        images = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//img')

        quantity_photo = 0
        for i in range(len(images)):
            if images[i].get_attribute('src') != '':
                quantity_photo += 1

        assert quantity_photo / len(images) > 0.5

        driver.quit()

    def test_different_names(self):
        """проверяем, что у всех питомцев разные имена"""

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # открываем страницу авторизации
        driver.get("https://petfriends.skillfactory.ru/")

        # нажимаем кнопку зарегистрироваться
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

        # выбираем у меня уже есть аккаунт
        driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # явное ожидание
        WDW(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'email')))

        # указываем email
        driver.find_element(By.ID, 'email').send_keys(email)

        # указываем пароль
        driver.find_element(By.ID, 'pass').send_keys(password)

        # нажимаем кнопку Войти
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

        # явные ожидания
        WDW(driver, 5).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

        # заходим на страницу Мои питомцы
        driver.find_element(By.XPATH, '/html/body/nav/button').click()
        driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()

        # проверяем, что находимся на нужной странице
        if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
            driver.save_screenshot('result_petfriends.png')
        else:
            raise Exception("login error")

        # неявные ожидания
        driver.implicitly_wait(10)

        # получаем элементы после 10 сек
        names = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')

        all_names = []
        for i in range(len(names)):
            all_names.append(names[i].text)

        assert len(set(all_names)) == len(names)

        driver.quit()

    def test_unique_pets(self):
        """проверяем, что в списке нет повторяющихся питомцев"""

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # открываем страницу авторизации
        driver.get("https://petfriends.skillfactory.ru/")

        # нажимаем кнопку зарегистрироваться
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

        # выбираем у меня уже есть аккаунт
        driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # явное ожидание
        WDW(driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'email')))

        # указываем email
        driver.find_element(By.ID, 'email').send_keys(email)

        # указываем пароль
        driver.find_element(By.ID, 'pass').send_keys(password)

        # нажимаем кнопку Войти
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

        # явные ожидания
        WDW(driver, 5).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

        # заходим на страницу Мои питомцы
        driver.find_element(By.XPATH, '/html/body/nav/button').click()
        driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()

        # проверяем, что находимся на нужной странице
        if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
            driver.save_screenshot('result_petfriends.png')
        else:
            raise Exception("login error")

        # неявные ожидания
        driver.implicitly_wait(10)

        # получаем элементы после 10 сек
        names = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')
        breeds = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[2]')
        ages = driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[3]')

        pets = {}
        for i in range(len(names)):
            pets[i] = names[i].text, breeds[i].text, ages[i].text
        unique_pets = set(pets.values())

        assert len(unique_pets) == len(names)

        driver.quit()
