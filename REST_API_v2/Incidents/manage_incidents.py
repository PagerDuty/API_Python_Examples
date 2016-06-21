#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json

# Update to match your API key
API_KEY = '3c3gRvzx7uGfMYEnWKvF'

# Update to match your email address
EMAIL = 'lucas@pagerduty.com'

# Update to match your chosen parameters for each incident
INCIDENT_ONE_ID = 'P1DIBFS'
INCIDENT_ONE_TYPE = 'incident'
INCIDENT_ONE_SUMMARY = 'Enter your incident one summary here'
INCIDENT_ONE_STATUS = 'resolved'
INCIDENT_ONE_ESCALATION_LEVEL = 1
INCIDENT_ONE_ASSIGNED_TO_USER = ''
INCIDENT_ONE_ESCALATION_POLICY = ''

INCIDENT_TWO_ID = 'PKSPVAW'
INCIDENT_TWO_TYPE = 'incident'
INCIDENT_TWO_SUMMARY = 'Enter your incident two summary here'
INCIDENT_TWO_STATUS = 'resolved'
INCIDENT_TWO_ESCALATION_LEVEL = 1
INCIDENT_TWO_ASSIGNED_TO_USER = ''
INCIDENT_TWO_ESCALATION_POLICY = ''

def manage_incidents():
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY,
        'Content-type': 'application/json',
        'From': EMAIL
    }
    payload = {
        'incidents': [{
            'id': INCIDENT_ONE_ID,
            'type': INCIDENT_ONE_TYPE,
            'summary': INCIDENT_ONE_SUMMARY,
            'status': INCIDENT_ONE_STATUS,
            'escalation_level': INCIDENT_ONE_ESCALATION_LEVEL,
            'assigned_to_user': INCIDENT_ONE_ASSIGNED_TO_USER,
            'escalation_policy': INCIDENT_ONE_ESCALATION_POLICY
        },
        {
            'id': INCIDENT_TWO_ID,
            'type': INCIDENT_TWO_TYPE,
            'summary': INCIDENT_TWO_SUMMARY,
            'status': INCIDENT_TWO_STATUS,
            'escalation_level': INCIDENT_TWO_ESCALATION_LEVEL,
            'assigned_to_user': INCIDENT_TWO_ASSIGNED_TO_USER,
            'escalation_policy': INCIDENT_TWO_ESCALATION_POLICY
        }]
    }
    r = requests.put(url, headers=headers, data=json.dumps(payload))
    print 'Status Code: ' + str(r.status_code)
    print r.json()

if __name__ == '__main__':
    manage_incidents()
