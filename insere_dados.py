import datetime
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
    
    def test_insere_dados(self):
        driver = self.driver
        driver.get('https://trainer-squad.vercel.app//')
        print("URL:", driver.current_url)
        # time.sleep(1)
        
        try:
            elem = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root")
            driver.execute_script("arguments[0].click();", elem)
            # time.sleep(1)
            
            elem = driver.find_element(By.ID, "standard-basic-label")
            driver.execute_script("arguments[0].click();", elem)
            # time.sleep(1)
            
            input_field1 = driver.find_element(By.XPATH, "(//input[@id='standard-basic'])[1]")
            input_field1.clear()
            input_field1.send_keys("user") 
            self.assertEqual(input_field1.get_attribute('value'), "user", "Texto não inserido corretamente")
            # time.sleep(1)
            
            elem = driver.find_element(By.ID, "standard-basic")
            driver.execute_script("arguments[0].click();", elem)
            # time.sleep(1)
            
            input_field2 = driver.find_element(By.XPATH, "(//input[@id='standard-basic'])[2]")
            input_field2.clear()
            input_field2.send_keys("123456") 
            self.assertEqual(input_field2.get_attribute('value'), "123456", "Senha errada")
            # time.sleep(1)       
            
            button_element = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-1y1k3rb")
            driver.execute_script("arguments[0].click();", button_element)
            button_element.send_keys(Keys.RETURN)  
            # time.sleep(1)
            
            link_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='CADASTRAR']"))
            )
            link_element.click()
            time.sleep(1)
            
            # >>>>>>>>>>>>>>>>>>>>>>>>>CARREGANDO DADOS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
            campo_nome = driver.find_element(By.ID, "nomeTextField")
            campo_cpf = driver.find_element(By.ID, "cpfTextField")
            campo_telefone = driver.find_element(By.ID, "telefoneTextField")
            campo_email = driver.find_element(By.ID, "emailTextField")

            campo_nome.send_keys("Nome do Aluno")
            campo_cpf.send_keys("12345678900")
            campo_telefone.send_keys("999999999")
            campo_email.send_keys("exemplo@email.com")
            
            link_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "sexoTextField"))
            )
            link_element.click()
           
            menu_items = driver.find_elements(By.XPATH, "//li[@role='option']")
            for item in menu_items:
                if item.text == "Masculino":
                    item.click()
                    break
            
            time.sleep(2)
            link_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "planonomeTextField"))
            )
            link_element.click()
            
            time.sleep(2)
            menu_item = driver.find_elements(By.XPATH, "//li[contains(@class, 'MuiMenuItem-root')]")
            for item in menu_item:
                if item.text == "Mensal":
                    item.click()
                    break
            
            time.sleep(2)
            campo_valor = driver.find_element(By.ID, "vaorTextField")
            campo_valor.send_keys('150')
            
            time.sleep(2)
            link_pagamento = driver.find_element(By.ID, ":rc:")
            link_pagamento.click()

            # SALVAR>>>>>>>>>>>>>>>>>>>
            time.sleep(2)
            salvar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btn"))
            )
            tag_name = salvar.tag_name
            print(f"Tag name do elemento: {tag_name}")
            driver.execute_script("arguments[0].click();", salvar)
            time.sleep(2)
            
        except Exception as e:
            print(f"<<<< Erro no elemento >>>>: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
