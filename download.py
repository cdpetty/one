import user, os, logger, requests
import client as c
from mediafire.client import File


def download(filename):
  '''Download the file by name of "filename"'''
  if (user.is_user_signed_in()):
    client = c.get_client()
    if (os.path.isfile(filename) or os.path.isdir(filename)):
      logger.die('File or dir with name "' + filename + '" in current directory')
    else:
      if (check_existance(filename, client)):
        client.download_file("mf:/one_storage/" + filename , '.')
        try:
          logger.log('File "' + filename + '" downloaded successfully.')
        except requests.exceptions.RequestException:
          logger.die('Network error, please check network status and try again')

      else:
        logger.log('File "' + filename + '" does not exist.')
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
  
