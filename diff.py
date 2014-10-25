import hashlib, logger, os, requests
import client as c
from mediafire.client import File

def diff(filename):
  '''Use hashlib library to compare sha256 hash of
  current file to the sha256 hash stored on mediafire'''

  full_expansion = get_path_expansion(filename)
  if (os.path.isfile(full_expansion)):
    in_file = open(filename, 'r')
    file_contents = in_file.read().encode('utf-8')
    hashed = hashlib.sha256(file_contents).hexdigest()
    media_hash = get_hash(os.path.basename(full_expansion))
    if (media_hash == ''):
      logger.die('No file "' + os.path.basename(full_expansion) + '" in Mediafire')
    else:
      if (hashed == media_hash):
        logger.end('Local file is up to date')
      else:
        logger.end('Local file is either behind or ahead')
  else:
    logger.die('No local file "' + os.path.basename(full_expansion) + '" found')

def get_path_expansion(path):
  return os.path.abspath(os.path.expanduser(path))

def get_hash(filename):
  try:
    client = c.get_client()  
    contents = client.get_folder_contents_iter('mf:/one_storage/')
    for item in contents:
      if type(item) is File:
        if (item['filename'] == filename):
          return item['hash']
    return ''
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
