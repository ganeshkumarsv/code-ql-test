import os
import json
import requests

 

url = 'https://http-intake.logs.datadoghq.com/v1/input'
with open('/home/runner/work/code-ql-test/results/go-builtin.sarif') as f:
    json_obj = json.load(f)
x = requests.post(url, data = json_obj, headers={'DD-API-KEY':os.environ["DD_API_KEY"], 'Content-Type':'application/json'})

print(x.text)
