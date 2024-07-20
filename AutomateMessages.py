"""
Sends a message to my phone number every day at 10 am
"""

import requests
import time
import schedule
from SuperSecret import phone

def task():
  resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': 'lol.',
    'key': 'textbelt',
  })
  print(resp.json())

schedule.every().day.at('10:00').do(task)

while True:
  schedule.run_pending()
  time.sleep(1)
