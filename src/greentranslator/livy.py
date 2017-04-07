import json, pprint, requests, textwrap, time, sys

class LivyContext(object):
    def __init__(self, host='http://localhost:8998', kind='pyspark'):
        self.host = host
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
        data = { 'code': textwrap.dedent (code) }
        r = requests.post(self.statements_url, data=json.dumps(data), headers=self.headers)
        print (r.headers)
        print (r.json ())
        statement_url = self.host + r.headers['location']
        print ('statement url: {}'.format (statement_url))
        r = None
        while True:
            r = requests.get(statement_url, headers=self.headers).json ()
            if r['state'] == 'available':
                break

        if not r['output']['status'] == 'ok':
            print (r)
            raise "Error: {}".format (r)

        return r['output']['data']['text/plain']

    def close (self):
        requests.delete(self.session_url, headers=self.headers)




acsLoaderCode="""
class ACSLoader(object):
    def __init__(self, path, table, sample_size=1.0):
        self.path = path
        self.rdd = self.load (sample_size=sample_size)
        self.rdd.toDF().registerTempTable (table)
    def load (self, sample_size=1.0):
        print (self.path)
        return sqlContext.read.                                     \
            format('com.databricks.spark.csv').                     \
            options(comment='#').                                   \
            options(delimiter=",").                                 \
            options(header='true').                                 \
            load(self.path).rdd.                                   \
            sample (False, sample_size, 1234)
acs = ACSLoader (
    path = "/projects/stars/translator/var/acs/dataworld/uscensusbureau-acs-2015-5-e-income/data/USA_All_States.csv",
    table = "acs_income")
"""

class ACSIncome(LivyContext):
    def __init__(self):
        LivyContext.__init__(self)
        r = self.execute (acsLoaderCode)
    def get_B19037E_036 (self):
        r = self.execute ("sqlContext.sql('select {0} from acs_income")


def main0 ():
    code_path = sys.argv[1]
    lc = LivyContext ()
    with open(code_path, 'r') as stream:
        code = stream.read ()
        print (code)
        print(lc.execute (code))
    lc.close ()

def main ():
    acs_income = ACSIncome ()
    print (acs_income.get_B19037E_036 ())


main ()

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

