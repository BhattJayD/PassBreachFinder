from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time
import sys
import argparse


def main():
    print("""
  __                       __                                 ___                      
 /  |                    |/  |                     /         /    /         |          
(___| ___  ___  ___      |___| ___  ___  ___  ___ (___      (___    ___  ___| ___  ___ 
|    |   )|___ |___      |   )|   )|___)|   )|    |   )     |    | |   )|   )|___)|   )
|    |__/| __/  __/      |__/ |    |__  |__/||__  |  /      |    | |  / |__/ |__  |    
                                                                                       
          """)
    parser = argparse.ArgumentParser(description="A script to take a password as an argument.")

    # Define the password argument
    parser.add_argument(
        '-p', 
        type=str, 
        help='Password to check', 
        required=True
    )
    
    # Parse the arguments
    args = parser.parse_args()

    # Get the password from the command line
    password = args.p

    password=sys.argv[2]
    # Set up Firefox options
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Run in headless mode (no visible browser)

    # Specify the local path to geckodriver
    service = Service("geckodriver")

    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Open the target URL
        driver.get("https://haveibeenpwned.com/Passwords")

        # Wait for the input field to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
        )

        # look for text input
        input_field = driver.find_element(By.CLASS_NAME, "form-control")

        # enter param as password into text input 
        input_text = password
        input_field.send_keys(input_text)
        time.sleep(5)
        # click on button
        btn = driver.find_element(By.CLASS_NAME, "btn-primary")
        btn.click()
        pwnTitle = driver.find_element(By.CLASS_NAME, "pwnTitle")
        # checking if password is been leak or not
        if pwnTitle:
            times = driver.find_element(By.ID, "pwnedPasswordResult")
            time.sleep(2)
            # wait for pwnedPasswordResult to load
            print(f"{input_text} {times.text}")
        else:
            print('safe')
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
