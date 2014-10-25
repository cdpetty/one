from mediafire.client import MediaFireClient
import user, requests, logger

# API and Mediafire information
APP_ID='43231'
API_KEY='8g8mn8gcahrr46bs9vhjidd15usnpvnvydzpa5xv'


def get_client(*info):
  ''' returns a mediafireapi.client object
  @email as first parameter
  @password as second parameter
  if no params are passed, then get_client
  pulls the account information from the user's
  saved credentials with the user file'''

  # Create Mediafire client
  try:
    client = MediaFireClient()
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  if (len(info) == 2):
    try:
      client.login(email=info[0],
          password=info[1],
          app_id=APP_ID,
          api_key=API_KEY)
    except requests.exceptions.RequestException:
     logger.die('Network error, please check network status and try again') 
  else:
    try:
      auth = user.get_auth()
      client.login(email=auth[0],
          password=auth[1],
          app_id=APP_ID,
          api_key=API_KEY)
    except requests.exceptions.RequestException:
      logger.die('Network error, please check network status and try again')
  return client

