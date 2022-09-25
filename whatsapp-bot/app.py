from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import pandas as pd


data = pd.read_csv('./data/Web_Dev_Team_update.csv')
phone_numbers = data['CONTACT'].values

no_of_message = 1

message_text = "Welcome to GDSC Web Team 2022/2023. Here is the link to join the Whatsapp Group: https://chat.whatsapp.com/I48576OGtjd1f540qPUdT1"



def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
    
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()

driver = webdriver.Chrome(r'C:\Users\ronle\Downloads\chromedriver_win32\chromedriver.exe') 
driver.get("http://web.whatsapp.com")
sleep(10)


def send_whatsapp_msg(phone_no, text):
    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Invailid phone no :" + str(phone_no))


def main():
    for moblie_no in phone_numbers:
        try:
            send_whatsapp_msg(phone_no=moblie_no, text=message_text)

        except Exception as e:

            sleep(10)
            is_connected()



if __name__ == '__main__':
    main()



# Replace below path with the absolute path 
# to chromedriver in your computer 
# driver = webdriver.Chrome('C:\Users\ronle\Downloads\chromedriver_win32') 

# driver.get("https://web.whatsapp.com/") 
# wait = WebDriverWait(driver, 600) 

# target = 'GDSC Web Team 2022/2023'

# Replace the below string with your own message 
# string = "Welcome to GDSC Web Team 2022/2023. Here is the link to join the Whatsapp Group: https://chat.whatsapp.com/I48576OGtjd1f540qPUdT1"

