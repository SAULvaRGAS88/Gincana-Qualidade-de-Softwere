import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ExemploSeleniumWebDriver(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_login(self):
        driver = self.driver
        driver.get('https://trainer-squad.vercel.app//')
        print("URL:", driver.current_url)
        time.sleep(2)
        
        elem = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root")
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(2)
        
        elem = driver.find_element(By.ID, "standard-basic-label")
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(2)
        
        input_field1 = driver.find_element(By.XPATH, "(//input[@id='standard-basic'])[1]")
        input_field1.clear()
        input_field1.send_keys("user") 
        self.assertEqual(input_field1.get_attribute('value'), "user", "Texto não inserido corretamente")
        time.sleep(2)
        
        elem = driver.find_element(By.ID, "standard-basic")
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(2)
        
        input_field2 = driver.find_element(By.XPATH, "(//input[@id='standard-basic'])[2]")
        input_field2.clear()
        input_field2.send_keys("123456") 
        self.assertEqual(input_field2.get_attribute('value'), "123456", "Senha errada")
        time.sleep(2)       
        
        button_element = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-1y1k3rb")

        driver.execute_script("arguments[0].click();", button_element)
        
        button_element.send_keys(Keys.RETURN)
        time.sleep(4)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
