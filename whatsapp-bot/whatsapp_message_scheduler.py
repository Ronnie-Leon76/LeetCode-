import sched
import time
from selenium import webdriver

# The message you want to send
message_body = 'Hello from Adept Schneider!'

# Initialize the scheduler
s = sched.scheduler()

# Schedule the message to be sent at a specific time
def send_message(sc):
    # Use Selenium to open WhatsApp in your browser and send the message
    driver = webdriver.Chrome(executable_path=r'C:\Users\ronle\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)

    # Find the chat box and send the message
    chat_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chat_box.send_keys(message_body)
    send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    send_button.click()
    print(f'Sent message to group: {message_body}')

# Set the time when the message should be sent (in this case, 2 minutes from now)
send_time = time.time() + 60 * 2
s.enterabs(send_time, 1, send_message, (s,))

# Start the scheduler
s.run()
