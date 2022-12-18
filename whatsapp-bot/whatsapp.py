from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd
import time

# Replace this with the path to the ChromeDriver executable
chromedriver_path = r'C:\Users\ronle\Downloads\chromedriver_win32\chromedriver.exe'

service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the page to load
driver.implicitly_wait(30)

# Replace this with the URL of your WhatsApp group
# GROUP_LINK = 'https://chat.whatsapp.com/I48576OGtjd1f540qPUdT1'

# Read the phone numbers from a CSV file
df = pd.read_csv('./data/Web_Dev_Team_update.csv')

# Loop through the phone numbers in the DataFrame
for index, row in df.iterrows():
  phone_number = row['CONTACT']
  url = f'https://api.whatsapp.com/send/?phone={phone_number}&text=Join%20our%20group%20using%20this%20link:%20https://chat.whatsapp.com/I48576OGtjd1f540qPUdT1'
  driver.get(url)
  time.sleep(5)
  print(f'Sent message to {phone_number}')
  # Find the search bar element and enter the phone number
  #search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
  #search_bar.send_keys(phone_number)
  
  # Wait for the contact to appear in the search results
  #driver.implicitly_wait(5)
  
  # Find the contact in the search results and click on it
  #contact = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div[1]')
  #contact.click()
  
  # Enter the phone number in the input field
  # contact = driver.find_element(By.XPATH, '//input[@title="Search or start new chat"]')
  # Wait for the page to load
  # driver.implicitly_wait(5)
  
  # Find the message input field and enter the group link
  # message_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
  # message_input.send_keys(GROUP_LINK)
  
  # Find the send button and click on it
  # send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')
  # send_button.click()

# Close the web driver
driver.quit()
