#!/usr/bin/env python
#
# Copyright (c) 2018, PagerDuty, Inc. <info@pagerduty.com>
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

# --------------------------------------------------------------------------------
#                               INSTRUCTIONS
#
# This script creates a maintenance window on all services. It does not support
# pagination, so it is limited to 100 services (by default it will sort by name)
#
# REQUIRED: API_KEY, EMAIL
#
# OPTIONAL: You can specify the delay before starting the maintenance window, as
# well as the duration. If you prefer, you can instead input the date in `start`
# and `end` below.
#
# # Date format: '2018-09-30T14:00:00'
#
# There are also optional parameters for filtering services or maintenance windows.
#
# --------------------------------------------------------------------------------

import requests
import json
import datetime

# Update to match your API key
API_KEY = ''

# Update to match your login email
EMAIL = ''

# get_services parameters
TEAM_IDS = []
TIME_ZONE = 'UTC'
SORT_BY = 'name'
QUERY = ''
INCLUDE = []

# set the delay and duration of maintenance windows
maintenance_start_delay_in_minutes = 0
maintenance_duration_in_minutes = 10

# This gets the timezone of your local server - for UTC, use datetime.datetime.utcnow()
current_time = datetime.datetime.now()
start_time = str(current_time + datetime.timedelta(minutes = maintenance_start_delay_in_minutes))
end_time = str(current_time + datetime.timedelta(minutes = maintenance_start_delay_in_minutes + maintenance_duration_in_minutes))

# You can also specify a start or end date here instead (Date format: '2018-09-30T14:00:00')
start = start_time
end = end_time
START_TIME = (start[0:10] + 'T' + start[11:19])
END_TIME = (end[0:10] + 'T' + end[11:19])
DESCRIPTION = 'This maintenance window was created from a python script'
TEAMS = []
TYPE = 'maintenance_window'

# -----------------------------------------------------------------------


def get_services():
    print('Getting services...', flush=True)
    url = 'https://api.pagerduty.com/services?total=true'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'team_ids[]': TEAM_IDS,
        'time_zone': TIME_ZONE,
        'sort_by': SORT_BY,
        'query': QUERY,
        'include[]': INCLUDE,
        'limit': 100
    }
    r = requests.get(url, headers=headers, params=payload)
    print('\tStatus code: {code}'.format(code=r.status_code))
    if r.status_code < 200 or r.status_code >= 204:
        print("\tThere was an error getting your services.")
        print("\tPlease ensure that the login email and v2 REST API key in this script are correct.")
        print(r.text)
        SERVICES = []
        return SERVICES
    #print(r.json())
    data = json.loads(r.text)
    total_services = data['total']
    print('Creating maintenance window on {total_services} services...'.format(total_services=total_services))
    SERVICES = data['services']
    return SERVICES


def create_maintenance_window(SERVICES):
    url = 'https://api.pagerduty.com/maintenance_windows'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
        'From': EMAIL
    }

    payload = {
        'maintenance_window': {
            'start_time': START_TIME,
            'end_time': END_TIME,
            'description': DESCRIPTION,
            'services': SERVICES,
            'teams': TEAMS,
            'type': TYPE
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print('\tStatus code: {code}'.format(code=str(r.status_code)))
    if r.status_code >= 200 and r.status_code < 204:
        print("Maintenance window successfully created:")
        print("\tStart: ", START_TIME)
        print("\tEnd: ", END_TIME)
        print("\tServices: ")
        for service in range(int(len(SERVICES))):
            print("\t\t", SERVICES[service]['id'])
    else:
        print("\tThere was an error creating this maintenance window.")
        print("\tPlease ensure that the login email and v2 REST API key in this script have proper permissions")
    # print(r.json())


if __name__ == '__main__':
    if EMAIL == '':
        print("Please add your login email to this script and run it again.")
    elif API_KEY == '':
        print("Please add your v2 REST API key to this script and run it again.")
    else:
        SERVICES = get_services()
        if SERVICES != []:
            create_maintenance_window(SERVICES)
