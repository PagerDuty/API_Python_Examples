#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_maintenance_windows():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        'query':'ruby 1.9 migration',
        'service_ids[]':'PY4XIXJ',
        'filter':'ongoing',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/maintenance_windows'.format(SUBDOMAIN),
                    headers=headers,
                    params=payload,
    )
    print r.status_code
    print r.text

