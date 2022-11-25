# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

    print(f'Login with username {user} and password {password}')
    product_list = driver.find_elements(By.CSS_SELECTOR, "div[class=inventory_item] > div.inventory_item_description > div.pricebar > button")
    c = 0 
    for item in product_list:
        print('Adding new item to cart!')
        item_name = item.find_element(By.CLASS_NAME, )
        item.click()
        c += 1
    print(f"There are {c} items added to cart!")

    print('Removing items from cart!')
    
    product_list = driver.find_elements(By.CSS_SELECTOR, "div[class=inventory_item] > div.inventory_item_description > div.pricebar > button[class='btn btn_secondary btn_small btn_inventory']")
    c = 0 
    for item in product_list:
        print('Removing an item from cart!')
        item.click()
        c += 1

    print(f'There are {c} items removed from cart!')
    
    driver.close()

login('standard_user', 'secret_sauce')

