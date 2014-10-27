import sys

def log(*statements):
  phrase = ' '.join(map(str, statements)) + '\n'
  sys.stdout.write(phrase)
  sys.stdout.flush()

def die(statement):
  sys.stderr.write('One: error: ' + statement + '\n')
  sys.exit(1)

def end(statement):
  log(statement + '\n')
  sys.exit(0)

