from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from loginFb import driver
import time

def get_matches():
    match_profiles = driver.find_elements('class name', 'matchListItem')
    print(str(match_profiles))
    message_links = []
    for profile in match_profiles:
        if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute(
                'href') == 'https://tinder.com/app/likes-you':
            continue
        match_name = profile.find_element(By.CLASS_NAME, 'Ell')
        name = match_name.text
        print("got matches")
        print(name)
        message_links.append((name, profile.get_attribute('href')))
    return message_links

def send_messages_to_matches():
    links = get_matches()
    for name, link in links:
        send_message(name, link)

def send_message(name, link):
    driver.get(link)
    time.sleep(2)
    text_area = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
    print("sending message")
    #message = generate_intro(generate_tinder_message(), name)
    text_area.send_keys("Hola... ¿Cómo estás?")
    time.sleep(1)
    text_area.send_keys(Keys.ENTER)