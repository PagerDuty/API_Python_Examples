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

# Update to match ID of resource you want to update
ID = 'P8RK2P8'

# Update to match your chosen parameters
NAME = 'Insert your service name here'
DESCRIPTION = 'Insert your service description here'
ESCALATION_POLICY_ID = 'PIX2DN3'
ACKNOWLEDGEMENT_TIMEOUT = 60 * 30  # 30 minutes
AUTO_RESOLVE_TIMEOUT = 60 * 60 * 4  # 4 hours
SEVERITY_FILTER = ''


def update_service():
    url = 'https://api.pagerduty.com/services/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json'
    }
    payload = {
        'service': {
            'name': NAME,
            'description': DESCRIPTION,
            'escalation_policy': {
                'id': ESCALATION_POLICY_ID,
                'type': 'escalation_policy_reference'
            },
            'acknowledgement_timeout': ACKNOWLEDGEMENT_TIMEOUT,
            'auto_resolve_timeout': AUTO_RESOLVE_TIMEOUT,
            'severity_filter': SEVERITY_FILTER
        }
    }
    r = requests.put(url, headers=headers, data=json.dumps(payload))
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    update_service()
