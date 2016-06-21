#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='PNJ1R1Y'

def get_escalation_policies():
    url = 'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}'.format(SUBDOMAIN, ESCALATION_POLICY_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    r = requests.delete(url, headers=headers)
    print r.status_code
    print r.text

