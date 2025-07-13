from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time

class RegisterPageTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_register_new_user(self):
        self.browser.get(f'{self.live_server_url}/register/')

        # Найдём поля
        username_input = self.browser.find_element(By.NAME, 'username')
        password1_input = self.browser.find_element(By.NAME, 'password1')
        password2_input = self.browser.find_element(By.NAME, 'password2')
        time.sleep(3)
        # Заполним форму
        username_input.send_keys('testuser')
        password1_input.send_keys('Testpass123!')
        password2_input.send_keys('Testpass123!')
        password2_input.send_keys(Keys.RETURN)

        # Немного подождать, пока произойдёт редирект
        time.sleep(3)

        # Проверим, что пользователь создался
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Проверим, что попали на главную (success_url = '/')
        # self.assertEqual(self.browser.current_url, f'{self.live_server_url}/')
