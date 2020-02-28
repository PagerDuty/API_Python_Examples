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

import json
import csv

import requests


# Update to match your API key
API_KEY = 'XXXXXXXX'

# Update to match your PagerDuty account's email address
PD_EMAIL = 'foo@bar.com'

CSV_FILE = 'users.csv'
ENDPOINT = 'https://api.pagerduty.com/users'


class User():
    def __init__(self, data):
        self.name = data[0]
        self.email = data[1]
        self.role = data[2]


def create_users():
    users = []

    with open(CSV_FILE, newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')
        next(csv_data) # skips the first row, which should be headers
        for row in csv_data:
            users.append(User(row))

    pd_session = requests.Session()
    pd_session.headers.update({
        'Authorization': 'Token token={}'.format(API_KEY),
        'Content-Type': 'application/json',
        'From': PD_EMAIL
    })

    print("Starting upload")
    for user in users:
        payload = json.dumps({
            'user': {
                'type': 'user',
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
        })
        print(payload)
        response = pd_session.post(ENDPOINT, data=payload)
        if response.status_code != 201:
            raise Warning("Failed to create user {}, process aborted. "
                "Any previous users successfully created. Server responded with"
                " status code {}."
                .format(user.name, response.status_code))
    print("Upload complete")


if __name__ == '__main__':
    create_users()
