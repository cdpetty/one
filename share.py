from mediafire.client import File
import requests, logger, lol
import client as c

def share(filename):
  exist = get_existance(filename)
  if (exist[1]):
    f = exist[1]
    mail(f['links']['normal_download'])
    logger.end(f['links']['normal_download'])
  else:
    logger.die('File "' + filename + '" does not exist')


def mail(link):
  send_mail = input('Send link in an email? [y/n]')
  if (send_mail[0].lower() == 'y'):
    which_email = input('Email address: ')
    lol.send_email(which_email, link)
  

def get_existance(filename):
  client = c.get_client()
  try:
    contents = client.get_folder_contents_iter('mf:/one_storage/')
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return (True, item)
    return (False, None)
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  
