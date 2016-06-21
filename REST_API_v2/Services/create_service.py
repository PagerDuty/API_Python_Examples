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

# Update to match your chosen parameters
NAME = 'Insert service name here'
DESCRIPTION = 'Insert service description here'
ESCALATION_POLICY_ID = 'PIX2DN3'
TYPE = 'service'
AUTO_RESOLVE_TIMEOUT = 14400 # 4 hours
ACKNOWLEDGEMENT_TIMEOUT = 1800 # 30 minutes
TEAMS = []
INCIDENT_URGENCY = 'high' # if using support hours, this urgency is used during support hours
OUTSIDE_SUPPORT_HOURS_URGENCY = 'low'
SCHEDULED_ACTIONS = []
SUPPORT_HOURS = {
    'type': 'fixed_time_per_day',
    'time_zone': 'UTC',
    'days_of_week': [1, 2, 3, 4, 5],
    'start_time': '09:00:00',
    'end_time': '17:00:00'
}
INTEGRATIONS = []
ADDONS = []

def create_service():
    url = 'https://api.pagerduty.com/services'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY,
        'Content-type': 'application/json'
    }
    payload = {
        'service': {
            'name': NAME,
            'description': DESCRIPTION,
            'escalation_policy': {
                'id': ESCALATION_POLICY_ID,
                'type': 'escalation_policy'
            },
            'type': TYPE,
            'auto_resolve_timeout': AUTO_RESOLVE_TIMEOUT,
            'acknowledgement_timeout': ACKNOWLEDGEMENT_TIMEOUT,
            'teams': TEAMS,
            'scheduled_actions': SCHEDULED_ACTIONS,
            'integrations': INTEGRATIONS,
            'addons': ADDONS,
            'support_hours': SUPPORT_HOURS
        }
    }
    if SUPPORT_HOURS == None:
        payload['service']['incident_urgency_rule'] = {
            'type': 'constant',
            'urgency': INCIDENT_URGENCY
        }
    else:
        payload['service']['incident_urgency_rule'] = {
            'type': 'use_support_hours',
            'during_support_hours': {
                'type': 'constant',
                'urgency': INCIDENT_URGENCY
            },
            'outside_support_hours': {
                'type': 'constant',
                'urgency': OUTSIDE_SUPPORT_HOURS_URGENCY
            }
        }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print 'Status Code: ' + str(r.status_code)
    print r.json()

if __name__ == '__main__':
    create_service()
