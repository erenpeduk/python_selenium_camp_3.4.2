from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
class TestSauce:
     
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.maximize_window()
    # driver.get("https://www.saucedemo.com/")
    # sleep(2)
    
    def test_null_login(self):
        
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    def test_null_password(self):
        
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        sleep(2)
        usernameInput.send_keys("1")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
    
    def test_username_password(self):
        
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"login-button")
        passwordInput = driver.find_element(By.ID,"user_name")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
    
    def show_error_icon_test(self):
        
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorIcon = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        errorIcon.click()

    def login_standard_user(self):
        
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"login-button")
        passwordInput = driver.find_element(By.ID,"user_name")
        sleep(5)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep()
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

    def show_product_count(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"login-button")
        usernameInput.click()
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID,"user_name")
        passwordInput.click()
        passwordInput.send_keys("secret_sauce")
       
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        if (productList.__len__()== 6):
            print(f"Product count equal to 6 : {True}")
        else:
            print(f"Product count equal to 6 : {False}")
            




test1 = TestSauce()
test1.show_product_count()

while True:
    continue
        









        

    