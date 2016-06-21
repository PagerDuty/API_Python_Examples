#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def create_escalation_policy():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {
      "name": "Escalation Policy",
      "escalation_rules": [
        {
          "escalation_delay_in_minutes": 22,
          "targets": [
            {
              "type": "user",
              "id": "PJR28TQ"
            }
          ]
        }
      ],
      "num_loops": 2
    }
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/escalation_policies'.format(SUBDOMAIN),
                    headers=headers,
                    data=json.dumps(params)
    )
    print r.status_code
    print r.text

