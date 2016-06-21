#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='P2LK6XG'


def update_escalation_policy():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {
      "name": "Escalation Policy 222222"
    }
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}'.format(SUBDOMAIN, ESCALATION_POLICY_ID),
                    headers=headers,
                    data=json.dumps(params)
    )
    print r.status_code
    print r.text

