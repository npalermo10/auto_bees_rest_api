import requests
import json

def post_data(data_line):
    db_url = "http://192.168.1.5:5000/api/experiments"    
    headers = {'content-type': 'application/json'}
    payload = data_line    
    r = requests.post(db_url, data=json.dumps(payload), headers=headers)

##format of payload = {"exp_name":"on_off", "box":"b", "datetime":"\"2016-08-19T07:03:40.615277\"", "correct":True, "testing":False}
