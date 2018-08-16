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
# This script will search for all currently active maintenance windows on all
# services and end them. It does not support pagination, so it is limited to 100
# maintenance windows (by default it will sort by name)
#
# REQUIRED: API_KEY, EMAIL
#
# OPTIONAL: You can set the END_TIME to a future date if required.
#
# # Date format: '2018-09-30T14:00:00'
#
# There are also other parameters for filtering maintenance windows.
#
# --------------------------------------------------------------------------------

import requests
import datetime

current_time = datetime.datetime.now()

# Update to match your v2 REST API key
API_KEY = ''

# Update to match your login email
EMAIL = ''

# Update to match your chosen parameters
# You can also specify a different end date here instead (Date format: '2018-09-30T14:00:00')
END_TIME = current_time
TEAM_IDS = []
SERVICE_IDS = []
INCLUDE = []
FILTER = 'ongoing'
QUERY = ''


def get_maintenance_windows():
    url = 'https://api.pagerduty.com/maintenance_windows?total=true'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'team_ids[]': TEAM_IDS,
        'service_ids[]': SERVICE_IDS,
        'include[]': INCLUDE,
        'filter': FILTER,
        'query': QUERY
    }
    maintenance_windows_ids = []
    r = requests.get(url, headers=headers, params=payload)
    print('Getting ongoing maintenance windows...')
    print('\tStatus Code: {code}'.format(code=r.status_code))
    if r.status_code < 200 or r.status_code >= 204:
        print("\tThere was an error getting your maintenance windows.")
        print("\tPlease ensure that the login email and v2 REST API key in this script are correct.")
        print(r.text)
        return maintenance_windows_ids
    maintenance_list = r.json()
    ids = maintenance_list['maintenance_windows']
    total = int(maintenance_list['total'])

    if total > 0:
        if total == 1:
            print("\t1 ongoing maintenance window found:")
        if total == 2:
            print("\t", total, 'ongoing maintenance windows found')
        for maintenance_window in range(total):
            maintenance_windows_ids.append(ids[maintenance_window]['id'])
        print("\t", maintenance_windows_ids)
    else:
        print("No ongoing maintenance windows found")
    return maintenance_windows_ids


def end_maintenance_window(MAINTENANCE_WINDOWS):
    if len(MAINTENANCE_WINDOWS) == 1:
        print("Ending maintenance window...")
    else:
        print("Ending maintenance windows...")
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    for maintenance_window in range(len(MAINTENANCE_WINDOWS)):
        url = 'https://api.pagerduty.com/maintenance_windows/{id}'.format(id=MAINTENANCE_WINDOWS[maintenance_window])
        print("\t", str(MAINTENANCE_WINDOWS[maintenance_window]))
        r = requests.delete(url, headers=headers)
        print('\tStatus Code: {code}'.format(code=r.status_code))
        if r.status_code == 204:
            print('\tMaintenance window ended successfully!')
        else:
            print("\tThere was an error ending this maintenance window")
            print("\tPlease ensure that the login email and v2 REST API key in this script have proper permissions")
            return maintenance_windows_ids
            print(r.text)

if __name__ == '__main__':

    if EMAIL == '':
        print("Please add your login email to this script and run it again.")
    elif API_KEY == '':
        print("Please add your v2 REST API key to this script and run it again.")
    else:
        MAINTENANCE_WINDOWS = get_maintenance_windows()
        if MAINTENANCE_WINDOWS != []:
            end_maintenance_window(MAINTENANCE_WINDOWS)


# -----------------------------------------------------------------------

