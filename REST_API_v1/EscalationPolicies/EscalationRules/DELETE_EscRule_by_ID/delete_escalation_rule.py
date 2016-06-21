#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='P2LK6XG'
ESCALATION_POLICY_RULE_ID='PKEAKH3'


def get_escalation_rule():
    url = 'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}/escalation_rules/{2}'.format(SUBDOMAIN, ESCALATION_POLICY_ID, ESCALATION_POLICY_RULE_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    r = requests.delete(url, headers=headers)
    print r.status_code
    print r.text

