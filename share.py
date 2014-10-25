
from mediafire.client import File
import requests, logger
import client as c

def share(filename):
  exist = get_existance(filename)
  if (exist[1]):
    f = exist[1]
    logger.end(f['links']['normal_download'])
  else:
    logger.die('File "' + filename + '" does not exist')


def get_existance(filename):
  client = c.get_client()
  try:
    contents = client.get_folder_contents_iter('mf:/one_storage/')
    for item in contents:
      if type(item) is File:
        if item['filename'] == filename:
          return (True, item)
    return (False, None)
  except requests.exceptions.RequestException:
    logger.die('Network error, please check network status and try again')
  
