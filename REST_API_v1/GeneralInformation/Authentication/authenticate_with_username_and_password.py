#!/usr/bin/env python
import requests


LOGIN_EMAIL='myemail@example.com'
LOGIN_PASSWORD='secret'
SUBDOMAIN='pdt-dank'
SCHEDULE_ID='PKROVQO'

def schedule_entries():
    url = 'https://{0}.pagerduty.com/api/v1/schedules/{1}/entries'.format(SUBDOMAIN, SCHEDULE_ID)
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.get(url, auth=(LOGIN_EMAIL, LOGIN_PASSWORD), headers=headers)
    print r.status_code

