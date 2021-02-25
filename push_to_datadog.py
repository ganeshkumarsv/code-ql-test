import os
import json
import requests

 

url = 'https://http-intake.logs.datadoghq.com/v1/input'
with open('/home/runner/work/code-ql-test/results/go-builtin.sarif') as f:
    json_obj = json.load(f)
message = '{"message": ' + json.dumps(json_obj) + ', "ddtags":"from:codeql_results"}' 
x = requests.post(url, data=message, headers={'DD-API-KEY':os.environ["DD_API_KEY"], 'Content-Type':'application/json'})

print(x.text)
