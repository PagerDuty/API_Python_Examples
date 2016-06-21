#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='zma9XjUU8tAjuzqnts1k'
USER_ID='PG9E0O0'
NOTIFICATION_RULE_ID='PKQMJN2'


def delete_notification_rule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.delete(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/notification_rules/{2}'.format(SUBDOMAIN, USER_ID, NOTIFICATION_RULE_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

