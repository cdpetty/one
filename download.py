import user, os, logger, requests, xattr, binascii
import client as c
from mediafire.client import File, ResourceNotFoundError, NotAFolderError


def download(file_path):
  '''Download the file by name of "file_path"'''
  if (user.is_user_signed_in()):
    client = c.get_client()
    filename = os.path.basename(file_path)
    file_path = sanitize_path(file_path)
    if (os.path.isfile(filename) or os.path.isdir(filename)):
      logger.die('File or dir with name "' + filename + '" in current directory')
    else:
      existance = check_existance(file_path, client)
      if (existance[0]):
        try:
          client.download_file("mf:" + file_path , '.')
          file_info = existance[1]
          xattr.setxattr(filename, 'hash', binascii.a2b_qp(file_info['hash']))
          logger.log('File "' + filename + '" downloaded successfully.')
        except NotAFolderError:
          logger.die('Path "' + remote_path + '" not found on MediaFire')
        except ResourceNotFoundError:
          logger.die('Path "' + remote_path + '" not found on MediaFire.')
        except requests.exceptions.RequestException:
          logger.die('Network error, please check network status and try again')

      else:
        logger.log('File path and name "' + file_path + '" does not exist.')
  else:
    user.get_auth()


def check_existance(file_path, client):
  try:
    contents = client.get_folder_contents_iter('mf:' + os.path.dirname(file_path) + '/')
    for item in contents:
      if type(item) is File:
        if item['filename'] == os.path.basename(file_path):
          return (True, item)
    return (False, None)

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
