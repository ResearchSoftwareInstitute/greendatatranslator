import json, pprint, requests, textwrap, time


pprint.pprint(r.json())

requests.delete(session_url, headers=headers)

class LivyContext(object):
    def __init__(self, host, kind='pyspark'):
        self.host = 'http://localhost:8998'
        self.data = { 'kind' : kind }
        self.headers = { 'Content-Type': 'application/json' }
        r = requests.post(host + '/sessions', data=json.dumps(self.data), headers=self.headers)
        #print (r.json())
        self.session_url = host + r.headers['location']
        self.statements_url = self.session_url + '/statements'
        while True:
            r = requests.get (self.session_url, headers=self.headers)
            #print (r.json ())
            if r.json()['state'] == 'idle':
                break
            else:
                time.sleep (2)
                print (".")

    def execute (self, code):
        data = { 'code': textwrap.dedent (code)) }
        r = requests.post(self.statements_url, data=json.dumps(self.data), headers=self.headers)
        r = None
        while True:
            r = requests.get(statement_url, headers=headers).json ()
            if r['state'] == 'available':
                break
        return r

    def close (self):
        requests.delete(self.session_url, headers=self.headers)


'''
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'running', 'output': None}
{'id': 0, 'state': 'available', 'output': {'status': 'ok', 'execution_count': 0, 'data': {'text/plain': 'Pi is roughly 3.145720'}}}
{'id': 0,
 'output': {'data': {'text/plain': 'Pi is roughly 3.145720'},
            'execution_count': 0,
            'status': 'ok'},
 'state': 'available'}
'''

