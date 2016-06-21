#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='zma9XjUU8tAjuzqnts1k'
USER_ID='PG9E0O0'
CONTACT_METHOD_ID='PIEGIBK'


def create_notification_rule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {"notification_rule": {
                                        "contact_method_id": "{0}".format(CONTACT_METHOD_ID),
                                        "start_delay_in_minutes":12,
                                    }
    }
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/notification_rules'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
                    data=json.dumps(payload),
    )
    print r.status_code
    print r.text

