#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='PXV2VTJ'
ESCALATION_POLICY_ID='PLYUUBF'


def update_service():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
                        "service":{
                            "name":"My New Name",
                            "description":"Brand New Description",
                            "escalation_policy_id":"{0}".format(ESCALATION_POLICY_ID)
                        }
                    }
    )
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/services/{1}'.format(SUBDOMAIN, SERVICE_ID),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

