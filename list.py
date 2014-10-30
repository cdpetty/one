import logger, user, requests
from mediafire.client import File, Folder, ResourceNotFoundError
import client as c

def list_files(path):
  if (user.is_user_signed_in()):
    sanitized_path = sanitize_path(path)
    contents = get_files(sanitized_path)
    if (len(contents) == 0):
      logger.end('No Files Stored')
    else:
      logger.log('Files contained on MediaFire/One:')
      logger.log('   Type       Privacy    Revision   Size/File_Count    Filename')
      for f in contents:
        if (type(f) == File):
          logger.log(compose_list_string('File', f['privacy'], f['revision'], f['size'], f['filename']))
        elif (type(f) == Folder):
          logger.log(compose_list_string('Folder', f['privacy'], f['revision'], f['file_count'], f['name']))
  else:
    user.get_auth()

def get_files(path):
  try:
    client = c.get_client()
    contents = client.get_folder_contents_iter('mf:' + path)
    return list(contents)
  except ResourceNotFoundError:
    logger.die('Path: "' + path + '" does not exist')
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  
def compose_list_string(media_type, priv, rev, siz, fil):
  t = [' ']*11
  p = [' ']*11
  r = [' ']*11
  s = [' ']*19
  for index, letter in enumerate(list(media_type)):
    t[index] = letter
  for index, letter in enumerate(list(priv)):
    p[index] = letter
  for index, letter in enumerate(list(rev)):
    r[index] = letter
  for index, letter in enumerate(list(siz)):
    s[index] = letter
  return '   ' + ''.join(t) + ''.join(p) + ''.join(r) + ''.join(s) + fil 

def sanitize_path(path):
  if path:
    if (path[0] != '/'):
      path = '/' + path
    if (path[-1] == '/'):
      path = path[0:-1]
    return path
  else:
    return '/'
