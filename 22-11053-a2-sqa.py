# Install selenium package and import it.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Instantiate the selenium opening exclusively chrome
driver = webdriver.Chrome()

# Give link to the website on which to perform the testing
url = 'https://www.saucedemo.com/'

# Open the website through selenium webdriver tool.
driver.get(url)

# Enter Username and Password to the dummy website for login
driver.find_element_by_xpath('//*[@id="user-name"]').send_keys('standard_user')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('secret_sauce')
# allow the webpage to remain open for 2 seconds so that it is easier to see what was done
time.sleep(2)

# Click the button to enter the website with the credentials given.
driver.find_element_by_xpath('//*[@id="login-button"]').click()
time.sleep(2)

# Select the backpack to be sent to the cart
driver.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(2)

# Select the bike light to be sent to the cart
driver.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
time.sleep(2)

# Go to the shopping cart to see the items selected
driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)

# Proceed to checkout
driver.find_element_by_xpath('//*[@id="checkout"]').click()
time.sleep(2)

# Enter invoice details
driver.find_element_by_xpath('//*[@id="first-name"]').send_keys('Abdullah')
driver.find_element_by_xpath('//*[@id="last-name"]').send_keys('Khalid')
driver.find_element_by_xpath('//*[@id="postal-code"]').send_keys('21-11214')
time.sleep(2)

# Continue to checkout
driver.find_element_by_xpath('//*[@id="continue"]').click()
time.sleep(2)

# Confirm the purchase
driver.find_element_by_xpath('//*[@id="finish"]').click()
time.sleep(2)

# Go back to main page
driver.find_element_by_xpath('//*[@id="back-to-products"]').click()
time.sleep(2)

# Go to drop-down menu
driver.find_element_by_xpath('//*[@id="react-burger-menu-btn"]').click()
time.sleep(2)

# Click logout
driver.find_element_by_xpath('//*[@id="logout_sidebar_link"]').click()
time.sleep(2)

# Exit the test and close selenium
driver.quit()
