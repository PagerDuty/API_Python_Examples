#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
MAINTENANCE_WINDOW_ID='PEP41A8'

def delete_maintenance_window():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.delete(
                    'https://{0}.pagerduty.com/api/v1/maintenance_windows/{1}'.format(SUBDOMAIN, MAINTENANCE_WINDOW_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

