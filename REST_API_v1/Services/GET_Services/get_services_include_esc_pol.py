#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_services_include_esc_pols():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        'include[]':'escalation_policy',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/services'.format(SUBDOMAIN),
                    headers=headers,
                    params=payload,
    )
    print r.status_code
    print r.text

