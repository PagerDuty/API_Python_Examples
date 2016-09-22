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
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
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
OVERFLOW = False

# Update to match your chosen parameters for the overall schedule
TYPE = 'schedule'
SUMMARY = 'Insert your schedule summary here'
NAME = 'Insert your schedule name here'
TIME_ZONE = 'UTC'
ESCALATION_POLICIES = []
TEAMS = []

# Update to match your chosen parameters for each schedule layer
LAYER_ONE_START = '2016-05-23T18:00:00-07:00'
LAYER_ONE_END = '2016-06-23T18:00:00-07:00'
LAYER_ONE_USERS = [
    {
        'id': 'PAZZ8LZ',
        'type': 'user_reference'
    },
    {
        'id': 'P1PJUIZ',
        'type': 'user_reference'
    }
]
LAYER_ONE_RESTRICTION_TYPE = 'Daily'
LAYER_ONE_RESTRICTIONS = []
LAYER_ONE_ROTATION_VIRTUAL_START = '2016-05-23T18:00:00-07:00'
LAYER_ONE_PRIORITY = 1
LAYER_ONE_ROTATION_TURN_LENGTH_SECONDS = 60 * 60 * 24  # 24 hours
LAYER_ONE_NAME = 'Insert layer one name here'

LAYER_TWO_START = '2016-05-23T18:00:00-07:00'
LAYER_TWO_END = '2016-06-23T18:00:00-07:00'
LAYER_TWO_USERS = [
    {
        'id': 'POC4AOM',
        'type': 'user_reference'
    },
    {
        'id': 'PLUWO2C',
        'type': 'user_reference'
    }
]
LAYER_TWO_RESTRICTION_TYPE = 'Weekly'
LAYER_TWO_RESTRICTIONS = []
LAYER_TWO_ROTATION_VIRTUAL_START = '2016-05-23T18:00:00-07:00'
LAYER_TWO_PRIORITY = 1
LAYER_TWO_ROTATION_TURN_LENGTH_SECONDS = 60 * 60 * 24  # 24 hours
LAYER_TWO_NAME = 'Insert layer two name here'


def create_schedule():
    url = 'https://api.pagerduty.com/schedules'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY,
        'Content-type': 'application/json'
    }
    payload = {
        'overflow': OVERFLOW,
        'schedule': {
            'type': TYPE,
            'summary': SUMMARY,
            'name': NAME,
            'time_zone': TIME_ZONE,
            'escalation_policies': ESCALATION_POLICIES,
            'teams': TEAMS,
            'schedule_layers': [
                {
                    'start': LAYER_ONE_START,
                    'end': LAYER_ONE_END,
                    'users': LAYER_ONE_USERS,
                    'restriction_type': LAYER_ONE_RESTRICTION_TYPE,
                    'restrictions': LAYER_ONE_RESTRICTIONS,
                    'rotation_virtual_start': LAYER_ONE_ROTATION_VIRTUAL_START,
                    'priority': LAYER_ONE_PRIORITY,
                    'rotation_turn_length_seconds':
                    LAYER_ONE_ROTATION_TURN_LENGTH_SECONDS,
                    'name': LAYER_ONE_NAME
                },
                {
                    'start': LAYER_TWO_START,
                    'end': LAYER_TWO_END,
                    'users': LAYER_TWO_USERS,
                    'restriction_type': LAYER_TWO_RESTRICTION_TYPE,
                    'restrictions': LAYER_TWO_RESTRICTIONS,
                    'rotation_virtual_start': LAYER_TWO_ROTATION_VIRTUAL_START,
                    'priority': LAYER_TWO_PRIORITY,
                    'rotation_turn_length_seconds':
                    LAYER_TWO_ROTATION_TURN_LENGTH_SECONDS,
                    'name': LAYER_TWO_NAME
                }
            ]
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print 'Status Code: ' + str(r.status_code)
    print r.json()

if __name__ == '__main__':
    create_schedule()
