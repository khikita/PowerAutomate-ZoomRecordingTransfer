import os
import json
import os
from pprint import pprint
import responder
import requests

api = responder.API()

PA_URL = os.environ['PA_URL']

@api.route('/')
async def index(req,resp):
    if req.method == "get":
        resp.text = "Zoom"

    if req.method == "post":
        req_data = await req.media()
        print(req_data)
        headers = {'content-type': 'application/json'}
        response = requests.post(PA_URL, data=json.dumps(req_data) ,headers=headers)



if __name__ == '__main__':
    api.run(address='0.0.0.0',debug=True)

