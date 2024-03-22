from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.fashionpass.com/")
    time.sleep(5)

    element_to_hover_over = driver.find_element(By.XPATH, "//li[@cat-name='Browse']")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Hover over the element
    actions.move_to_element(element_to_hover_over).perform()
    time.sleep(4)

    # Wait for the container with the values to appear
    container_with_values = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//header[@id='header_container_id']//div[2]//ul[1]")))

    # Find all the elements within the container
    all_values_elements = container_with_values.find_elements(By.XPATH, ".//a")

    # Print the text of each element
    for element in all_values_elements:
       print("element text : ",element.text)

       try : 
            element.click()
            time.sleep(5)
            # driver.get("https://www.fashionpass.com/")
            # time.sleep(5)

            # element_to_hover_over = driver.find_element(By.XPATH, "//li[@cat-name='Browse']")

            # # Create an ActionChains object
            # actions = ActionChains(driver)

            # # Hover over the element
            # actions.move_to_element(element_to_hover_over).perform()
            # time.sleep(4)

            # # Wait for the container with the values to appear
            # container_with_values = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//header[@id='header_container_id']//div[2]//ul[1]")))


       except:
           print("not clicked")
    # # Close the WebDriver
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
