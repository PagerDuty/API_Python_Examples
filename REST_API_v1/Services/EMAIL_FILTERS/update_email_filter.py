#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='P295MFW'
EMAIL_FILTER_ID='P2T76VF'


def update_email_filter():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({"email_filter":{
                            "from_email_mode":"match",
                            "from_email_regex":"[rR]yan",
                            }
                        }
    )

    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/services/{1}/email_filters/{2}'.format(SUBDOMAIN, SERVICE_ID, EMAIL_FILTER_ID),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

