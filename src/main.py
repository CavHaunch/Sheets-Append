# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from time import time, sleep
import creds

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1PYfEx_3jP0RZxd9bE0QMRhMKw_O0a9C9Opc-zpFrlUA'
RANGE_NAME = 'Sheet1'

def main():
    
    service = creds.create_service(SCOPES)

    #Spreadsheet append parameters
    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED'

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    
    # Initiate timing variable
    start = time()

    # Initialise data structure
    value_range_body = {}
    value_range_body["values"] = [[]]

    # Call the Sheets API
    sheet = service.spreadsheets()
    for i in range(20):
        current_time = time() - start
        value_range_body = {
            "values": [
                [
                    "{}".format(current_time),
                    "{}".format(i)
                ]
            ]
        }
        sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME,
                                valueInputOption=value_input_option, 
                                insertDataOption=insert_data_option, 
                                body=value_range_body).execute()

if __name__ == '__main__':
    main()
# [END sheets_quickstart]
