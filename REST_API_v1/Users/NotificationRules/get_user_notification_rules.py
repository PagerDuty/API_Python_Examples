#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='zma9XjUU8tAjuzqnts1k'
USER_ID='PG9E0O0'


def get_user_notification_rules():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/notification_rules'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

