#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='P295MFW'
EMAIL_FILTER_ID='PY88T3A'


def create_email_filter():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
                        "email_filter":{
                            "body_mode":"no-match",
                            "body_regex":"sev 3",
                            }
                        }
    )

    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/services/{1}/email_filters'.format(SUBDOMAIN, SERVICE_ID),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

