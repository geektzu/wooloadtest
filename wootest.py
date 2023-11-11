from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time, random
from faker import Faker


def test_shop_page(driver):
	driver.get("https://loadtest.mystagingwebsite.com/shop-2/")
	print(driver.title)
	elements = driver.find_elements(By.CSS_SELECTOR, "a[class='button product_type_simple add_to_cart_button ajax_add_to_cart']")
	print(elements)
	time.sleep(2)
	choice = random.randint(1, 3)
	elements[choice].click()
	timeout = random.randint(5, 10)
	time.sleep(timeout)

def test_checkout_page(driver):
	driver.get("https://loadtest.mystagingwebsite.com/checkout-2/")
	print(driver.title)

	faker = Faker()
	first_name = driver.find_element(By.ID, 'billing_first_name')
	first_name.send_keys(faker.first_name())
	last_name = driver.find_element(By.ID, 'billing_last_name')
	last_name.send_keys(faker.last_name())
	address = driver.find_element(By.ID, 'billing_address_1')
	address.send_keys('60 29th Street #343')

	city = driver.find_element(By.ID, 'billing_city')
	city.send_keys('San Francisco')

	zipcode = driver.find_element(By.ID, 'billing_postcode')
	zipcode.send_keys('94110')

	phone = driver.find_element(By.ID, 'billing_phone')
	phone.send_keys('08002733049')

	email = driver.find_element(By.ID, 'billing_email')
	email.send_keys('alan.zhutao@gmail.com')

	timeout = random.randint(2, 5)
	time.sleep(timeout)

	place_order = driver.find_element(By.CSS_SELECTOR, "button[name='woocommerce_checkout_place_order']")
	place_order.click()

	timeout = random.randint(2, 5)
	time.sleep(timeout)

def selenium_test():
	#driver = webdriver.Chrome('./chromedriver')
	options = Options()
	options.headless = True
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	options.add_argument('window-size=4086x4086')
	driver = webdriver.Chrome(options=options)
	driver.maximize_window()

	try:
		test_shop_page(driver)
	except Exception as e:
		test_shop_page(driver)

	#checkout page
	try:
		test_checout_page(driver)
	except Exception as e:
		test_checkout_page(driver)

	
	print(driver.current_url)
	driver.close()

if __name__ == "__main__":
	selenium_test()