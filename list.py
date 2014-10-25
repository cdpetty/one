import logger, user, requests
from mediafire.client import File
import client as c

def list_files():
  if (user.is_user_signed_in()):
    contents = get_files()
    if (len(contents) == 0):
      logger.end('No Files Stored')
    else:
      logger.log('Files contained on Mediafire/One:')
      logger.log('   Privacy    Revision   Size       Filename')
      for f in contents:
        logger.log(compose_list_string(f['privacy'], f['revision'], f['size'], f['filename']))
  else:
    user.get_auth()

def get_files():
  try:
    client = c.get_client()
    contents = client.get_folder_contents_iter('mf:/one_storage')
    return list(contents)
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')

def compose_list_string(priv, rev, siz, fil):
  p = [' ']*11
  r = [' ']*11
  s = [' ']*11
  for index, letter in enumerate(list(priv)):
    p[index] = letter
  for index, letter in enumerate(rev):
    r[index] = letter
  for index, letter in enumerate(siz):
    s[index] = letter
  return '   ' + ''.join(p) + ''.join(r) + ''.join(s) + fil 
