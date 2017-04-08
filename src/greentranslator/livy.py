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
    def get_col (self, col):
        r = self.execute ("sqlContext.sql('select {0} from acs_income')".format (col))


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
    for x in range (0, 10):
        print (acs_income.get_col('B19037E_036'))
    acs_income.close ()

main ()


'''
{'Date': 'Fri, 07 Apr 2017 23:15:15 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/0', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 0, 'state': 'waiting', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/0
{'Date': 'Fri, 07 Apr 2017 23:15:40 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/1', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 1, 'state': 'waiting', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/1
None
{'Date': 'Fri, 07 Apr 2017 23:15:41 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/2', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 2, 'state': 'waiting', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/2
None
{'Date': 'Fri, 07 Apr 2017 23:15:41 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/3', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 3, 'state': 'waiting', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/3
None
{'Date': 'Fri, 07 Apr 2017 23:15:41 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/4', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 4, 'state': 'running', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/4
None
{'Date': 'Fri, 07 Apr 2017 23:15:41 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/5', 'Transfer-Encoding': 'chunked', 'Server': 'Jetty(9.2.16.v20160414)'}
{'id': 5, 'state': 'waiting', 'output': None}
statement url: http://localhost:8998/sessions/0/statements/5
None
{'Date': 'Fri, 07 Apr 2017 23:15:41 GMT', 'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Location': '/sessions/0/statements/6', 'Transfer-Encoding': 'chunked', 'Server': 'Je

'''
