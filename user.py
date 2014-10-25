from mediafire.client import Folder
import mediafire, requests, getpass, logger
import os.path as p
import os
import client as c

INFO_PATH = p.join(p.expanduser('~'), '.one')

def get_auth():
  if (is_user_signed_in()):
    in_file = open(INFO_PATH, 'r')
    name = in_file.readline()
    password = in_file.readline()
    return (name.strip(), password.strip())
  else:
    sign_in()

def is_user_signed_in():
  return p.isfile(INFO_PATH) 

def sign_in():
  is_old = input('Do you already have a Mediafire account? [y/n] ')
  if (is_old[0].lower() == 'y'):
    email = input('What is your email: ').lower()
    password = getpass.getpass('What is your password: ')
    existance = check_existance(email, password) 
    if (existance[0]):
      ofstream = open(INFO_PATH, 'w')
      ofstream.write(email + '\n') 
      ofstream.write(password)
      ofstream.close()
      client = existance[1]
      if (not check_one_existance(client)):
        try:
          client.create_folder('mf:/one_storage/')     
        except requests.exceptions.RequestException:
          logger.die('Network error, please check network status and try again')
      logger.end('You are signed in!')
    else:
      logger.die('Either your credentials are incorrect or your account does not exist.\nPlease try again or see Mediafire.com')
  elif (is_old[0].lower() == 'n'):
      logger.end('Please go to Mediafire.com and create an account.') 
  else:
    logger.log('Please answer with a a "n" or "y"')
    sign_in()

def check_existance(email, password):
  try:
    client = c.get_client(email, password) 
    return (True, client)
  except (mediafire.api.MediaFireApiError):
    return (False, None)
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')

def check_one_existance(client):
  try:
    users = client.get_folder_contents_iter("mf:/")
    for name in users:
      if type(name) is Folder:
        if name['name'] == 'one_storage':
          return True
    return False
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')

