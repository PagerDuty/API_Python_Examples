#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='P295MFW'
EMAIL_FILTER_ID='PY88T3A'


def delete_email_filter():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.delete(
                    'https://{0}.pagerduty.com/api/v1/services/{1}/email_filters/{2}'.format(SUBDOMAIN, SERVICE_ID, EMAIL_FILTER_ID, EMAIL_FILTER_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

