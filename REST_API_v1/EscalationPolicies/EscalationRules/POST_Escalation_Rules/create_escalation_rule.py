#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='P2LK6XG'


def create_escalation_rule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {"escalation_rule":{"escalation_delay_in_minutes":10,"targets":[{"type":"user","id":"PJR28TQ"}]}}
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}/escalation_rules'.format(SUBDOMAIN, ESCALATION_POLICY_ID),
                    headers=headers,
                    data=json.dumps(params)
    )
    print r.status_code
    print r.text

