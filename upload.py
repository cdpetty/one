import user, os, logger, requests, xattr, binascii
import client as c
from mediafire.client import File

def upload(path):
  '''upload a file with the directory path "path"'''
  if (user.is_user_signed_in()):
    full_path_expansion = get_path_expansion(path)
    file_name = os.path.basename(full_path_expansion)
    if (os.path.isfile(full_path_expansion)):
        
      client = c.get_client() 
      if (check_existance(file_name, client)):
        logger.die('File with name "' + file_name + '" already exists')
      else:
        try:
          client.upload_file(full_path_expansion, 'mf:/one_storage/')
          #updated_hash = get_hash(full_path_expansion, client)
          #xattr.setxattr(f, 'hash', binascii.a2b_qp(updated_hash))
          logger.log('File "' + file_name + '" has been succesfully uploaded.')
        except requests.exceptions.RequestException:
          logger.die('Network error, please check network status and try again')

    elif (os.path.isdir(full_path_expansion)):
      logger.die('File, "' + full_path_expansion + '", is a directory')
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

'''def get_hash(filename, client):
  try:
    contents = client.get_folder_contents_iter('mf:/one_storage')
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return  item['hash']
    return '' 
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')'''

