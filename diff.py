import hashlib, logger, os, requests, subprocess, xattr
import client as c
from mediafire.client import File

def diff(filename):
  '''Use hashlib library to compare sha256 hash of
  current file to the sha256 hash stored on mediafire'''

  full_expansion = get_path_expansion(filename)
  if (os.path.isfile(full_expansion)):
    in_file = open(filename, 'r')
    file_contents = in_file.read().encode('utf-8')

    new_hash = hashlib.sha256(file_contents).hexdigest()
    media_hash = get_hash(os.path.basename(full_expansion))
    try:
      old_hash = xattr.getxattr(full_expansion, 'hash').decode('ascii')
    except OSError:
      old_hash = '' 

    if (media_hash == ''):
      logger.die('No file "' + os.path.basename(full_expansion) + '" in Mediafire')
    else:
      figure_time_scale(media_hash, old_hash, new_hash, os.path.basename(full_expansion))
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

def figure_time_scale(media_hash, old_hash, new_hash, filename):
  if (old_hash == media_hash and new_hash != old_hash and new_hash != media_hash):
    logger.end('One: The local file, "' + filename + '", is ahead of the remote.')
  elif(old_hash == media_hash == new_hash):
    logger.end('One: All files are properly synced.')
  elif(old_hash == new_hash and media_hash != old_hash and media_hash != new_hash):
    logger.end('One: The remote file, "' + filename + '", is ahead of the local file.')
  elif(old_hash != new_hash != media_hash):
    logger.end('One: The remote and head are out of sync.')
