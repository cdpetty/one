from mediafire.client import File
import user, logger, argparse, requests
import client as c

def delete(filename):
  '''Deletes file with name "filename" from
  Mediafire account.'''
  if (user.is_user_signed_in()):
    client = c.get_client()
    if (check_existance(filename, client)):
      try: 
        client.delete_file('mf:/one_storage/' + filename)
        logger.log('File "' + filename + '" successfully deleted.')
      except requests.exceptions.RequestException:
        logger.die('Network error, please check network status and try again')
    else:
      logger.die('File "' + filename + '" does not exist.')
  else:
    user.get_auth()

def check_existance(filename, client):
  try:
    contents = client.get_folder_contents_iter('mf:/one_storage/')
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return True
    return False
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')


