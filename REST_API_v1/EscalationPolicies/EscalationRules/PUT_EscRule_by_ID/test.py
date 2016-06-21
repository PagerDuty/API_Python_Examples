#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='P2LK6XG'
ESCALATION_RULE_ID='PCPB3KW'


def update_escalation_rule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {
        "escalation_delay_in_minutes":140,
        "targets":[
            {
                "type":"schedule",
                "id":"PBCHDG6"
            }
        ]
    }
    r = requests.put(
                        'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}/escalation_rules/{2}'.format(SUBDOMAIN, ESCALATION_POLICY_ID, ESCALATION_RULE_ID),
                        headers=headers,
                        data=json.dumps(params)
        )
    print r.status_code
    print r.text
update_escalation_rule()

