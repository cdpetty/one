import user, os, logger, requests
import client as c
from mediafire.client import File

def upload(path):
  '''upload a file with the directory path "path"'''
  if (user.is_user_signed_in()):
    f = get_path_expansion(path)
    if (os.path.isfile(f)):
      client = c.get_client() 
      if (check_existance(os.path.basename(f), client)):
        logger.die('File with name "' + os.path.basename(f) + '" already exists')
      else:
        try:
          client.upload_file(f, 'mf:/one_storage/')
          logger.log('File "' + os.path.basename(f) + '" has been succesfully uploaded.')
        except requests.exceptions.RequestException:
          logger.die('Network error, please check network status and try again')
    elif (os.path.isdir(f)):
      logger.die('File, "' + f + '", is a directory')
    else:
      logger.die('No such file or directory')
  else:
    user.get_auth()

def get_path_expansion(path):
  return os.path.abspath(os.path.expanduser(path))

def check_existance(filename, client):
  try:
    contents = client.get_folder_contents_iter('mf:/one_storage')
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return True
    return False
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
