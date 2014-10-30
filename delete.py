from mediafire.client import File, NotAFolderError, ResourceNotFoundError
import user, logger, argparse, requests, os
import client as c

def delete(file_path):
  '''Deletes file with name "filename" from
  MediaFire account.'''
  if (user.is_user_signed_in()):
    client = c.get_client()
    file_path = sanitize_path(file_path)
    if (check_existance(file_path, client)):
      try: 
        client.delete_file('mf:' + file_path)
        logger.log('File "' + os.path.basename(file_path) + '" successfully deleted.')
      except requests.exceptions.RequestException:
        logger.die('Network error, please check network status and try again')
    else:
      logger.die('File with path and name "' + file_path + '" does not exist.')
  else:
    user.get_auth()

def check_existance(file_path, client):
  try:
    contents = client.get_folder_contents_iter('mf:' + os.path.dirname(file_path) + '/')
    for item in contents:
      if type(item) is File:
        if item['filename'] == os.path.basename(file_path):
          return True
    return False
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  except NotAFolderError:
    logger.die('Path "' + file_path + '" not found on MediaFire')
  except ResourceNotFoundError:
    logger.die('Path "' + file_path + '" not found on MediaFire.')


def sanitize_path(path):
  path = os.path.normpath(path)
  if (path[0] != '/'):
    path = '/' + path
  if (path[-1] == '/'):
    path = path[0:-1]
  return path
