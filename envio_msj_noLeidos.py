from time import sleep
from loginFb import driver
from selenium.webdriver.common.by import By
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
from selenium.webdriver.common.keys import Keys
def get_matches():
 sleep(5)
 #mensajes = driver.find_element('xpath', '//*[@id="q766808048"]')
 #mensajes.click()
 mensajes_nuevos = driver.find_elements(By.CLASS_NAME, 'messageListItem--isNew')
 print(str(mensajes_nuevos))
 message_links = []
 for profile in mensajes_nuevos:
  if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute(
          'href') == 'https://tinder.com/app/likes-you':
   continue
  match_name = profile.find_element(By.CLASS_NAME, 'Ell')
  name = match_name.text
  print("got matches")
  print(name)
  message_links.append((name, profile.get_attribute('href')))
 return message_links


def send_messages_nuevos():
 links = get_matches()
 for name, link in links:
  send_message(name, link)

DIALOGFLOW_PROJECT_ID = 'tinderbot-orwp'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = '1234567abcdef.json'
SESSION_ID = 'current-user-id'
def send_message(name, link):
 driver.get(link)
 sleep(2)
 text_to_be_analyzed = name

 session_client = dialogflow.SessionsClient()
 session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

 text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
 query_input = dialogflow.types.QueryInput(text=text_input)

 try:
  response = session_client.detect_intent(session=session, query_input=query_input)
 except InvalidArgument:
  raise

 print("Query text:", response.query_result.query_text)
 print("Detected intent:", response.query_result.intent.display_name)
 print("Detected intent confidence:", response.query_result.intent_detection_confidence)
 print("Fulfillment text:", response.query_result.fulfillment_text)

 print("Antes de detectar el elemento")
 text_area = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
 print("sending message")
 # message = generate_intro(generate_tinder_message(), name)
 text_area.send_keys(response.query_result.fulfillment_text)
 sleep(2)
 text_area.send_keys(Keys.ENTER)
