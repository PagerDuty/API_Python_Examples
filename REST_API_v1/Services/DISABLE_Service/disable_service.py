#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='PJGPSVN'
REQUESTER_ID='PJR28TQ'


def disable_service():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
                        "requester_id":"{0}".format(REQUESTER_ID)
                        }
    )
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/services/{1}/disable'.format(SUBDOMAIN, SERVICE_ID),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

