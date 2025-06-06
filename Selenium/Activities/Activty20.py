# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Start the Driver
with webdriver.Firefox() as driver:
    # Declare the wait variable
    wait = WebDriverWait(driver, timeout=10)
    # Navigate to the URL
    driver.get("https://training-support.net/webelements/alerts")
    # Print the title of the page
    print("Page title is: ", driver.title)

    # Find and click the button to open the alert
    driver.find_element(By.ID, "prompt").click()

    # Switch focus to the alert
    promptAlert = wait.until(EC.alert_is_present())

    # Print the text in the alert
    alertText = promptAlert.text
    print("Text in alert: " + alertText)
    
    # Type text in the prompt alert
    promptAlert.send_keys("Awesome!")

    # Close the alert by clicking OK
    promptAlert.accept()

    # Print the message
    print(driver.find_element(By.ID, "result").text)
