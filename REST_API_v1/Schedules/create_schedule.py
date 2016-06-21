#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def create_schedule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({"schedule":{"id":"P5WPTAH","name":"TestJulianStuff","time_zone":"UTC","today":"2014-06-12","escalation_policies":[],"description":"","schedule_layers":[{"name":"Schedule Layer 1","rendered_schedule_entries":[],"id":"PSJCVEV","priority":0,"start":"2014-06-12T22:55:05Z","end":None,"restriction_type":None,"rotation_virtual_start":"2014-06-08T00:00:00Z","rotation_turn_length_seconds":86400,"users":[{"member_order":1,"user":{"id":"PJR28TQ","name":"Dan Khersonsky","email":"dkhersonsky@pagerduty.com","color":"purple"}}],"restrictions":[],"rendered_coverage_percentage":0.0}],"overrides_subschedule":{"name":"Overrides","rendered_schedule_entries":[]},"final_schedule":{"name":"Final Schedule","rendered_schedule_entries":[],"rendered_coverage_percentage":0.0}}})

    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/schedules'.format(SUBDOMAIN),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

