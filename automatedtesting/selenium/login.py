# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime

def _get_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    

# Start the browser and login with standard_user
def login (user, password):
    print (_get_timestamp(), 'Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print (_get_timestamp(), 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

    print(_get_timestamp(), f'Login with username {user} and password {password}')
    product_list = driver.find_elements(By.CSS_SELECTOR, "div[class=inventory_item] > div.inventory_item_description")
    c = 0 
    for item in product_list:
        item_name = item.find_element(By.CSS_SELECTOR, "div[class=inventory_item_label] > a > div[class=inventory_item_name]").get_attribute('innerHTML')
        print(_get_timestamp(), f'Adding new {item_name} to cart!')
        item.find_element(By.CSS_SELECTOR, "button[class='btn btn_primary btn_small btn_inventory']").click()
        c += 1

    print(_get_timestamp(), f"There are {c} items added to cart!")

    print(_get_timestamp(), 'Removing items from cart!')
    
    product_list = driver.find_elements(By.CSS_SELECTOR, "div[class=inventory_item] > div.inventory_item_description")
    c = 0 
    for item in product_list:
        item_name = item.find_element(By.CSS_SELECTOR, "div[class=inventory_item_label] > a > div[class=inventory_item_name]").get_attribute('innerHTML')
        print(_get_timestamp(), f'Removing {item_name} from cart!')
        item.find_element(By.CSS_SELECTOR, "button[class='btn btn_secondary btn_small btn_inventory']").click()
        c += 1

    print(_get_timestamp(), f'There are {c} items removed from cart!')

    driver.close()
    print(_get_timestamp(), 'Closed browser sucessfully!')

login('standard_user', 'secret_sauce')

