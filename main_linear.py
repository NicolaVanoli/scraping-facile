from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# URL of the page
url = "https://www.linear.it"

# Set up the Chrome driver (you need to download the ChromeDriver executable)
options = Options()

# options.add_argument("--headless")
options.add_argument("--disable-logging")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Open the URL in the browser
driver.get(url)

try:
    # Find the 'targa' input element by aria-label using CSS selector
    targa_input = driver.find_element("css selector", 'input[aria-label="targa"]')
    print('Targa input found:', targa_input)

    # Clear any existing value in the 'targa' input field
    targa_input.clear()

    # Enter a value into the 'targa' input field
    targa_input.send_keys('FW085TZ')  # Replace with the actual value you want to submit

    # Find the 'birth-date' input element by aria-label using CSS selector
    birth_date_input = driver.find_element("css selector", 'input[aria-label="dt_nascita_propr"]')
    print('Birth date input found:', birth_date_input)

    # Clear any existing value in the 'birth-date' input field
    birth_date_input.clear()

    # Enter a value into the 'birth-date' input field
    birth_date_input.send_keys('07/07/1960')  # Replace with the actual value you want to submit

    # Find the button with the id 'scopri il prezzo' and click it
    fai_preventivo = driver.find_element("id", "FaiPreventivo")
    fai_preventivo.click()

    # Wait for a few seconds to ensure the page has loaded
    time.sleep(5)

    # Get the page source after clicking the button
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Now you can extract data from the soup object using BeautifulSoup methods
    # For example, printing the title of the page
    print("Page Title:", soup.title.text)
    # Fill the form with the value "123"
    address_input = driver.find_element("id", "Address_Address")
    address_input.clear()
    address_input.send_keys('Salita San Pancrazio 17')

    # Wait for the suggestions to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "results"))
    )

    suggestion = driver.find_element("class name", "address-suggestion-item")
    suggestion.click()

    button = driver.find_element(By.CLASS_NAME, "btn-green")
    button.click()


    # You can continue extracting other data as needed

finally:
    # Close the browser window
    driver.quit()

