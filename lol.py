import requests

def send_email(email, link):
  data={'api_user':'cdpetty', 'api_key':'password1', 'to[]':email, 'subject': 'Sharing with One', 'text': link, 'from':'one@one.com'}
  r = requests.post('https://api.sendgrid.com/api/mail.send.json', data=data)



