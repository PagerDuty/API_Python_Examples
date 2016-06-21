#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='PLYUUBF'


def create_service():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
                        "service":{
                            "name":"default",
                            "description":"service sevname10",
                            "escalation_policy_id":"{0}".format(ESCALATION_POLICY_ID),
                            "type":"generic_events_api",
                            }
                        }
    )
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/services'.format(SUBDOMAIN),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

