import user, os, logger, requests, xattr, binascii
import client as c
from mediafire.client import File, ResourceNotFoundError, NotAFolderError

def upload(path, remote_path=''):
  '''upload a file with the directory path "path"'''
  if (user.is_user_signed_in()):
    remote_path = sanitize_path(remote_path)
    full_path_expansion = get_path_expansion(path)
    file_name = os.path.basename(full_path_expansion)
    if (os.path.isfile(full_path_expansion)):
        
      client = c.get_client() 
      if (check_existance(file_name, remote_path, client)):
        logger.die('File with name "' + file_name + '" already exists')
      else:
        try:
          client.upload_file(full_path_expansion, 'mf:' + remote_path + '/')
          #updated_hash = get_hash(full_path_expansion, client)
          #xattr.setxattr(f, 'hash', binascii.a2b_qp(updated_hash))
          logger.log('File "' + file_name + '" has been succesfully uploaded.')
        except ResourceNotFoundError:
          Logger.die('Path "' + remote_path + '" not found.')
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

def check_existance(filename, remote_path, client):
  try:
    contents = client.get_folder_contents_iter('mf:' + remote_path)
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return True
    return False
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  except NotAFolderError:
    logger.die('Path "' + remote_path + '" not found on MediaFire')
  except ResourceNotFoundError:
    logger.die('Path "' + remote_path + '" not found on MediaFire.')


def sanitize_path(path):
  if path:
    if (path[0] != '/'):
      path = '/' + path
    if (path[-1] == '/'):
      path = path[0:-1]
    return path
  return ''
