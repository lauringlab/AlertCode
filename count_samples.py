'''
This is an example of how to send data to Slack webhooks in Python with the
requests module.
Detailed documentation of Slack Incoming Webhooks:
https://api.slack.com/incoming-webhooks
Code from: https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784
'''

import json
import requests
import pandas as pd

################################################################################
with open('C:/Users/juliegil/Documents/UofM_Work/Lab_Organization/AlertCode/hades_info.txt','r') as file:
    hades_url = file.read()
################################################################################

#print(hades_url)

# read in full lab sample file
samples = pd.read_csv("C:/Users/juliegil/Dropbox (University of Michigan)/MED-LauringLab/SequenceSampleMetadata/FinalSummary/full_compiled_data.csv", dtype = str)
row_count = samples.shape[0]

samples['PlateDate'] = pd.to_datetime(samples['PlateDate'])
platedate1 = str(min(samples['PlateDate']))[0:10]
platedate2 = str(max(samples['PlateDate']))[0:10]

announcement = "From plate runs dated {} to {}, total COVID-19 samples sequenced = {}".format(platedate1, platedate2, row_count)

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = hades_url
slack_data = {'text': announcement}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
