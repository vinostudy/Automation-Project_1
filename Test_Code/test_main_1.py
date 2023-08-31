# test_main_1.py (Page Object Model)

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_OrangeHRM:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Ohrm_Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_admin_login(self, booting_function): #Test case1 (login data)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox).send_keys(data.Ohrm_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().password_inputbox).send_keys(data.Ohrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().Login_button).click()
        sleep(2)

        assert self.driver.title ==  self.driver.title
        print("Test case1 - The User logged in successfully")
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_button).click()
        self.driver.close()


    def test_admin_invalid(self, booting_function): #Test case2 (Invalid crediticals data)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox).send_keys(data.Ohrm_Data.username)
        #   self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox1).send_keys(data.Ohrm_Data.username1)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().password_inputbox1).send_keys(data.Ohrm_Data.password1)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().Login_button).click()
        sleep(2)

        assert self.driver.title ==  self.driver.title
        print("Test case2 - Invalid credentials error message displayed successfully")
        self.driver.close() 


    def test_add_employee(self,booting_function): #Test case3 (Adding new employee detials data)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox).send_keys(data.Ohrm_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().password_inputbox).send_keys(data.Ohrm_Data.password)  
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().Login_button).click()
        sleep(2)
        
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().pim_module).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().add_module).click()
        sleep(2) 
        
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().employee_firstname).send_keys(data.Ohrm_Data().first_name)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().employee_lastname).send_keys(data.Ohrm_Data().last_name) 
        sleep(2)                   
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().save_button).click() 
        sleep(2)

        assert self.driver.title ==  self.driver.title
        print("Test case3 - Employee successfully added")
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_button).click()
        self.driver.close()


    def test_edit_details(self,booting_function):   #Test case4 (Editing employee detials data)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox).send_keys(data.Ohrm_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().password_inputbox).send_keys(data.Ohrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().Login_button).click()
        sleep(2)
        
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().pim_module).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().employee_name).send_keys(data.Ohrm_Data().first_name)
        sleep(2)
        
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().search_button).click()     
        sleep(2)
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().click_button).click()
        sleep(2)
        
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().middle_name).send_keys(data.Ohrm_Data.middle_name)
        sleep(2)     
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().esave_button).click()
        sleep(2)

        assert self.driver.title ==  self.driver.title
        print("Test case4 - Employee details updated")
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_button).click()
        self.driver.close()  


    def test_delete_employee(self,booting_function):  #Test case5 (Deleting employee detials data)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().username_inputbox).send_keys(data.Ohrm_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_Locators().password_inputbox).send_keys(data.Ohrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().Login_button).click()
        sleep(2)

        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().pim_module).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().employee_name).send_keys(data.Ohrm_Data().first_name)
        sleep(2)
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().search_button).click()     
        sleep(2)         
          
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().trash_button).click()
        sleep(2)
        self .driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().yes_delete).click()
        sleep(2)

        assert self.driver.title ==  self.driver.title
        print("Test case5 - Employee successfully deleted")
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_Locators().logout_button).click()
        self.driver.close() 

                