# pip install undetected-chromedriver 
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
import time
# Initializing driver 
driver = uc.Chrome() 
product_name = input("Enter your Product name")
size = input("Enter your Size : ")
price = input("Enter your price : ")

# lowercase_text = product_name.lower()

# # Replace spaces with hyphens
# hyphenated_text = lowercase_text.replace(" ", "-")

# # Remove non-alphanumeric characters
# final_product_name = ''.join(char if char.isalnum() or char == '-' else '' for char in hyphenated_text)
# # Try accessing a website with antibot service 
# print(final_product_name)
driver.get(f"https://stockx.com")

# search_input = driver.find_element(By.CSS_SELECTOR('input[data-testid="site-search"]'))
search_input = driver.find_element(By.CLASS_NAME,"chakra-input")


# Clear any existing value in the input field
# search_input.clear()
print("working")
# Input the desired text (e.g., "Crocs Classic Clog Lightning McQueen")
search_input.send_keys(product_name)
time.sleep(5)
search_result_item = driver.find_element(By.CLASS_NAME, "css-1k7lzmm-SearchResultItemContent")

search_result_item.click()
time.sleep(5)

bid_link_element = driver.find_element(By.CLASS_NAME,"chakra-button css-lievjk")
bid_link = bid_link_element.get_attribute("href")
print("Bid Link:", bid_link)

# print(driver.get(f"https://stockx.com/{final_product_name}"))
# driver.get (f"https://stockx.com/buy/{final_product_name}?size={size}")
# # Try a more general selector or xpat
# time.sleep(10)

# bid_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="bid-input"]')
# print("bid_input : " , bid_input)
# # Input the desired value
# bid_input.clear()
# bid_input.send_keys(price)
        
time.sleep(10)

# driver.close()
driver.quit()